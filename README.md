# AlphaVantage MCP Server with Azure Functions

### Introduction 

### Prerequisites

```bash
az functionapp keys list \
  --resource-group <resource_group> \ 
  --name <function_app_name>
```


```
https://<funcappname>.azurewebsites.net/runtime/webhooks/mcp/sse?code=<your-mcp-extension-system-key>
```

```
azd up
```


```bash
az functionapp config appsettings set \
  --name <function_app_name> \
  --resource-group <resource-group> \
  --settings <MY_ENV_VAR>=<secret-value>
```

```
azd up
```