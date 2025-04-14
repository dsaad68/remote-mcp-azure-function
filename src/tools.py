from textwrap import dedent

from schema import Tool, ToolProperty

# Description of a Tool property for stock symbol
SYMBOL_TOOL_PROPERTY = ToolProperty("symbol", "string", "The stock symbol to fetch data for.")

# Description of a Tool object for Company Overview tool
COMPANY_OVERVIEW = Tool(
    name="get_company_overview",
    description=dedent("""
    This returns the company information, financial ratios, and other key metrics for the equity specified.
    Data is generally refreshed on the same day a company reports its latest earnings and financials.
    """),
    tool_properties=[SYMBOL_TOOL_PROPERTY],
)

# Description of a Tool object for Income Statement tool
INCOME_STATEMENT = Tool(
    name="get_income_statement",
    description=dedent("""
        This returns the annual and quarterly income statements for the company of interest, with normalized fields
        mapped to GAAP and IFRS taxonomies of the SEC.
        Data is generally refreshed on the same day a company reports its latest earnings and financials.
    """),
    tool_properties=[SYMBOL_TOOL_PROPERTY],
)

# Description of a Tool object for Balance Sheet tool
BALANCE_SHEET = Tool(
    name="get_balance_sheet",
    description=dedent("""
        This returns the annual and quarterly balance sheets for the company of interest, with normalized fields
        mapped to GAAP and IFRS taxonomies of the SEC.
        Data is generally refreshed on the same day a company reports its latest earnings and financials.
    """),
    tool_properties=[SYMBOL_TOOL_PROPERTY],
)

# Description of a Tool object for Cash Flow tool
CASH_FLOW = Tool(
    name="get_cash_flow",
    description=dedent("""
        This returns the annual and quarterly cash flow for the company of interest, with normalized fields
        mapped to GAAP and IFRS taxonomies of the SEC.
        Data is generally refreshed on the same day a company reports its latest earnings and financials.
    """),
    tool_properties=[SYMBOL_TOOL_PROPERTY],
)

# Description of a Tool object for Earnings tool
EARNINGS = Tool(
    name="get_earnings",
    description=dedent("""
        This returns the annual and quarterly earnings (EPS) for the company of interest.
        Quarterly data also includes analyst estimates and surprise metrics.
    """),
    tool_properties=[SYMBOL_TOOL_PROPERTY],
)
