# overview
You can set or override the required providers within the main configuration from your testing files by using provider and providers blocks and attributes.

At the root level of a Terraform testing file, you can define provider blocks as if Terraform were creating them within the main configuration. Terraform will then pass these provider blocks into its configuration as each run block executes.

By default, each provider you specify is directly available within each run block. You can customize the availability of providers within a given run block by using a providers attribute. The behavior and syntax for this block match the behavior of providers meta-argument.

If you do not provide provider configuration within a testing file, Terraform attempts to initialize any providers within its configuration using the provider's default settings. For example, any environment variables aimed at configuring providers are still available, and Terraform can use them to create default providers.

Below, we expand on our previous example to allow tests, instead of the configuration, to specify the region. In this example, we are going to test the following configuration file:

!! main.tf

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

variable "bucket_prefix" {
  type = string
}

resource "aws_s3_bucket" "bucket" {
  bucket = "${var.bucket_prefix}-bucket"
}

output "bucket_name" {
  value = aws_s3_bucket.bucket.bucket
}


!! customised_provider.tftest.hcl

provider "aws" {
    region = "eu-central-1"
}

variables {
  bucket_prefix = "test"
}

run "valid_string_concat" {

  command = plan

  assert {
    condition     = aws_s3_bucket.bucket.bucket == "test-bucket"
    error_message = "S3 bucket name did not match expected"
  }

}


We can also create a more complex example configuration, that makes use of multiple providers and aliases:

REF: https://developer.hashicorp.com/terraform/language/tests

