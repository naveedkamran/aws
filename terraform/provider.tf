
# provider.tf

# Specify the provider and access details
provider "aws" {
  shared_credentials_file = "keys/public.pub"
  profile                 = "default"
  region                  = var.aws_region
}
