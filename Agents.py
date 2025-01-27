from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_groq import ChatGroq
import pandas as pd
from sqlalchemy import create_engine
import os

# Initialize LLM (Groq)
llm = ChatGroq(
    model ="llama3-8b-8192",
    temperature=0.0,
    max_retries=2,
    api_key=os.environ.get("GROQ_API_KEY", "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")

    #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
)
#... Vector Database


# Step 1: Load CSV into a Pandas DataFrame
# Step 1: Load CSV into a Pandas DataFrame
# Option 1: Use a raw string
csv_file = r"C:\Users\pbag604\Desktop\github\Database\rev.csv"
df = pd.read_csv(csv_file, low_memory=False)

# Step 2: Store DataFrame into SQLite
engine = create_engine("sqlite:///rev_mnth.db")
table_name = "rev"
df.to_sql(table_name, con=engine, if_exists="replace", index=False)

# Step 3: Query the table and load the result into a pandas DataFrame
query = "SELECT * FROM rev"
df_query_result = pd.read_sql(query, con=engine)

# Step 4: Display the queried data
print("Queried DataFrame:")
print(df_query_result)

# Step 5: Create LangChain Agents
agent1 = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True
)

agent2 = create_pandas_dataframe_agent(
    llm,
    df_query_result,
    verbose=True,
    allow_dangerous_code=True,
    handle_parsing_errors=True
)

# Step 6: Test Agents
#response1 = agent1.invoke("How many product is there")
#response2 = agent2.invoke("what is the meta data")

#print(f"Agent1 Response: {response1}")
#print(f"Agent2 Response: {response2}")
