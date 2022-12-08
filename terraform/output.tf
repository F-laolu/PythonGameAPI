output "cosmos_key" {
value = azurerm_cosmosdb_account.dbacc.primary_key
sensitive = true 
}

output "instrumentation_key" {
  value = azurerm_application_insights.appins.instrumentation_key
  sensitive = true
}

output "app_id" {
  value = azurerm_application_insights.appins.app_id
}

output "connection_string" {
  value = azurerm_application_insights.appins.connection_string
  sensitive = true
}