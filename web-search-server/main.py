import logging
import os

import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp.server.fastmcp import FastMCP

load_dotenv()

sk = os.getenv("OPENAI_API_KEY")
tvly = os.getenv("TAVILY_API_KEY")

os.environ["OPENAI_API_KEY"] = sk
os.environ["TAVILY_API_KEY"] = tvly

llm = ChatOpenAI(model="gpt-5")

mcp = FastMCP("WebSearch")


def search_web_tavily(query: str) -> str:
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    payload = {
        "query": query,
        "search_depth": "basic",
        "include_answers": True,
        "max_results": 5,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        results = response.json().get("results", [])

        if not results:
            return "검색 결과가 없습니다."

        contents = "\n\n".join([f"{r['title']}\n{r['content']}" for r in results])
        return contents
    except Exception as e:
        logging.error(f"Tavily 검색 오류 {e}")
        return f"검색 중 오류가 발생했습니다: {e}"


@mcp.tool()
async def search_web(query: str) -> str:
    logging.info(f"검색 요청: {query}")
    content = search_web_tavily(query)
    summary = await llm.ainvoke(f"다음 검색 결과를 한 문단으로 요약해줘:\n\n{content}")
    return summary


if __name__ == "__main__":
    mcp.run(transport="stdio")
