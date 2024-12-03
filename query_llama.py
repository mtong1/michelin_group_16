#query_llama.py
#Built to replace modelSetUp.py

from langchain_experimental.agents import create_pandas_dataframe_agent
#agent documentation link: https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent.html
from langchain_ollama import ChatOllama
from sqlalchemy import create_engine
import pandas as pd

# Creating a Pandas agent
#  Querying the DataFrame LLaMA
# Future: Adjust temperature?
def create_pandas_agent(df):
    llama_model = ChatOllama(model="llama3.2", temperature=0)
    return create_pandas_dataframe_agent(llama_model, df, verbose=True)

# Converts a DataFrame into a temporary SQLite database
# Necessary bc you can't preform querries on pandas dataframe
    #Future: Check?
def create_temp_sql_db(dataframe):
    engine = create_engine("sqlite:///:memory:")
    dataframe.to_sql("temp_table", engine, index=False, if_exists="replace")
    return engine

# For the natural language SQL queries 
def query_llama_with_sql(input_query, dataframe):
    try:
        engine = create_temp_sql_db(dataframe)  # Convert DataFrame to SQLite DB
        llama_model = ChatOllama(model="llama3.2", temperature=0)
        sql_query = llama_model.chat(input_query)["query"]  # Generate SQL query
        with engine.connect() as connection:
            result = connection.execute(sql_query).fetchall()  # Execute query
        return result
    except Exception as e:
        raise ValueError(f"Error querying SQL database: {e}")

# Queries the dataframe with a Pandas agent
def query_llama_with_dataframe(query, df):
    try:
        agent = create_pandas_agent(df)  # Creating the agent
        # Running query
        response = agent.run(query)  
        return response
    except Exception as e:
        raise ValueError(f"Error querying DataFrame: {e}")
