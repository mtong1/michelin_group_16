import pandas as pd
import streamlit as st
from query_llama import query_llama_with_dataframe, query_llama_with_sql
from parse_csv import extract_csv_context, extract_csv_metadata
from langchain_ollama import ChatOllama
from langchain_experimental.agents import create_pandas_dataframe_agent


def pad_prompt(df, user_question: str, user_context:str  ):
    full_prompt = f"""
            The dataset has {df.shape[0]} rows and {df.shape[1]} columns.
            Columns include: {', '.join(df.columns)}.

            Context: {user_context}

            Using the context, answer the question: {user_question}. You do not need to ouput any code unless specified, only output the answer.
            Format the answer as plain text.
            """
    return full_prompt

llama_model = ChatOllama(model="llama3.2", temperature=1)

st.title('Road Safety CSV')

uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"], accept_multiple_files=True)
user_context = st.text_area("Provide some context for the uploaded CSV(s)", placeholder="E.g., This dataset contains accident statistics for 2023...")
user_question= st.text_area("Enter Question", placeholder="What is the average speed of vehicles involved in accidents?")

if uploaded_file:

    #get rid of the None values in the uploaded files so there is no pd.read_csv error
    valid_files = [file for file in uploaded_file if file is not None]

    if len(valid_files) == 0:
        st.info("No files uploaded yet.")


# Remember to update to include these imports
# Switch to SQLDatabaseChain to avoid REPL issues?
# less dynamic
from visualization import (
    create_bar_chart,
    create_scatter_plot,
    create_histogram,
    create_box_plot,
)

# title
st.title("CSV Analysis and Visualization Tool")

# CSV upload here 
uploaded_files = st.sidebar.file_uploader("Upload your CSV files", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    try:
        # Read uploaded files into DataFrames
        dataframes = {file.name: pd.read_csv(file) for file in uploaded_files}
    except Exception as e:
        st.error(f"Error loading files: {e}")
        st.stop()

    # For file select
    file_options = ["All Files"] + list(dataframes.keys())
    selected_option = st.selectbox("Select a file for analysis:", file_options)

    if selected_option == "All Files":
        try:
            combined_df = pd.concat(dataframes.values(), ignore_index=True)  # Combine dataframes from the multiple CSVs
            st.write("### Combined Data Preview")
            st.write(combined_df.head())

            metadata = extract_csv_metadata(combined_df)  # Extract metadata (look to parse_csv)
            st.write("### Data Summary: Combined Metadata")
            st.write(metadata)

            #user_query = st.text_input("What would you like to know about the data?")
#             if user_query:
#                 # Future: Need to get rid of all of this bc unrealistic to expect user to actuallu say they want a SQL querry
#                 if "SQL" in user_query:  # Example SQL prompter
#                     response = query_llama_with_sql(user_query, combined_df)
#                 else:
#                     response = query_llama_with_dataframe(user_query, combined_df)
#                 st.write("### Query Result")
#                 st.write(response)
        except Exception as e:
            st.error(f"Error processing combined data: {e}")
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

            full_prompt = pad_prompt(data, user_question, user_context)
#         try:
#             selected_df = dataframes[selected_option]
#             st.write(f"### File Preview: {selected_option}")
#             st.write(selected_df.head())

#             metadata = extract_csv_metadata(selected_df)  # Extract metadata
#             st.write("### File Metadata")
#             st.write(metadata)

#             user_query = st.text_input(f"What do you want to know about {selected_option}?")
#             if user_query:
#                 # Future: Need to get rid of all of this bc unrealistic to expect user to actuallu say they want a SQL querry
#                 # This is the same issue as above
#                 # Would it be fixed with SQLDatabaseChain?
#                 if "SQL" in user_query:  # Example trigger for SQL-specific queries
#                     response = query_llama_with_sql(user_query, selected_df)
#                 else:
#                     response = query_llama_with_dataframe(user_query, selected_df)
#                 st.write("### Query Result")
#                 st.write(response)
#         except Exception as e:
#             st.error(f"Error processing selected file: {e}")

else:
    st.info("Please upload your CSV file(s) to proceed.")


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