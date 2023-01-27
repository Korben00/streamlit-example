# Un script python pour streamlit qui utilise rembg pour supprimer l'arrière-plan d'une image
import streamlit as st
from PIL import Image
from rembg import remove
from io import BytesIO


st.set_page_config(page_title="RIMOUVEUR DE LA MORT", page_icon=":skull:", layout="wide")
st.write("## RIMOUVEUR DE LA MORT")
st.write("Uploadez une image :dog: pour retirer l'arrière-plan et la rendre transparente.")
st.sidebar.write("## Uploadeur")


col1, col2 = st.columns(2)

def convert_image(image):
    buf = BytesIO()
    image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im

def fix_image(image):
    image = Image.open(image)
    col1.write("Image originale")
    col1.image(image)
    fixed = remove(image)
    col2.write("Image détourée")
    col2.image(fixed)

    st.sidebar.write("\n")
    st.sidebar.download_button("Télécharger l'image", convert_image(fixed), 'image_detouree.png', 'image/png')

image_upload = st.sidebar.file_uploader("Choisissez une image", type=['png', 'jpg', 'jpeg'])


if image_upload is not None:
    fix_image(image_upload)
else:
    fix_image("./girl.jpg")
