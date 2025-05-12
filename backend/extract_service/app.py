from minio import Minio
from utils import get_streaming_data
import threading
import sys

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False,
)

URL_TRAFFIC = "https://datos.madrid.es/egob/catalogo/202087-0-trafico-intensidad.xml"
URL_POLLUTION = (
    "https://datos.madrid.es/egob/catalogo/212531-10530806-calidad-aire-tiempo-real.xml"
)
DIR_TRAFFIC = "traffic-data"
DIR_POLLUTION = "pollution-data"
traffic_sleep_time = 300  # 5 min
pollution_sleep_time = 1200  # 20 min


# Start both streams in parallel
threading.Thread(
    target=get_streaming_data,
    args=(client, URL_TRAFFIC, DIR_TRAFFIC, traffic_sleep_time),
).start()
threading.Thread(
    target=get_streaming_data,
    args=(client, URL_POLLUTION, DIR_POLLUTION, pollution_sleep_time),
).start()
