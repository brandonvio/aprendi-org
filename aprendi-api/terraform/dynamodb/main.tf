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

resource "aws_dynamodb_table" "aprendi_org_table" {
  name         = "aprendi_org_table"
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
    Name = "aprendi_org_table"
  }
}

output "dynamodb_table_arn" {
  value = aws_dynamodb_table.aprendi_org_table.arn
}
