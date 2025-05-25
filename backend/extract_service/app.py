from utils import get_streaming_data
import threading
import sys
import time
import signal


URL_TRAFFIC = "https://datos.madrid.es/egob/catalogo/202087-0-trafico-intensidad.xml"
URL_POLLUTION = (
    "https://datos.madrid.es/egob/catalogo/212531-10530806-calidad-aire-tiempo-real.xml"
)
DIR_TRAFFIC = "database/traffic_data"
DIR_POLLUTION = "database/pollution_data"
traffic_sleep_time = 300  # 5 min
pollution_sleep_time = 1200  # 20 min


def signal_handler(sig, frame):
    print("Stopping Extraction Service...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


traffic_thread = threading.Thread(
    target=get_streaming_data,
    args=(URL_TRAFFIC, DIR_TRAFFIC, traffic_sleep_time),
    daemon=True,
)
pollution_thread = threading.Thread(
    target=get_streaming_data,
    args=(URL_POLLUTION, DIR_POLLUTION, pollution_sleep_time),
    daemon=True,
)

traffic_thread.start()
pollution_thread.start()

while True:
    time.sleep(1)
