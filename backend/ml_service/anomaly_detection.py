from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import pickle
# import requests
# Initialize Spark session
spark = SparkSession.builder.appName("PollutionPredictionStreaming").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Define the schema for incoming CSV files
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

schema = StructType([
    StructField("FECHA_HORA", StringType(), True),
    StructField("INTENSIDAD", DoubleType(), True),
    StructField("OCUPACION", DoubleType(), True),
    StructField("CARGA", DoubleType(), True),
    StructField("VALOR_CONTAMINACION", DoubleType(), True)
])

# Load the pre-trained model
with open('database\\models\\pollution_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Read CSV files from the folder as they arrive
input_path = "database\\streaming_data"
df_stream = (
    spark.readStream
    .option("maxFilesPerTrigger", 1)
    .schema(schema)
    .csv(input_path)
)

# Preprocess: extract hour from FECHA_HORA
# df_stream = df_stream.withColumn("HORA", hour(to_timestamp(col("FECHA_HORA"), "yyyy-MM-dd")))
df_stream = df_stream.withColumn("HORA", hour(to_timestamp(col("FECHA_HORA"), "yyyy-MM-dd HH:mm:ss")))

def process_batch(df, epoch_id):
    if df.count() == 0:
        pass

    pandas_df = df.select("HORA", "INTENSIDAD", "OCUPACION", "CARGA", "VALOR_CONTAMINACION").toPandas()

    feature_cols = ["HORA", "INTENSIDAD", "OCUPACION", "CARGA"]
    X = pandas_df[feature_cols]
    y_true = pandas_df["VALOR_CONTAMINACION"]

    y_pred = model.predict(X)

    for actual, predicted in zip(y_true, y_pred):
        if abs(predicted - actual) > 0.1:
            payload = {"expected": actual, "predicted": predicted}
            # fix: QUE NO SALGA NP.FLOAT(N.0000000000)
            print(f"ALERT: {payload}")
            # Uncomment to send alert to FastAPI
            # try:
            #     requests.post("http://localhost:8000/alert", json=payload)
            # except Exception as e:
            #     print(f"Error sending alert: {e}")

# Start the streaming query
query = df_stream.writeStream.foreachBatch(process_batch).start()
query.awaitTermination()