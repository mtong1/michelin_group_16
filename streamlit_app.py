import streamlit as st
from parse_csv import parse_csv
from query_llama import initialize_llama_model, query_llama_for_visualization
from visualization import generate_visualization
import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)

st.title("Data Query Tool")

# File uploader in Streamlit to select a CSV file
uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file:
    # Step 1: Parse the CSV
    parsed_data, data_df = parse_csv(uploaded_file)

    if parsed_data:
        # Step 2: Initialize the Llama model
        model = initialize_llama_model()

        # Step 3: User can enter a question and generate visualization type suggestion
        user_question = st.text_input("Ask a question about the data:")
        if st.button("Submit") and user_question:
            visualization_type = query_llama_for_visualization(parsed_data, model)
            #Outputting type suggestion onto Streamlit to make it easier to see what model is thinking
            #Can always get rid of later
            st.write(f"Suggested Visualization Type: {visualization_type}")

            # Step 4: Generate and display the visualization
            st.write("Generating Visualization...")
            generate_visualization(data_df, visualization_type)
        else:
            st.warning("Please enter a question to proceed.")
    else:
        st.error("Could not parse the CSV file. Please check the format.")

