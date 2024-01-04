# Q&A Chatbot

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
api_key =  os.environ['GOOGLE_API_KEY']

def get_google_response(question):
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key, temperature=0.6)
    response = llm.predict(question)
    return response
response = get_google_response(input)

###  Initialize the streamlit app

st.set_page_config(page_title="Q&A Demo")


st.header("Langchain Application")
input= st.text_input("input: ", key="input")

submit = st.button("Ask the question")

if submit:
    st.subheader("The Response is")
    st.write(response)