import asyncio

from mcp_server import ask_gpt


async def client():
    question = "explain about the relation between mcp and agent"
    result = await ask_gpt(None, question)
    print("answer", result)


asyncio.run(client())
