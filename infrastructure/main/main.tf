provider "aws" {
  region = "us-west-2"
}

terraform {
  backend "s3" {
    bucket         = "aprendi-org-terraform-state"
    key            = "infrastructure/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "aprendi_terraform_locks"
    encrypt        = true
  }
}

locals {
  root_name   = "aprendi"
  root_domain = "aprendi.org"
}

data "aws_caller_identity" "current" {}

module "dns" {
  source      = "./dns"
  root_domain = local.root_domain
}

module "ssl_east1" {
  source      = "./ssl-east-1"
  zone_id     = module.dns.zone_id
  root_domain = local.root_domain
}

module "ssl_west2" {
  source      = "./ssl-west-2"
  zone_id     = module.dns.zone_id
  root_domain = local.root_domain
}

# import the s3 module
module "s3" {
  source    = "./s3"
  root_name = local.root_name
}

output "aws_region" {
  value = "us-west-2"
}

# output the s3 bucket name
output "builds_bucket_name" {
  value = module.s3.builds_bucket_name
}

output "ssl_east_certifcate_arn" {
  value = module.ssl_east1.certificate_arn
}

output "ssl_west_certifcate_arn" {
  value = module.ssl_west2.certificate_arn
}

output "zone_id" {
  value = module.dns.zone_id
}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
