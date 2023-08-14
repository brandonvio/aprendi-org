provider "aws" {
  region = "us-west-2"
}

resource "aws_route53_zone" "aprendi_zone" {
  name = "aprendi.org"
}

output "zone_id" {
  value       = aws_route53_zone.aprendi_zone.zone_id
  description = "The ID of the hosted zone"
}

output "name_servers" {
  value       = aws_route53_zone.aprendi_zone.name_servers
  description = "The name servers for the hosted zone"
}

