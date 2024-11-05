import streamlit as st
import pandas as pd
from langchain_ollama import ChatOllama
from langchain_experimental.agents import create_pandas_dataframe_agent

# if "GROQ_API_KEY" not in os.environ:
#     os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
llama_model = ChatOllama(model="llama3.2", temperature=0)

st.title('🦜🔗 Quickstart App')

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    data = pd.read_csv(uploaded_file)
    st.write("Here's a preview of your data:")
    st.write(data.head())

    agent = create_pandas_dataframe_agent(llama_model, data, verbose=True, allow_dangerous_code=True)

    user_question= st.text_input("Enter your question here:", "How many rows are there?")

    if st.button('Submit'):
        response = agent.run(user_question)
        st.write(response)