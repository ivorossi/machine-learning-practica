import os

from src.main.python.gesturedetector.config.configurations import Config
from src.main.python.gesturedetector.scrapers.scraper_ml import download_images_by_category

if __name__ == "__main__":
    download_path = Config.get_config()['download_folder']
    folder = os.path.join(download_path)
    os.makedirs(folder, exist_ok=True)
    site_id = "MLA"
    category_id = "muñecos"
    limit = 5
    download_images_by_category(site_id, category_id, limit)
