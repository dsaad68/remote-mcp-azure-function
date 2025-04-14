  (✓) Done: Resource group: rg-func-test (1.733s)
  (✓) Done: App Service plan: plan-oxtj4exki5eyi (3.675s)
  (✓) Done: Log Analytics workspace: log-oxtj4exki5eyi (17.385s)
  (✓) Done: Storage account: stoxtj4exki5eyi (22.377s)
  (✓) Done: Application Insights: appi-oxtj4exki5eyi (2.305s)
  (✓) Done: Function App: func-api-oxtj4exki5eyi (24.936s)


az functionapp keys list --resource-group <resource_group> --name <function_app_name>

az functionapp keys list --resource-group rg-another-test --name func-api-x75zo5xfj3kng


https://<funcappname>.azurewebsites.net/runtime/webhooks/mcp/sse?code=<your-mcp-extension-system-key>


https://func-api-x75zo5xfj3kng.azurewebsites.net/runtime/webhooks/mcp/sse?code=<your-mcp-extension-system-key>
