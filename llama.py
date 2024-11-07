import ollama
# from llama_index.readers.file import CSVReader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

desiredModel = 'llama3.2:1b' 
question_to_ask = 'What is the best strategy to learn coding ?' 

print(question_to_ask)
response = ollama.chat(model=desiredModel, messages=[ 

    { 
        'role' : 'user', 
        'content' : question_to_ask 
    } 
]) 

OllamaResponse = response['message']['content'] 
print(OllamaResponse) 



llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    # other params...
)

# this is where we script our prompt to query data
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)

# csv_reader = CSVReader(filepath='path/to/your/file.csv')  
# data=csv_reader.read()
