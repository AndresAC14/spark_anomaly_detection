import sys
import time
import urllib.request

URL_TRAFFIC = "https://datos.madrid.es/egob/catalogo/202087-0-trafico-intensidad.xml"
DIRECTORY_TRAFFIC = "traffic_data"
secondsToSleep = 10

while True:
    time_stamp = str(time.time())

    newFile = DIRECTORY_TRAFFIC + "/" + str(time_stamp).replace(".","") + ".xml"
    urllib.request.urlretrieve(URL_TRAFFIC, newFile)

    time.sleep(secondsToSleep)