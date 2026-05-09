# overview
Terraform tests let authors validate that module configuration updates do not introduce breaking changes. Tests run against test-specific, short-lived resources, preventing any risk to your existing infrastructure or state.

# Integration or Unit testing

By default, tests within Terraform create real infrastructure and can run assertions and validations against that infrastructure. This is analogous to integration testing because you are testing Terraform's core functionality by executing operations and validating the infrastructure Terraform creates.

You can override the normal testing behavior by updating the command attribute within a run block . 

By default, each run block executes with command = apply instructing Terraform to execute a complete apply operation against your configuration. Replacing the command value with command = plan instructs Terraform to not create new infrastructure for this run block. This allows test authors to validate logical operations and custom conditions within their infrastructure in a process analogous to unit testing.

Terraform v1.7.0 introduced the ability to mock data returned by the providers during a terraform test execution. This can be used to write more detailed and complete unit tests.

# Syntax

Each Terraform test lives in a test file. 

Terraform discovers test files based on their file extension: .tftest.hcl or .tftest.json.

Each test file contains the following root level attributes and blocks:

- Zero to one test blocks.
- One to many run blocks.
- Zero to one variables block.
- Zero to many provider blocks.

By default, Terraform executes run blocks sequentially.

Each run block simulates a series of Terraform commands executing directly within the configuration directory. 

The order of the variables and provider blocks doesn't matter, Terraform processes all the values within these blocks at the beginning of the test operation. 

HCP recommends defining your variables and provider blocks first, at the beginning of the test file.

# Example : 

The following example demonstrates a simple Terraform configuration that creates an AWS S3 bucket, using an input variable to modify the name. 

!! main.tf

provider "aws" {
    region = "eu-central-1"
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

We create an example test file (below) that validates the buckets name is created as expected.

The following test file runs a single Terraform plan command which creates the S3 bucket, and then validates the logic for calculating the name is correct by checking the actual name matches the expected name.

!! valid_string_concat.tftest.hcl

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

