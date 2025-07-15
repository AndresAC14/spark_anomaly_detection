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

🚀 INSTRUCCIONES PARA LEVANTAR TODO
Lanzar la API:

lua
Copiar
Editar
uvicorn backend.api.main:app --reload
Ejecutar el proceso Spark

bash
Copiar
Editar
python backend/spark_process.py
Levantar el frontend Streamlit

arduino
Copiar
Editar
streamlit run frontend/app.py