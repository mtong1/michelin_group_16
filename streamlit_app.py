import streamlit as st
import pandas as pd
from langchain_ollama import ChatOllama
from langchain_experimental.agents import create_pandas_dataframe_agent

llama_model = ChatOllama(model="llama3.2", temperature=1)

st.title('Road Safety CSV')

uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"], accept_multiple_files=True)
user_context = st.text_input("Provide some context for the uploaded CSV(s)", placeholder="E.g., This dataset contains accident statistics for 2023...")
user_question= st.text_input("Enter Question", placeholder="What is the average speed of vehicles involved in accidents?")

if uploaded_file:

    #get rid of the None values in the uploaded files so there is no pd.read_csv error
    valid_files = [file for file in uploaded_file if file is not None]

    if len(valid_files) == 0:
        st.info("No files uploaded yet.")

    else:
        file_names = [file.name for file in valid_files]

        #creates a select box which displays the names of the uploaded files
        selected_file = st.sidebar.selectbox(label= "Select a CSV file", options=file_names)
        #search for the selected file index
        selected_index = file_names.index(selected_file)

        data = pd.read_csv(valid_files[selected_index])
        st.write("Here's a preview of your data:")
        st.write(data.head())

        #make sure user provides context
        if not user_context:
            st.warning("Please provide context for the CSV dataset.")
        #make sure user provides a question
        elif not user_question:
            st.warning("Please enter a question to ask about the CSV dataset.")
        else:
            dataset_info = f"The dataset has {data.shape[0]} rows and {data.shape[1]} columns. " \
            f"Columns include: {', '.join(data.columns)}. Here is the user-provided context about this CSV: {user_context}"

            full_prompt = f"""
            The dataset has {data.shape[0]} rows and {data.shape[1]} columns.
            Columns include: {', '.join(data.columns)}.

            Context: {user_context}

            Using the context, answer the question: {user_question}. You do not need to ouput any code unless specified, only output the answer.
            Format the answer as plain text.
            """

            agent = create_pandas_dataframe_agent(
                llm = llama_model,
                df = data,
                allow_dangerous_code=True,
                max_iterations=100,
                max_execution_time=100,
                verbose= True,
                agent_executor_kwargs=dict(handle_parsing_errors=True)
                )
            response_section = st.container()

            if st.button('Submit'):
                with response_section:
                    processing_placeholder = st.empty()  # placeholder to show the processing message
                    processing_placeholder.write("Processing your request...")
                    try:
                        #using run instead of invoking gets better results
                        response = agent.run(full_prompt)
                        #make the processing your request message disappear
                        processing_placeholder.empty()
                        st.write("Response:")
                        st.success(response)
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")