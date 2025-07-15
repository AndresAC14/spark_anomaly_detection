[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Real-Time Anomaly Detection with Spark Structured Streaming
Real-Time Anomaly Detection in Traffic and Pollution Data Stream with Spark Structured Streaming.


# Installation

# Use It

Do not forget to stop Docker after using it in background: docker stop minio

Run docker for data extraction service:

```sh
#to-do
```



# Services

## Launch API:

```sh
cd spark_anomaly_detection\backend
fastapi dev api/main.py
```

## Launch Streaming Data Extraction
```sh
cd spark_anomaly_detection\backend
python extract_service\streaming.py
```


## Launch Spark

```sh
cd spark_anomaly_detection\backend
python ml-service/anomaly_detection.py
```
## Launch frontend with streamlit

```sh
streamlit run frontend/app.py
```