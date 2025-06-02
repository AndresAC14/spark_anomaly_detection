import os
import time
from datetime import datetime
import urllib.request

def get_streaming_data(url: str, folder: str, sleep_time: int):
    
    while True:
        time_stamp = datetime.now().isoformat().replace(":", "-")
        file_name = f"{time_stamp}.xml"
        file_path = os.path.join(folder, file_name)

        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()

            with open(file_path, "wb") as f:
                f.write(data)

            print(f"Saved {file_path}")

        except Exception as e:
            print(f"Error saving file: {e}")

        time.sleep(sleep_time)
