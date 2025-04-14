import json
import logging
import os

import azure.functions as func
from httpx import Client

from tools import COMPANY_OVERVIEW

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
        client (AsyncClient): The HTTP client to use for the request.
        function (str): The function to call on the API.
        symbol (str): The stock symbol to fetch data for.
        api_key (str): The API key for authentication.

    Returns:
        dict: The JSON response from the API.

    """  # noqa: E501
    # Define the parameters for the request
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
    }
    # Make the request to the API
    try:
        response = client.get(url=BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"Error": str(e)}


@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName=COMPANY_OVERVIEW.name,
    description=COMPANY_OVERVIEW.description,
    toolProperties=COMPANY_OVERVIEW.tool_properties_as_json(),
)
def get_company_overview(context) -> dict:
    """Fetch company overview data from Alpha Vantage API.

    Args:
        symbol (str): The stock symbol of the company to fetch data for.
        ctx (Context): The context object containing request information.

    Returns:
        str: The response text from the HTTP request.

    """  # noqa: E501
    logging.info("Fetching company overview")

    content = json.loads(context)
    symbol = content["arguments"]["symbol"]

    # Fetch the company overview
    result = fetcher(client, "OVERVIEW", symbol)
    logging.info("Company overview fetched successfully!")

    return result
