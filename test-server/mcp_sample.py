import asyncio
import logging

from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


if __name__ == "__main__":
    asyncio.run(mcp.run(transport="stdio"))
