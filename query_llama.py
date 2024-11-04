#query_llama.py
#Built to replace modelSetUp.py

from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate

#To Do: 
    # extract_keywords_from_question 
        #- need keyword_prompt to pass to model
        #- Format prompt
        #toString --> list --> .split(",")

def initialize_llama_model(model_name="llama3.2:latest"):
    #Initializing the Llama model using Ollama.
    return Ollama(model=model_name)

def query_llama_for_visualization(parsed_data, model):
    #Sending the parsed data to the Llama model
    #determine visualization type
    prompt_template = """
    You are an AI that analyzes geospatial data and recommends visualizations. Here is a data summary:

    {data}

    Based on the data, what type of visualization would best represent this information? Suggest either a map, bar chart, or scatter plot.
    """
    # Using ChatPromptTemplate to format the prompt
    prompt = ChatPromptTemplate.from_template(prompt_template)
    
    # Formating the prompt with the data
    formatted_prompt = prompt.format(data=parsed_data)
    
    # formatted prompt --> model
    response = model(formatted_prompt)
    
    # Extracting the response text and interpret it as a visualization type
    visualization_type = response.strip().lower()
    return visualization_type
