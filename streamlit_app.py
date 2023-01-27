import streamlit as st
from transformers import pipeline

st.title("Analyseur de sentiments")

text = st.text_input("Entrez votre texte ici :")

sentiment_classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

if text:
    result = sentiment_classifier(text)[0]
    st.write("Prediction:", result["label"])
