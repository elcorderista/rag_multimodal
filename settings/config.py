import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    CHROMA_DB_PATH = os.path.join(BASE_DIR, os.getenv('CHROMA_DB_PATH'))
    CHROMA_COLLECTION_NAME = os.getenv('CHROMA_COLLECTION_NAME')
    CHAT_MODEL = os.getenv('CHAT_MODEL')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    MODEL_TEMPERATURE = float(os.getenv('MODEL_TEMPERATURE'))
    DATASET_NAME = os.getenv('DATASET_NAME')
    DATASET_FOLDER = os.path.join(BASE_DIR, os.getenv('DATASET_FOLDER'))
    DEBUG = os.getenv('DEBUG')

    @classmethod
    def print_config(cls):
        """Print configuration variables."""
        print("----- CURRENT CONFIGURATION -----")
        print(f'BASE_DIR: {cls.BASE_DIR}')
        print(f"CHORMA_DB_PATH: {cls.CHROMA_DB_PATH}")
        print(f"CHROMA_COLLECTION_NAME: {cls.CHROMA_COLLECTION_NAME}")
        print(f"CHAT_MODEL: {cls.CHAT_MODEL}")
        print(f"MODEL_TEMPERATURE: {cls.MODEL_TEMPERATURE}")
        print(f"DEBUG: {cls.DEBUG}")
        print(f"DATASET_FOLDER: {cls.DATASET_FOLDER}")
        print("----- END CONFIGURATION -----")


#Test
if __name__ == "__main__":
    Config.print_config()