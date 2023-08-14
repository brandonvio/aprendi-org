# main.tf
# This template create 
provider "aws" {
  region = "us-west-2"
}

terraform {
  backend "s3" {
    bucket         = "aprendi-org-terraform-state"
    key            = "infrastructure/app/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "aprendi_terraform_locks"
    encrypt        = true
  }
}

data "terraform_remote_state" "main" {
  backend = "s3"
  config = {
    bucket = "aprendi-org-terraform-state"
    key    = "infrastructure/terraform.tfstate"
    region = "us-west-2"
  }
}

module "aprendi_website_bucket" {
  source = "./website-bucket"
}

module "aprendi_cloudfront" {
  source                     = "./cloudfront"
  website_bucket_id          = module.aprendi_website_bucket.website_bucket_id
  website_bucket_domain_name = module.aprendi_website_bucket.website_bucket_domain_name
  ssl_certificate_arn        = data.terraform_remote_state.main.outputs.east_ssl_certifcate_arn
  aws_region                 = data.terraform_remote_state.main.outputs.aws_region
  zone_id                    = data.terraform_remote_state.main.outputs.zone_id
  depends_on                 = [module.aprendi_website_bucket]
}
