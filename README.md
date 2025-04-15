# AlphaVantage MCP Server with Azure Functions

This project implements an Azure Function that serves as a bridge between an Agent as a MCP Server and the AlphaVantage Financial API. 
It allows AI agents to access financial data and perform financial analysis through tools exposed via MCP. 

The Azure Function exposes the following financial data endpoints as MCP tools:
- Company Overview
- Income Statement
- Balance Sheet
- Cash Flow
- Earnings Report

## Prerequisites

- [Azure Developer CLI (azd)](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd)
- An Azure subscription
- [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- Python 3.8 or higher
- An AlphaVantage API key

## Local Development

1. Clone this repository
2. Create a virtual environment and install dependencies:
```bash
uv sync --frozen
```

3. Create a `local.settings.json` file in the `src` directory with your AlphaVantage API key:
```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "ALPHAVANTAGE_API_KEY": "your-alphavantage-api-key"
  }
}
```

4. Run the function locally:
```bash
cd src
func start
```

## Deployment

1. Log in to Azure:
```bash
azd auth login
```

2. Deploy the application:
```bash
azd up
```

This will provision the necessary Azure resources and deploy the Function App.


> **Note:** For setting up environment variables, refer to the [Adding Environment Variables](#adding-environment-variables) section.


## Getting the MCP Endpoint URL

After deployment, retrieve your MCP extension system key:

```bash
az functionapp keys list \
  --resource-group <resource_group> \ 
  --name <function_app_name>
```

Your MCP endpoint URL will be:

```
https://<funcappname>.azurewebsites.net/runtime/webhooks/mcp/sse?code=<your-mcp-extension-system-key>
```

## Adding Environment Variables

You can add environment variables to your Azure Function in two ways:

### 1. Using the parameters file (recommended for deployment)

Add your environment variables to the `infra/main.parameters.json` file:

```json
{
  "parameters": {
    // Other parameters...
    "functionAppEnvironmentVariables": {
      "value": {
        "ALPHAVANTAGE_API_KEY": "your-api-key",
        "MY_VARIABLE": "my-value"
      }
    }
  }
}
```

Then deploy with:

```
azd up
```

### 2. Using Azure CLI (for updating existing deployments)

```bash
az functionapp config appsettings set \
  --name <function_app_name> \
  --resource-group <resource-group> \
  --settings ALPHAVANTAGE_API_KEY=<your-api-key>
```

## Using with AI Agents

The `agent` directory contains an example of how to use this MCP endpoint with an AI agent using the Agno framework. You can use this as a starting point for your own financial analysis agent.

## Available Financial Tools

This project exposes the following AlphaVantage API endpoints as MCP tools:

1. **Company Overview** - Returns company information, financial ratios, and key metrics
2. **Income Statement** - Returns annual and quarterly income statements
3. **Balance Sheet** - Returns annual and quarterly balance sheets
4. **Cash Flow** - Returns annual and quarterly cash flow statements
5. **Earnings** - Returns annual and quarterly earnings data including analyst estimates

Each tool takes a stock symbol as input and returns the corresponding financial data from AlphaVantage.
