from fastapi import FastAPI
from models import Alert, DataPoint
from typing import List

app = FastAPI()

alerts_storage: List[Alert] = []
data_storage: List[DataPoint] = []

@app.post("/alert")
def receive_alert(alert: Alert):
    alerts_storage.append(alert)
    return {"message": "Alert received"}

@app.post("/data")
def receive_data_point(data_point: DataPoint):
    data_storage.append(data_point)
    return {"message": "Data point received"}

@app.get("/alerts")
def get_alerts():
    return alerts_storage

@app.get("/data")
def get_data():
    return data_storage
