import pandas as pd
import streamlit as st
from query_llama import query_llama_with_dataframe, query_llama_with_sql
from parse_csv import extract_csv_context, extract_csv_metadata

# Remember to update to include these imports
# Switch to SQLDatabaseChain to avoid REPL issues?
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

            user_query = st.text_input("What would you like to know about the data?")
            if user_query:
                # Future: Need to get rid of all of this bc unrealistic to expect user to actuallu say they want a SQL querry
                if "SQL" in user_query:  # Example SQL prompter
                    response = query_llama_with_sql(user_query, combined_df)
                else:
                    response = query_llama_with_dataframe(user_query, combined_df)
                st.write("### Query Result")
                st.write(response)
        except Exception as e:
            st.error(f"Error processing combined data: {e}")
    else:
        try:
            selected_df = dataframes[selected_option]
            st.write(f"### File Preview: {selected_option}")
            st.write(selected_df.head())

            metadata = extract_csv_metadata(selected_df)  # Extract metadata
            st.write("### File Metadata")
            st.write(metadata)

            user_query = st.text_input(f"What do you want to know about {selected_option}?")
            if user_query:
                # Future: Need to get rid of all of this bc unrealistic to expect user to actuallu say they want a SQL querry
                # This is the same issue as above
                # Would it be fixed with SQLDatabaseChain?
                if "SQL" in user_query:  # Example trigger for SQL-specific queries
                    response = query_llama_with_sql(user_query, selected_df)
                else:
                    response = query_llama_with_dataframe(user_query, selected_df)
                st.write("### Query Result")
                st.write(response)
        except Exception as e:
            st.error(f"Error processing selected file: {e}")

else:
    st.info("Please upload your CSV file(s) to proceed.")




