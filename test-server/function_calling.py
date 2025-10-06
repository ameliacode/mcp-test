import os

from dotenv import load_dotenv
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key


@tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@tool
def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


tools = [add, subtract]
llm = ChatOpenAI(model="gpt-5", temperature=0)
agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True
)
response = agent.invoke("subtract 7 from 3")
print("response:", response)
