import streamlit as st
from utils import pred_pipe

MODEL_PATH = "NLP/sentiment_classifier.pkl"

st.title(
    "Welcome to Movie Review Classification tool",
    text_alignment = "center"    
)

user_input = st.text_area(label = "Movie Review", height=250)

if st.button(label= "Predict !"):
    sentiment = pred_pipe(user_input, MODEL_PATH)
    
    sentiment_color = "green" if sentiment == "Positive" else "red"
    st.markdown(f"<h2 style='text-align: center; color: {sentiment_color};'>{sentiment}</h2>", unsafe_allow_html=True)
    
    # st.subheader(sentiment, text_alignment="center")