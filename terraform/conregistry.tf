resource "azurerm_container_registry" "acr" {
  name                = var.conreg
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = false

} 

resource "azurerm_role_assignment" "role1" {
  principal_id                     = azurerm_kubernetes_cluster.example.identity.0.principal_id
  role_definition_name             = "AcrPull"
  scope                            = azurerm_container_registry.acr.id
  skip_service_principal_aad_check = true
}