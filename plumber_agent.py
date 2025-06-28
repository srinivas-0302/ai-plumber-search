# plumber_agent.py
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import langgraph
from plumber_data import get_plumbers_by_pincode

# Set your OpenAI API key (ensure you set this in your environment)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step 1: Define the prompt template
prompt = PromptTemplate(
    input_variables=["pincode"],
    template="""
You are an assistant that helps users find the best plumbers in their area based on pincode, reviews, and ratings.

Given the pincode: {pincode}, fetch the list of plumbers, sort them by rating (desc) and reviews (desc), and return the top 3 with their details.
"""
)

# Step 2: Define the function to fetch and sort plumbers
def fetch_and_sort_plumbers(pincode):
    plumbers = get_plumbers_by_pincode(pincode)
    sorted_plumbers = sorted(plumbers, key=lambda x: (-x["rating"], -x["reviews"]))
    return sorted_plumbers[:3]

# Step 3: Define the agent logic using LangChain
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

chain = LLMChain(
    llm=llm,
    prompt=prompt
)

def agent(pincode):
    # Fetch and sort plumbers
    top_plumbers = fetch_and_sort_plumbers(pincode)
    if not top_plumbers:
        return f"No plumbers found for pincode {pincode}."
    # Format the response
    response = "Top plumbers in pincode {}:\n".format(pincode)
    for idx, plumber in enumerate(top_plumbers, 1):
        response += f"{idx}. {plumber['name']} - Rating: {plumber['rating']} ({plumber['reviews']} reviews)\n"
    return response

if __name__ == "__main__":
    user_pincode = input("Enter your pincode: ")
    print(agent(user_pincode)) 