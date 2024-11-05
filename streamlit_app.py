import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import getpass
import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI
from langchain_ollama import ChatOllama
from langchain.llms import Ollama


# if "GROQ_API_KEY" not in os.environ:
#     os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
# llama_model = ChatOllama(model="llama3.2", temperature=0,)
llm = Ollama(model="llama3.2")

st.title('🦜🔗 Quickstart App')


uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

csv_to_string = ""


if uploaded_file is not None:
    st.write("File uploaded successfully!")
    data = pd.read_csv(uploaded_file)
    st.write("Here's a preview of your data:")
    st.write(data.head())
    csv_to_string = data.head().to_string()

    st.write(csv_to_string)
    prompt = f"Using {csv_to_string} which is a CSV file as a string. Give me the summary of the data, the amount of rows, and columns."
    # response = llama_model(prompt)
    messages = [ ("system", "You are a CSV analyser"),  ("human", f"Using {csv_to_string} which is a CSV file as a string. Give me the summary of the data, the amount of rows, and columns.")]
    result = llm.invoke(messages)
    st.write(result)

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
#   if submitted:
#     generate_response(text)

