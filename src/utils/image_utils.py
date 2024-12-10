from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt

def show_image_from_uri(uri:str, width:int=200):
    try:
        img = Image.open(uri)
        st.image(img, width=width)
    except Exception as e:
        print(f"--- Error: Cannot open image from {uri}")


def show_image_from_uri_plot(uri:str):
    plt.imshow(Image.open(uri))
    plt.axis('off')
    plt.show()