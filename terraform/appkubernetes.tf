resource "azurerm_kubernetes_cluster" "example" {
  name                = var.kub
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  dns_prefix          = "olakscluster3"


  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_a2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }

}
