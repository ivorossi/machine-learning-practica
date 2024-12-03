import requests
from src.main.python.gesturedetector.config.configurations import Config
from src.main.python.gesturedetector.face_detector.face_rcognition_dlib import get_face_descriptor
from src.main.python.gesturedetector.face_detector.face_recognition_mediapipe import detect_face
from src.main.python.gesturedetector.face_detector.face_recognition_opencv import detect_face_in_image
from src.main.python.gesturedetector.utils.image import save_image, download_image, to_cv2_image
from requests.exceptions import Timeout
import time

BASE_URL = Config.get_config()['mercadolibre_api_URL']


def fetch(url, retries=3, delay=5):
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            return response
        except Timeout:
            time.sleep(delay)
    raise Timeout(f"Failed to connect after {retries} attempts")


def fetch_category(site_id, category_id, limit=10, offset=0):
    url = f"{BASE_URL}/sites/{site_id}/search?category={category_id}&limit={limit}&offset={offset}"
    response = fetch(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return []


def fetch_query(site_id, query, limit=50, offset=0):
    url = f"{BASE_URL}/sites/{site_id}/search?q={query}&limit={limit}&offset={offset}"
    response = fetch(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return []


def fetch_item(item_id):
    url = f"{BASE_URL}/items/{item_id}"
    response = fetch(url)
    if response.status_code == 200:
        return response.json().get("pictures", [])
    else:
        return []


def fetch_image(image_id):
    url = f"{BASE_URL}/pictures/{image_id}"
    response = fetch(url)
    if response.status_code == 200:
        variations = response.json().get("variations", [])
        return variations[0]["url"]


def download_images_by_category(site_id, category_id, limit=1):
    items = fetch_query(site_id, category_id, limit)
    for item in items:
        item_id = item.get("id")
        pictures = fetch_item(item_id)
        for picture in pictures:
            image_id = picture.get("id")
            image_url = fetch_image(image_id)
            image_bytes = download_image(image_url)
            if image_bytes:
                image = to_cv2_image(image_bytes)
                if detect_face_in_image(image):
                    save_image(image_bytes, f"{image_id}_cv2")
                if detect_face(image):
                    save_image(image_bytes, f"{image_id}_mediapipe")
                if get_face_descriptor(image):
                    save_image(image_bytes, f"{image_id}_dlib")

            print(image_id)
