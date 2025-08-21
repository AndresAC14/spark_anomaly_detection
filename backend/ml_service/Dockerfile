FROM bitnami/spark:3.5.0

USER root
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip install --no-cache-dir pyspark==3.5.0 pandas requests scikit-learn
USER 1001
WORKDIR /app

COPY . /app
CMD ["python3", "anomaly_detection.py"]
