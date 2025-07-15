from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import pickle
import requests
import time

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

# Load the pre-trained models
with open('database\\models\\pollution_model.pkl', 'rb') as f:
    pollution_model = pickle.load(f)

with open('database\\models\\traffic_model.pkl', 'rb') as f:
    traffic_model = pickle.load(f)

# Read CSV files from the folder as they arrive
input_path = "database\\streaming_data"
df_stream = (
    spark.readStream
    .option("maxFilesPerTrigger", 1)
    .schema(schema)
    .csv(input_path)
)

# Preprocess: extract hour from FECHA_HORA
df_stream = df_stream.withColumn("HORA", hour(to_timestamp(col("FECHA_HORA"), "yyyy-MM-dd HH:mm:ss")))

def send_alert(y_true, y_pred, type: str):
    for actual, predicted in zip(y_true, y_pred):
        percent_diff = abs(predicted - actual) / abs(actual) * 100

        print(f"Actual: {actual} vs Predicted: {predicted} \n Diff% {percent_diff}")
        if percent_diff > 30:
            payload = {"expected": float(actual), "predicted": float(predicted), "type": type}
            print(f"ALERT POLLUTION: {payload}")
            try:
                requests.post("http://localhost:8000/alert", json=payload)
            except Exception as e:
                print(f"Error sending alert: {e}")

def process_batch(df, epoch_id):
    if df.count() == 0:
        pass

    pandas_df = df.select("HORA", "INTENSIDAD", "OCUPACION", "CARGA", "VALOR_CONTAMINACION").toPandas()

    # --- Pollution Prediction ---
    pollution_features = ["HORA", "INTENSIDAD", "OCUPACION", "CARGA"]
    X_pollution = pandas_df[pollution_features]
    y_true_pollution = pandas_df["VALOR_CONTAMINACION"]
    y_pred_pollution = pollution_model.predict(X_pollution)

    send_alert(y_true_pollution, y_pred_pollution, "pollution")


    # --- Traffic Prediction ---
    traffic_features = ["HORA","VALOR_CONTAMINACION", "OCUPACION", "CARGA"]
    X_traffic = pandas_df[traffic_features]
    y_true_traffic = pandas_df["INTENSIDAD"]
    y_pred_traffic = traffic_model.predict(X_traffic)

    send_alert(y_true_traffic, y_pred_traffic, "traffic")

    time.sleep(30)

# Start the streaming query
query = df_stream.writeStream.foreachBatch(process_batch).start()
query.awaitTermination()