import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp.server.fastmcp import Context, FastMCP

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

mcp = FastMCP("GPT-5 MCP")


@mcp.tool()
async def ask_gpt(ctx: Context, question: str) -> str:
    llm = ChatOpenAI(model="gpt-5", temperature=0.3)
    return llm.predict(question)


if __name__ == "__main__":
    mcp.run(transport="stdio")
