from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
import pandas as pd
import os

# Step 1: Set up your database connection for SQL database
db = SQLDatabase.from_uri(f"sqlite:///C:/Users/pbag604/Desktop/github/database/daw.db")

# 
# Step 2: Initialize LLM (Groq)
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.0,
    max_retries=5,
    max_iterations=20,
    max_execution_time=120,
    api_key=os.environ.get("GROQ_API_KEY", "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")
)

# Step 3: Create a SQLDatabaseToolkit from the SQLDatabase
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Step 4: Create LangChain SQL Agent
agent3 = create_sql_agent(
    llm=llm,                # The Groq LLM instance
    toolkit=toolkit,        # Pass the SQLDatabaseToolkit directly
    verbose=True            # Enable verbose output for debugging
)

# Step 5: Test agent2
#response3 = agent3.invoke("What is the total revenue?")
#print(f"Agent2 Response: {response3}")
