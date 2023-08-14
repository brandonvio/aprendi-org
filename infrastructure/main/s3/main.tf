# This module creates an S3 bucket to store the lambda deployment package.

# create s3 bucket to store lambda zip deploymnet package
resource "aws_s3_bucket" "aprendi_lambda_functions" {
  bucket = "aprendi-lambda-functions"
}

# export the bucket arn so it can be used by other modules
output "aprendi_lambda_functions_bucket_name" {
  value = aws_s3_bucket.aprendi_lambda_functions.bucket
}
