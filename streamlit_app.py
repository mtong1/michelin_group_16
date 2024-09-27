import streamlit as st
from langchain_groq import ChatGroq
import getpass
import os

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

st.title('🦜🔗 Quickstart App')

groq_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2 )
    st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
#   if not groq_api_key.startswith(''):
#     st.warning('Please enter your Groq API key!', icon='⚠')
  if submitted and groq_api_key.startswith('sk-'):
    generate_response(text)