import os

import chromadb
from chromadb.utils.data_loaders import ImageLoader
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from settings.config import Config



def get_chroma_collection(collection_name: str = Config.CHROMA_COLLECTION_NAME) -> chromadb.Collection:
    '''
    Configure and retrieve ChromaDB for images using multimodals embeddings
    If collection_name all ready exist, it retrieve it.
    :param collection_name:
    :return:colleccion
    '''
    chroma_client = chromadb.PersistentClient(path=Config.CHROMA_DB_PATH)
    image_loader = ImageLoader()
    embedding_function = OpenCLIPEmbeddingFunction()

    # Create o Retriever Collection
    collection = chroma_client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function,
        data_loader=image_loader,
    )

    print(f"==== Vectorial Data Base configured: {Config.CHROMA_COLLECTION_NAME}")
    return collection


def get_existing_ids(collection: chromadb.Collection) -> list:
    """
    Retrieve all existing IDs for a collection
    :param collection: Chromadb collection
    :return: Existing IDs
    """
    try:
        results = collection.peek(limit=10000)
        return results["ids"] if results else []
    except Exception as e:
        print(f"---- Error: To retrieve existing IDs: {e} ----")
        return []


def bulk_load_images(collection: chromadb.Collection, dataset_folder: str):
    """
    Load local image to ChromaDB
    :param collection: Chromadb collection
    :param dataset_folder: Folder where images are located
    """
    ids = []
    uris = []
    existing_ids = set(get_existing_ids(collection))
    for i, filename in enumerate(os.listdir(dataset_folder)):
        if filename.endswith(".png"):
            file_path = os.path.join(dataset_folder, filename)
            ids.append(str(i))
            uris.append(file_path)

        #Get Existing ids
        new_ids = []
        new_uris = []
        update_ids = []
        update_uris = []

        #Validate if an image is new or all ready exist.
        for idx, uri in zip(ids, uris):
            if idx in existing_ids:
                update_ids.append(idx)
                update_uris.append(uri)
            else:
                new_ids.append(idx)
                new_uris.append(uri)

        #Add new images
        if new_ids:
            print("==== Adding new images... ====")
            collection.add(
                ids=new_ids,
                uris=new_uris,
            )
            print(f"==== Added {len(new_ids)} new images... ====")

        #Update new images
        if update_ids:
            print("==== Updating existing images... ====")
            collection.update(
                ids=update_ids,
                uris=new_uris,
            )
            print(f"==== Updated {len(update_ids)} new images... ====")

    print("=== Bulk loading images completed ====")

