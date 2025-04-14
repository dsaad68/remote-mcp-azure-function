from textwrap import dedent

from schema import Tool, ToolProperty

# Create a Tool object for Company Overview tool
COMPANY_OVERVIEW = Tool(
    name="get_company_overview",
    description=dedent("""
    This returns the company information, financial ratios, and other key metrics for the equity specified.
    Data is generally refreshed on the same day a company reports its latest earnings and financials.
    """),
    tool_properties=[ToolProperty("symbol", "string", "The stock symbol to fetch data for.")],
)
