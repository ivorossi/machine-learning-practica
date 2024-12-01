import os.path
from io import BytesIO
import requests
import imghdr
from PIL.Image import Image

from src.main.python.gesturedetector.config.configurations import Config

download_path = Config.get_config()['download_folder']


def download_image(url: str):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException:
        return None


def get_image_format(image_bytes):
    image_format = imghdr.what(None, h=image_bytes)
    if not image_format:
        image_format = 'undefined'
    return image_format


def is_integrity_correct(image_byte):
    try:
        with Image.open(BytesIO(image_byte)) as img:
            img.verify()
        return True
    except OSError:
        return False


def save_image(image_bytes, name):
    if image_bytes and is_integrity_correct(image_bytes):
        file_path = os.path.join(download_path, f"{name}.{get_image_format(image_bytes)}")
        with open(file_path, "wb") as file:
            file.write(image_bytes)
