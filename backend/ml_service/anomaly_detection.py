from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, TimestampType, IntegerType, FloatType
import pickle

# Load the pre-trained model
with open('database\\models\\pollution_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Start Spark Session
spark = SparkSession.builder.appName("StreamingModelComparison").getOrCreate()

# Define the expected schema
schema = StructType([
    StructField("FECHA_HORA", TimestampType(), True),
    StructField("IDELEM", IntegerType(), True),
    StructField("INTENSIDAD", FloatType(), True),
    StructField("OCUPACION", FloatType(), True),
    StructField("CARGA", FloatType(), True),
    StructField("VALOR_CONTAMINACION", FloatType(), True)
])

# Read the hourly CSV files in streaming mode
streaming_df = spark.readStream.schema(schema).option("maxFilesPerTrigger", 1).csv('data_by_hour')

def process_batch(df, epoch_id):
    pandas_df = df.toPandas()

    if not pandas_df.empty:
        # Select relevant features for the model
        features = pandas_df[['INTENSIDAD', 'OCUPACION', 'CARGA']]
        
        # Make predictions
        predictions = model.predict(features)
        
        # Compare predictions with actual pollution values
        pandas_df['MODEL_PREDICTION'] = predictions
        pandas_df['DIFFERENCE'] = pandas_df['VALOR_CONTAMINACION'] - pandas_df['MODEL_PREDICTION']

        print(pandas_df[['FECHA_HORA', 'IDELEM', 'VALOR_CONTAMINACION', 'MODEL_PREDICTION', 'DIFFERENCE']])

# Stream processing: apply the process_batch function on each micro-batch
query = streaming_df.writeStream.foreachBatch(process_batch).start()

query.awaitTermination()
