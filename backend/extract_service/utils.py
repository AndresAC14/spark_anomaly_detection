from datetime import datetime
import time
import urllib.request
from minio import Minio
from io import BytesIO


def get_streaming_data(client: Minio, url: str, directory: str, sleep_time: int):
    # Ensure bucket exists
    if not client.bucket_exists(directory):
        client.make_bucket(directory)

    while True:
        time_stamp = datetime.now().isoformat()
        file_name = f"{time_stamp}.xml"

        # Download the file content into memory
        with urllib.request.urlopen(url) as response:
            data = response.read()

        # Upload to MinIO
        client.put_object(
            directory,
            file_name,
            data=BytesIO(data),
            length=len(data),
            content_type="application/xml",
        )

        print(f"Uploaded {file_name} to bucket '{directory}'")

        time.sleep(sleep_time)
