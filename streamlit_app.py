import streamlit as st
import pandas as pd
from langchain_ollama import ChatOllama
from langchain_experimental.agents import create_pandas_dataframe_agent

llama_model = ChatOllama(model="llama3.2", temperature=0)

st.title('Road Safety CSV')

uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"], accept_multiple_files=True)

user_question= st.text_input("Enter a CSV then ask a question about it. The model will try to answer it!", "How many rows are there?")


if uploaded_file:

    #get rid of the None values in the uploaded files so there is no pd.read_csv error
    valid_files = [file for file in uploaded_file if file is not None]

    if len(valid_files) == 0:
        st.info("No files uploaded yet.")

    else:
        file_names = [file.name for file in valid_files]

        #creates a select box which displays the names of the uploaded files
        selected_file = st.selectbox(label= "Select a CSV file", options=file_names)
        #search for the selected file index
        selected_index = file_names.index(selected_file)

        st.write("File uploaded successfully!")

        data = pd.read_csv(valid_files[selected_index])
        st.write("Here's a preview of your data:")
        st.write(data.head())

        agent = create_pandas_dataframe_agent(llama_model, data, verbose=True, allow_dangerous_code=True)

        if st.button('Submit'):
            response = agent.run(user_question)
            st.write(response)