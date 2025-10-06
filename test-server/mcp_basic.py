from fastmcp import FastMCP

mcp = FastMCP("add")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b


if __name__ == "__main__":
    mcp.run()
