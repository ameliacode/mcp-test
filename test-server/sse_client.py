import asyncio
import json
import sys

from mcp import ClientSession
from mcp.client.sse import sse_client


async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py http://127.0.0.1:3000/sse")
        return

    url = sys.argv[1]
    print(f"Connecting SSE to client server...({url})")

    async with sse_client(url) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            print("Starting MCP Chat client. | 'quit' to exit")

            while True:
                user_input = input("\nQuery: ").strip()
                if user_input.lower() == "quit":
                    break
                try:
                    response = await session.call_tool("chat", {"input": user_input})
                    if isinstance(response.content, str):
                        try:
                            data = json.loads(response.content)
                            print("Response:", data["content"])
                        except json.JSONDecodeError:
                            print("Response:", response.content)
                    elif isinstance(response.content, dict):
                        print(
                            "Response:",
                            response.content.get("content", str(response.content)),
                        )
                    else:
                        print("Response:", str(response.content))
                except Exception as e:
                    print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
