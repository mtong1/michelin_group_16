# parse_csv.py
#making a very basic instantiation to test out querry_llama

import pandas as pd

def parse_csv(file_path):
    #Parsing the CSV file and returning a summary as a string.
    try:
        data = pd.read_csv("")
        # Summarize the first few rows as a sample of data
        data_summary = data.head().to_string()
        return data_summary, data
    except Exception as e:  #error handle case
        print("Error reading CSV:", e)
        return None, None
#To Do: 
    # extract_keywords_from_question