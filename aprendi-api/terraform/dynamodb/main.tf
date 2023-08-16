# Terraform module for creating a DynamoDB table for the Course Enrollment service.
provider "aws" {
  region = "us-west-2"
}

terraform {
  backend "s3" {
    bucket         = "aprendi-org-terraform-state"
    key            = "infrastructure/api/table/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "aprendi_terraform_locks"
    encrypt        = true
  }
}

resource "aws_dynamodb_table" "aprendi_organization_table" {
  name         = "aprendi_organization_table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "pk"
  range_key    = "sk"

  attribute {
    name = "pk"
    type = "S"
  }

  attribute {
    name = "sk"
    type = "S"
  }

  tags = {
    Name = "aprendi_organization_table"
    Env  = "dev"
  }
}

resource "aws_dynamodb_table" "aprendi_organization_data_table" {
  name         = "aprendi_organization_data_table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "pk"
  range_key    = "sk"

  attribute {
    name = "pk"
    type = "S"
  }

  attribute {
    name = "sk"
    type = "S"
  }

  attribute {
    name = "lsi_sk1"
    type = "S"
  }

  attribute {
    name = "lsi_sk2"
    type = "S"
  }

  local_secondary_index {
    name      = "local_secondary_index1"
    range_key = "lsi_sk1"

    projection_type = "ALL"
  }

  local_secondary_index {
    name      = "local_secondary_index2"
    range_key = "lsi_sk2"

    projection_type = "ALL"
  }

  tags = {
    Name = "aprendi_organization_data_table"
    Env  = "dev"
  }
}
