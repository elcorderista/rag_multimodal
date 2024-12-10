#Cargamos el dataset desde Huggin Face
from datasets import load_dataset
from settings.config import Config


def load_dataset_for_work(datset_name:str = Config.DATASET_NAME):
    """
    Load a dataset using the name from the library Hugging Face
    :param datset_name:
    :return: Database dict, Obeject Dataset from Huggin Face
    """
    print(f"==== Load Data SET {Config.DATASET_NAME} ====")
    dataset = load_dataset(datset_name)
    return dataset