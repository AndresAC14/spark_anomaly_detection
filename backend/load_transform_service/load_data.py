from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

# Setup SparkSession
spark = SparkSession.builder.appName("MinIO XML Streaming").getOrCreate()

# MinIO config
# spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", os.getenv("MINIO_ENDPOINT", "http://minio:9000"))
# spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", os.getenv("MINIO_ACCESS_KEY", "minioadmin"))
# spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", os.getenv("MINIO_SECRET_KEY", "minioadmin"))
# spark._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
# spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

# Define source directory (pollution or traffic)
bucket = "traffic-data"  # or "pollution-data"
input_path = f"s3a://{bucket}/"

# Read stream from MinIO
df = (
    spark.readStream.format("xml")
    .option("host", "localhost")
    .option("port", 9000)
    .option("header", "true")
    .load(input_path)
)

print(df)
