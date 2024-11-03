import ollama
import ollama 

  #use a prompt template every time querry
#can llama take in the csv string and understand it?
#figure out how to geospatially visualize data in python 

desiredModel = 'llama3.2' 

  

question_to_ask = 'What intersection is them most dangerous in LA ?' 

  

response = ollama.chat(model=desiredModel, messages=[ 

    { 

        'role' : 'user', 

        'content' : question_to_ask 

    } 

]) 

  

OllamaResponse = response['message']['content'] 

  

print(OllamaResponse) 
#use llama to give you exactly what to search for in the csv
#writes functions to look for
#parse llama input into panda searchable 
#clear response schema
#how to chain our prompt with the input 
#ask llama to tell us which version of fucntion would work best for prompt
#tell llama exact format of data all context, 