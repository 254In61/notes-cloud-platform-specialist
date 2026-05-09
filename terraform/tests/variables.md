
# Variables

You can provide values for Input Variables within your configuration directly from your test files.

The test file syntax supports variables blocks at both the root level and within run blocks. Terraform passes all variable values from the test file into all run blocks within the file. You can override variable values for a particular run block with values provided directly within that run block.

Adding to the test file from the example above:

# variable_precedence.tftest.hcl

variables {
  bucket_prefix = "test"
}

run "uses_root_level_value" {

  command = plan

  assert {
    condition     = aws_s3_bucket.bucket.bucket == "test-bucket"
    error_message = "S3 bucket name did not match expected"
  }

}

run "overrides_root_level_value" {

  command = plan

  variables {
    bucket_prefix = "other"
  }

  assert {
    condition     = aws_s3_bucket.bucket.bucket == "other-bucket"
    error_message = "S3 bucket name did not match expected"
  }

}

We've added a second run block that specifies the bucket_prefix variable value as other, overriding the value test that is provided by the test file and used during the first run block.

# Specify variables with the Command Line or definition files

In addition to specifying variable values via test files, the Terraform test command also supports the other typical mechanisms for specifying variable values.

You can specify values for variables across all tests with the Command line and with Variable definition files.

As with the main configuration direction, Terraform will automatically load any variables defined in the automatic variable files within a test directory. The automatic variable files are terraform.tfvars, terraform.tfvars.json, and any files that end with .auto.tfvars or .auto.tfvars.json.

Note: Variable values loaded from the automatic variable files within a test directory will only apply to tests also defined within the same test directory. Variables defined in all other ways will apply to all tests in a given test run.

This is particularly useful for using sensitive variables values and for configuring providers. Otherwise, testing files could directly expose those sensitive values.

# Variable References

Variables you define within run blocks can refer to outputs from modules executed in earlier run blocks and variables defined at higher precedence levels. 

Variables defined within the file level variables block can only refer to global variables.

For example, the following code block shows how a variable can refer to higher precedence variables and previous run blocks:

variables {
  global_value = "some value"
}

run "run_block_one" {
  variables {
    local_value = var.global_value
  }

  *# ...
  *# Some test assertions should go here.
  *# ...
}

run "run_block_two" {
  variables {
    local_value = run.run_block_one.output_one
  }

  *# ...
  *# Some test assertions should go here.
  *# ...
}

Above, the local_value in run_block_one gets its value from the global_value variable. This pattern is useful if you want to assign multiple variables the same value. You can specify a variable value once at the file level and then share it with different variables.

In comparison, local_value in run_block_two takes its value from the output value of output_one from run_block_one. This pattern is useful for passing values between run blocks, particularly if run blocks are executing different modules as detailed in the Modules section.

