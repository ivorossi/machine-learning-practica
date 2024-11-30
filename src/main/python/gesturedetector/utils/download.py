import os.path
import requests
import imghdr
from src.main.python.gesturedetector.config.configurations import Config

download_path = Config.get_config()['download_folder']


def download_image_with_format(url: str, name: str):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        image_bytes = response.content
        image_format = imghdr.what(None, h=image_bytes)
        if not image_format:
            print("Error: Unable to determine the image format.")
            return

        file_path = os.path.join(download_path, f"{name}.{image_format}")
        with open(file_path, "wb") as file:
            file.write(image_bytes)

        print(f"Image downloaded and saved as: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image: {e}")
