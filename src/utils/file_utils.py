import os
from settings.config import Config


def create_blob_image_if_not_exist(path: str = Config.DATASET_FOLDER):

    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

    return








