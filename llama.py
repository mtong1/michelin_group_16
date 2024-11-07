## MADIES WORK
# import ollama
# # from llama_index.readers.file import CSVReader
# from langchain_ollama import ChatOllama
# from langchain_core.prompts import ChatPromptTemplate

# desiredModel = 'llama3.2:1b' 
# question_to_ask = 'What is the best strategy to learn coding ?' 

# print(question_to_ask)
# response = ollama.chat(model=desiredModel, messages=[ 

#     { 
#         'role' : 'user', 
#         'content' : question_to_ask 
#     } 
# ]) 

# OllamaResponse = response['message']['content'] 
# print(OllamaResponse) 



# llm = ChatOllama(
#     model="llama3.1",
#     temperature=0,
#     # other params...
# )

# # this is where we script our prompt to query data
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a helpful assistant that translates {input_language} to {output_language}.",
#         ),
#         ("human", "{input}"),
#     ]
# )

# chain = prompt | llm
# chain.invoke(
#     {
#         "input_language": "English",
#         "output_language": "German",
#         "input": "I love programming.",
#     }
# )

# # csv_reader = CSVReader(filepath='path/to/your/file.csv')  
# # data=csv_reader.read()


import pandas as pd
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Load your CSV data using pandas
csv_file_path = "path_to_your_file.csv"
data = pd.read_csv(csv_file_path)

# Summarize or extract the necessary data from the CSV file
data_summary = data.head().to_string()  # Modify this based on your needs

# Define the chat prompt template
prompt_template = """
You are an AI model trained to analyze and provide insights from data. Here's a sample of the data:

{data}

What insights or observations can you make from this data?
"""

# Initialize ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(prompt_template)

# Set up the Ollama chat model
chat_ollama = ChatOllama(model="llama3.2:1b")  # Replace with your desired model

# Run the chat model with the data
response = chat_ollama.generate_prompt(
    prompt.format(data=data_summary)
)

# Output the response
print("Insights from the model:")
print(response)

