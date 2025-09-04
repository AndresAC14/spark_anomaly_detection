[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white)
[![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://img.shields.io/badge/Docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)
[![FastAPI](https://img.shields.io/badge/FastAPI-%23009688.svg?style=flat&logo=fastapi&logoColor=white)](https://img.shields.io/badge/FastAPI-%23009688.svg?style=flat&logo=fastapi&logoColor=white)
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

# Real-Time Anomaly Detection with Spark Structured Streaming
An end-to-end system for **real-time anomaly detection** in traffic and pollution data streams using **Spark Structured Streaming**, **FastAPI**, and **Streamlit**.


# 📦 Installation

### Requirements
- [Docker Desktop](https://docs.docker.com/desktop/)
- [Visual Studio](https://code.visualstudio.com/download)
- [Python 3.11](https://www.python.org/) (only needed if you want to run outside Docker)
- [uv](https://github.com/astral-sh/uv) (Python package manager, used for manual runs)

Clone the repository:

```sh
git clone https://github.com/AndresAC14/spark_anomaly_detection
```
```sh
cd spark_anomaly_detection
```

# 🚀 Usage

### 1. Start all services with Docker

Run the following commands to build and start all containers:

```sh
docker compose build
```


```sh
docker compose up
```


Stop containers when finished:

```sh
docker compose down
```




### 2. Run components manually (alternative)

Install Python dependencies with uv:

```sh
uv sync
```

Then enable the Python environment in different consoles to run each component individually:

```sh
source .venv/Scripts/activate   # Linux/Mac
.venv\Scripts\activate      # Windows (PowerShell)
```


#### Backend API (FastAPI)

```sh
cd spark_anomaly_detection/backend
fastapi dev api/main.py
```

#### Streaming Data Extraction
```sh
cd spark_anomaly_detection/backend
python extract_service/streaming.py
```

#### Spark Streaming Service

```sh
cd spark_anomaly_detection/backend
python ml-service/anomaly_detection.py
```
#### Frontend with streamlit

```sh
streamlit run frontend/app.py
```

# 🛠 Services Overview

* **FastAPI** → REST API to collect data and alerts (`/data`, `/alert` endpoints).
* **Streaming Service** → Generates hourly CSV files simulating live data.
* **Spark Structured Streaming** → Reads new files, applies ML models, and posts results to the API.
* **Streamlit** → Real-time visualization of data and alerts.

---

# 📊 Dashboard Preview

![Alerts](/images/front1.png)

![Charts](/images/front2.png)

---

# ⚠️ Notes

* Do not forget to stop containers if running in the background:

  ```sh
  docker stop <container_id>
  ```
* Replace `<container_id>` with the actual container name or ID from `docker ps`.

---