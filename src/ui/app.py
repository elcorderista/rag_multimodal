import os
import sys

BASE_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(BASE_dir)

from src.utils.image_utils import show_image_from_uri
from src.ui.logic import process_query
import streamlit as st


#Configuracion de St
st.set_page_config(page_title="Flower Arrangement Service", layout="wide")
st.title("🌸 Flower Arrangement Query Service 🌸")

#Inicializacion
st.info("Welcome to the Flower Arrangement Services")
# Get the chain

user_query = st.text_input("Enter your query (e.g., 'wedding bouquet with pink roses'):")
if user_query:
    with st.spinner("Retrieving results..."):
        results, response = process_query(user_query)

    st.write("Here are some images base on your query:")
    for uri in results["uris"][0]:
        show_image_from_uri(uri)
    st.markdown(f"### Suggestions for bouquet arrangment:")
    st.write(response)
