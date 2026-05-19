from datetime import datetime, timezone

from fastmcp import FastMCP

mcp = FastMCP("everything-server")

@mcp.tool()
def now() -> str:
    """Return the current UTC time in ISO-8601 format."""
    return datetime.now(timezone.utc).isoformat()

@mcp.tool()
def reverse(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


if __name__ == "__main__":
    mcp.run()
