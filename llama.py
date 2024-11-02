import ollama

desiredModel = 'llama3.2:1b'

question_to_ask = 'What is the best strategy to learn coding ?'


response = ollama.chat(model=desiredModel, messages=[
    {
        'role' : 'user',
        'content' : question_to_ask
    }
])



OllamaResponse = response['message']['content']



print(OllamaResponse)