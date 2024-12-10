import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

from src.data_ingestion.dataset_loader import load_dataset_for_work
from src.data_ingestion.dataset_saver import save_blob_image_if_not_exist
from src.database.vector_db import get_chroma_collection, bulk_load_images
from settings.config import Config



def initialize_db():

    print("==== Loading dataset ====")
    flowers_dataset = load_dataset_for_work(Config.DATASET_NAME)

    print("==== Loading images to Repo ====")
    save_blob_image_if_not_exist(flowers_dataset, Config.DATASET_FOLDER)

    print("==== Get ChromaDB Collection ====")
    collection = get_chroma_collection(Config.CHROMA_COLLECTION_NAME)

    print("==== Bulk Load Images ====")
    bulk_load_images(collection=collection, dataset_folder=Config.DATASET_FOLDER)


if __name__ == "__main__":

    initialize_db()

å

