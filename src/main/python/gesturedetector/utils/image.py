import os.path
from io import BytesIO

import cv2
import numpy as np
import requests
import imghdr
from PIL import Image

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
    try:
        with Image.open(BytesIO(image_bytes)) as img:
            return img.format.lower()
    except Exception:
        return 'undefined'


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


def to_cv2_image(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
