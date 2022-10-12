# Configure the Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.23.0"
  
    }
  }

  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
}

resource "azurerm_resource_group" "rg" {
  name     = var.rgname
  location = "UK West"
}

#backend
terraform {
  backend "azurerm" {
    resource_group_name  = "gameapicontainer"
    storage_account_name = "olaterraformstore"
    container_name       = "olastateterraform"
    key                  = "terraform.tfstate"
    access_key = "__storagekey__"
  }
}
