import os
import sys

from src.utils.image_utils import show_image_from_uri, show_image_from_uri_plot
import matplotlib
from chromadb import Collection
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt


def query_db(collection: Collection, query: str, results: int = 3):
    """
    Query a collection using a query.
    :param collection: Chromadb collection
    :param query: Search query
    :param : Chromadb Collection instance, number of results to return
    :return: results: Retrieval results of query (default 3)
    """
    print(f"==== Querying database for {query} ====")
    results = collection.query(
        query_texts=[query],
        n_results=results,
        include=['uris', 'distances']
    )

    return results


def print_results(results: dict):
    for idx, uri in enumerate(results['uris'][0]):
        print(f"ID: {results['ids'][0][idx]}")
        print(f"Distance: {results['distances'][0][idx]}")
        print(f"URI: {uri}")

        show_image_from_uri_plot(uri)
        print('\n')
