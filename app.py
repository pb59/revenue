import streamlit as st
from Agents import agent1, agent2
from SQL_agent import agent3

# Streamlit UI
st.title("DAW Revenue Data Analysis with AgentsAI")

# Input fields for query and agent selection
query = st.text_input("Enter your query:")
agent_choice = st.radio("Choose an agent:", ["Agent1", "Agent2", "Agent3"])

# Button to trigger query execution
if st.button("Run Query"):
    if query.strip():
        # Execute query directly with the selected agent
        if agent_choice == "Agent1":
            response = agent1.run(query)  # Assuming agent1 has a `run` method
        elif agent_choice == "Agent2":
            response = agent2.run(query)  # Assuming agent2 has a `run` method
        elif agent_choice == "Agent3":
            response = agent3.run(query)  # Assuming agent3 has a `run` method
        else:
            response = "Invalid agent selection."
        
        # Display the response
        st.success(f"Response: {response}")
    else:
        st.error("Please enter a query.")
