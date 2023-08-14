# This module creates an S3 bucket to store the lambda deployment package.

variable "root_name" {
  description = "The root name for the system"
  type        = string
}

# create s3 bucket to store lambda zip deploymnet package
resource "aws_s3_bucket" "builds_bucket" {
  bucket = "${var.root_name}-builds"
}

# export the bucket arn so it can be used by other modules
output "builds_bucket_name" {
  value = aws_s3_bucket.builds_bucket.bucket
}
