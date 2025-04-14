import json
import logging
import os

import azure.functions as func
from httpx import Client

from tools import BALANCE_SHEET, CASH_FLOW, COMPANY_OVERVIEW, EARNINGS, INCOME_STATEMENT

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
client = Client()

# Constants
API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"


def fetcher(
    client: Client,
    function: str,
    symbol: str,
    api_key: str = API_KEY,
) -> dict:
    """Fetch data from Alpha Vantage API.

    This function constructs the URL with the provided parameters and makes an asynchronous GET request.

    Args:
        client (Client): The HTTP client to use for the request.
        function (str): The function to call on the API.
        symbol (str): The stock symbol to fetch data for.
        api_key (str): The API key for authentication.

    Returns:
        dict: The JSON response from the API.

    """
    # Define the parameters for the request
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
    }
    # Make the request to the API
    try:

        response = client.get(url=BASE_URL, params=params, timeout=10.0)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        return {"Error": str(e)}


def extract_symbol(context: str) -> tuple[str, dict]:
    """Extract symbol from context and validate it.

    Args:
        context (str): The context containing arguments.

    Returns:
        tuple[str, dict]: Symbol and error dict (if any). If error is None, symbol is valid.
    """
    try:
        content = json.loads(context)
        symbol = content["arguments"]["symbol"]

        if not symbol:
            return None, {"Error": "Missing stock symbol"}

    except (json.JSONDecodeError, KeyError) as e:
        return None, {"Error": f"Invalid context format: {str(e)}"}

    else:
        return symbol, None


@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName=COMPANY_OVERVIEW.name,
    description=COMPANY_OVERVIEW.description,
    toolProperties=COMPANY_OVERVIEW.tool_properties_as_json(),
)
def get_company_overview(context: str) -> dict:
    """Fetch company overview data from Alpha Vantage API.

    Args:
        context (str): The context string is containing the arguments for the function.

    Returns:
        dict: The JSON response from the API.

    """
    logging.info("Fetching company overview")

    symbol, error = extract_symbol(context)
    if error:
        return error

    # Fetch the company overview
    try:
        result = fetcher(client, "OVERVIEW", symbol)
        logging.info("Company overview fetched successfully!")
    except Exception as e:
        logging.exception(f"Error fetching company overview: {e}")
        result = {"Error": str(e)}

    else:
        return result


@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName=INCOME_STATEMENT.name,
    description=INCOME_STATEMENT.description,
    toolProperties=INCOME_STATEMENT.tool_properties_as_json(),
)
def get_income_statement(context: str) -> dict:
    """Fetch income statement data from Alpha Vantage API.

    Args:
        context (str): The context string is containing the arguments for the function.

    Returns:
        dict: The JSON response from the API.

    """
    logging.info("Fetching income statement")

    symbol, error = extract_symbol(context)
    if error:
        return error

    try:
        # Fetch the income statement
        result = fetcher(client, "INCOME_STATEMENT", symbol)
        logging.info("Income statement fetched successfully!")

    except Exception as e:
        logging.exception(f"Error fetching income statement: {e}")
        result = {"Error": str(e)}

    else:
        return result


@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName=BALANCE_SHEET.name,
    description=BALANCE_SHEET.description,
    toolProperties=BALANCE_SHEET.tool_properties_as_json(),
)
def get_balance_sheet(context: str) -> dict:
    """Fetch balance sheet data from Alpha Vantage API.

    Args:
        context (str): The context string is containing the arguments for the function.

    Returns:
        dict: The JSON response from the API.

    """
    logging.info("Fetching balance sheet")

    symbol, error = extract_symbol(context)
    if error:
        return error

    try:
        # Fetch the balance sheet
        result = fetcher(client, "BALANCE_SHEET", symbol)
        logging.info("Balance sheet fetched successfully!")

    except Exception as e:
        logging.exception(f"Error fetching balance sheet: {e}")
        result = {"Error": str(e)}

    else:
        return result


@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName=CASH_FLOW.name,
    description=CASH_FLOW.description,
    toolProperties=CASH_FLOW.tool_properties_as_json(),
)
def get_cash_flow(context: str) -> dict:
    """Fetch cash flow data from Alpha Vantage API.

    Args:
        context (str): The context string is containing the arguments for the function.

    Returns:
        dict: The JSON response from the API.

    """
    logging.info("Fetching cash flow")

    symbol, error = extract_symbol(context)
    if error:
        return error

    try:
        # Fetch the cash flow
        result = fetcher(client, "CASH_FLOW", symbol)
        logging.info("Cash flow fetched successfully!")

    except Exception as e:
        logging.exception(f"Error fetching cash flow: {e}")
        result = {"Error": str(e)}

    else:
        return result


@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName=EARNINGS.name,
    description=EARNINGS.description,
    toolProperties=EARNINGS.tool_properties_as_json(),
)
def get_earnings(context: str) -> dict:
    """Fetch earnings data from Alpha Vantage API.

    Args:
        context (str): The context string is containing the arguments for the function.

    Returns:
        dict: The JSON response from the API.

    """
    logging.info("Fetching earnings")

    symbol, error = extract_symbol(context)
    if error:
        return error

    try:
        # Fetch the earnings
        result = fetcher(client, "EARNINGS", symbol)
        logging.info("Earnings fetched successfully!")

    except Exception as e:
        logging.exception(f"Error fetching earnings: {e}")
        result = {"Error": str(e)}

    else:
        return result
