from src.database.queries import query_db
from src.utils.prompt_utils import format_prompt_inputs
from src.utils.image_utils import show_image_from_uri, show_image_from_uri_plot
from src.llm.chain import get_bouquet_chain
from src.database.vector_db import get_chroma_collection
import streamlit as st
@st.cache_data
def process_query(query: str):
    """
    Process the user query to retrieve results and generate bouquet suggestions.

    :param query: User query input
    :param collection: ChromaDb collection object
    :param vision_chain: LangChain chain combining prompt, model and parser
    :param n_results: Number of results to return
    :return: tuple: Results from the database query and response from the model.

    """
    vision_chain = get_bouquet_chain()
    collection = get_chroma_collection()

    results = query_db(
        collection=collection,
        query=query,
    )

    prompt_input = format_prompt_inputs(results, query)
    response = vision_chain.invoke(prompt_input)
    return results, response
def show_results(results, response):

    #PrintOutput
    print("\n Here are some ideas for a bouquet arrangement based on your query: \n")
    print(response)
    show_image_from_uri_plot(results["uris"][0][0])
    show_image_from_uri_plot(results["uris"][0][1])

    print("\n Image URI: \n")
    print(f"Image 1: {results["uris"][0][0]}")
    print(f"Image 2: {results["uris"][0][1]}")



