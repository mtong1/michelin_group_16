import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import getpass
import os
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI

# if "GROQ_API_KEY" not in os.environ:
#     os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

st.title('🦜🔗 Quickstart App')

groq_api_key = st.sidebar.text_input('Groq API Key')
openai_api_key = st.sidebar.text_input('openai API Key')

def generate_response(input_text):
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
        llm = ChatGroq(
            model="llama-3.1-70b-versatile",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2
        )
        # Call the model and display the result
        response = llm([HumanMessage(content=input_text)])
        # print (type(response))
        st.info((response.content))
        st.info(type(response))

    else:
        st.warning('Please enter your Groq API key!', icon='⚠')

def csv_agent():
    os.environ["OPENAI_API_KEY"] = openai_api_key
    agent = create_csv_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613" ),
    "data/Crash data_LA_county.csv",
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    allow_dangerous_code=True
)
    response = agent.run("how many rows and columns")
    st.info(response)


with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if submitted:
    generate_response(text)
    csv_agent()
#   if not groq_api_key.startswith(''):
#     st.warning('Please enter your Groq API key!', icon='⚠')
#   if submitted and groq_api_key.startswith('sk-'):
    # generate_response(text)


