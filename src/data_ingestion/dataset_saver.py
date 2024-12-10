import os
from PIL import Image
from datasets import Dataset
from settings.config import Config
from src.utils.file_utils import create_blob_image_if_not_exist


def save_blob_image_if_not_exist(dataset: Dataset, path: str = Config.DATASET_FOLDER, num_images: int = 1000):

    print(path)
    if not os.path.exists(path):
        create_blob_image_if_not_exist(path)

    for i in range(num_images):
        image_path = os.path.join(path, f'flower_{i+1}.png')

        #Validate if image exist
        if os.path.exists(image_path):
            print(f'==== Image {image_path} already exists ====')
            continue

        #Save image
        print(f'==== Save image {i+1} de {num_images}.... ====')
        image = dataset['train'][i]["image"]

        #Validate type image
        if isinstance(image, Image.Image):
            image.save(image_path)
            print(f"==== Saved image {image_path}.... ====")
        else:
            print(f'==== Incompatible image {image_path}.... {type(image)} ====')

    print(f'==== All images saved ====')