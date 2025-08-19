FROM bitnami/spark:3.5.0

USER root
WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN python3.11 -m pip install --upgrade pip && \
    python3.11 -m pip install pandas requests scikit-learn

ENV PYSPARK_PYTHON=python3.11

CMD ["python", "anomaly_detection.py"]
