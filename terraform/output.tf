output "cosmos_key" {
value = azurerm_cosmosdb_account.dbacc.primary_key
sensitive = true 
}