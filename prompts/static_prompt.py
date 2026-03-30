from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import streamlit as st

load_dotenv()
model = init_chat_model(
    model = "groq:llama-3.1-8B-instant"
)

st.header("Research Tool")
user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    response = model.invoke(user_input)
    st.write(response.content)