
# Checks

Use the check block to validate your infrastructure outside of the typical resource lifecycle.

The check block executes as the last step of plan or apply operation, after Terraform has planned or provisioned your infrastructure. 

When a check block's assertion fails, Terraform reports a warning and continues executing the current operation.

Use check blocks to complete the following tasks:

- Validate resources, data sources, variables, or outputs in your configuration.
- Validate the behavior of your infrastructure as a whole.
- Verify infrastructure configuration without blocking operations.
- Perform continuous validation in HCP Terraform.

The following example uses a check block to verify the Terraform website is healthy.

check "health_check" {
  data "http" "terraform_io" {
    url = "https://www.terraform.io"
  }

  assert {
    condition = data.http.terraform_io.status_code == 200
    error_message = "${data.http.terraform_io.url} returned an unhealthy status code"
  }
}

If the website's endpoint returns a 200 status code, then the website is healthy and the check passes. 

Unlike other ways of validating your configuration, check blocks do not block operations. If the assertion evaluates to false, Terraform throws a warning that includes the result of the error_message expression and continues the operation.

