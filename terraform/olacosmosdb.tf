resource "azurerm_cosmosdb_account" "dbacc" {
  name                = "olacosmosdbacc2"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  offer_type          = "Standard"

  geo_location {
    location          = azurerm_resource_group.rg.location
    failover_priority = 0
  }

  consistency_policy {
    consistency_level       = "Session"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

}

resource "azurerm_cosmosdb_sql_database" "db" {
  name                = "GameDetails1"
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.dbacc.name
}

resource "azurerm_cosmosdb_sql_container" "dbcon" {
  name                  = "GameScores1"
  resource_group_name   = azurerm_resource_group.rg.name
  account_name          = azurerm_cosmosdb_account.dbacc.name
  database_name         = azurerm_cosmosdb_sql_database.db.name
  partition_key_path    = "/definition/id"
  partition_key_version = 1
  throughput            = 400

  indexing_policy {
    indexing_mode = "consistent"

    included_path {
      path = "/*"
    }

    included_path {
      path = "/included/?"
    }

    excluded_path {
      path = "/excluded/?"
    }
  }

  unique_key {
    paths = ["/definition/idlong", "/definition/idshort"]
  }
}