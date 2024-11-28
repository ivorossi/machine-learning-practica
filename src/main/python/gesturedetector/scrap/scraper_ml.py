import os
import requests
from src.main.python.gesturedetector.config.configurations import Config

BASE_URL = Config.get_config()['mercadolibre_api_URL']


def fetch_category_items(site_id, category_id, limit=10):
    """Obtiene productos de una categoría y sitio específicos."""
    url = f"{BASE_URL}/sites/{site_id}/search?category={category_id}&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error al obtener los productos: {response.status_code}")
        return []


def download_image(image_url, folder, image_name):
    """Descarga una imagen de una URL y la guarda en la carpeta especificada."""
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(folder, image_name), "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Imagen guardada: {image_name}")
    else:
        print(f"Error al descargar la imagen: {image_url}")


def download_images_by_category(site_id, category_id, limit=10):
    """Descarga imágenes de productos en una categoría y sitio específicos."""
    items = fetch_category_items(site_id, category_id, limit)

    # Crear una carpeta para guardar las imágenes
    folder = os.path.join("images", category_id)
    os.makedirs(folder, exist_ok=True)

    for item in items:
        image_url = item.get("thumbnail")  # URL de la imagen de miniatura
        if image_url:
            image_name = f"{item['id']}.jpg"
            download_image(image_url, folder, image_name)


if __name__ == "__main__":
    # Configura el sitio y categoría que deseas buscar
    site_id = "MLA"  # MercadoLibre Argentina
    category_id = "MLA5725"  # ID de una categoría (ejemplo: 'MLA5725' para Notebooks)
    limit = 5  # Número de imágenes a descargar

    download_images_by_category(site_id, category_id, limit)
