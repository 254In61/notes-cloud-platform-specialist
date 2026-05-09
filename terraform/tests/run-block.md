# Run blocks

Each run block has the following fields and blocks:

1. command : An optional attribute, which is either apply or plan. Default = apply

2. plan_options.mode :	An optional attribute, which is either normal or refresh-only.	Default = normal

3. plan_options.refresh: An optional boolean attribute.	Default = true

4. plan_options.replace: An optional attribute containing a list of resource addresses referencing resources within the configuration under test.

5. plan_options.target	: An optional attribute containing a list of resource addresses referencing resources within the configuration under test.	

6. variables:	An optional variables block.

7. module: 	An optional module block.

8. providers: An optional providers attribute.

9. assert: Optional assert blocks.

10. expect_failures: An optional attribute.	

11. state_key:	An optional attribute.

12. parallel:	An optional boolean attribute.


# Example

!! with_config.tftest.hcl

test {
  parallel = true
}

variables {
  bucket_prefix = "test"
}

run "first" {
  assert {
    condition     = aws_s3_bucket.bucket.bucket == "test-bucket"
    error_message = "S3 bucket name did not match expected"
  }
}

run "second" {
  assert {
    condition     = aws_s3_bucket.bucket.bucket == "test-bucket"
    error_message = "S3 bucket name did not match expected"
  }
}

run "third" {
  parallel = false
  assert {
    condition     = aws_s3_bucket.bucket.bucket == "test-bucket"
    error_message = "S3 bucket name did not match expected"
  }
}

In the above example, the first and second run blocks implicitly have parallel set to true since the test block enables parallel runs. 
The third run block sets parallel to false to override the global setting.

