import asyncio
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools


async def run_agent(message: str) -> None:
    """Run the financial anlysis agent with the given message."""

    async with MCPTools("") as mcp_tools:
        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            tools=[mcp_tools],
            instructions=dedent("""\
            You are a financial analysis agent.

            Analyze a company's income statement, balance sheet, cash flow, and earnings.
            Generate a concise report summarizing the company's financial overview.
            """),
            markdown=True,
            planning=True,
            show_tool_calls=True,
        )

        # Run the agent
        await agent.aprint_response(message, stream=True)


# Example usage
if __name__ == "__main__":
    # Basic example - exploring project license
    asyncio.run(run_agent("What is the license for this project?"))
