import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import getpass
import os
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI

# if "GROQ_API_KEY" not in os.environ:
#     os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

st.title('🦜🔗 Quickstart App')


uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    st.write("File uploaded successfully!")

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
#   if submitted:
#     generate_response(text)

