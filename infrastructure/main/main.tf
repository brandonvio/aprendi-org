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

data "aws_caller_identity" "current" {}

module "aprendi_dns" {
  source = "./dns"
}

module "aprendi_ssl" {
  source  = "./ssl-east-1"
  zone_id = module.aprendi_dns.zone_id
}

module "aprendi_ssl_west" {
  source  = "./ssl-west-2"
  zone_id = module.aprendi_dns.zone_id
}

# import the s3 module
module "aprendi_s3" {
  source = "./s3"
}

output "aws_region" {
  value = "us-west-2"
}

# output the s3 bucket name
output "aprendi_lambda_functions_bucket_name" {
  value = module.aprendi_s3.aprendi_lambda_functions_bucket_name
}

output "east_ssl_certifcate_arn" {
  value = module.aprendi_ssl.certificate_arn
}

output "west_ssl_certifcate_arn" {
  value = module.aprendi_ssl_west.certificate_arn
}

output "zone_id" {
  value = module.aprendi_dns.zone_id
}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
