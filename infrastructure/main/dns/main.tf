provider "aws" {
  region = "us-west-2"
}

variable "root_domain" {
  description = "The root domain for the hosted zone"
  type        = string
}

resource "aws_route53_zone" "root_zone" {
  name = var.root_domain
}

output "zone_id" {
  value       = aws_route53_zone.root_zone.zone_id
  description = "The ID of the hosted zone"
}

output "name_servers" {
  value       = aws_route53_zone.root_zone.name_servers
  description = "The name servers for the hosted zone"
}

