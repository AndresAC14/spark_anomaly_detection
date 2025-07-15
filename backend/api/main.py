from fastapi import FastAPI
from models import Alert
from typing import List

app = FastAPI()

# Guarda alertas en memoria temporalmente
alerts_storage: List[Alert] = []

@app.post("/alert")
def receive_alert(alert: Alert):
    print(f"Alert received: {alert}")
    alerts_storage.append(alert)
    return {"message": "Alerta received"}

@app.get("/alerts")
def get_alerts():
    return alerts_storage
