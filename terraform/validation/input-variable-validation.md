
Input variable validation
===========================

Use input variable validation to perform the following tasks:

- Verify input variables meet specific format requirements.
- Verify input values fall within acceptable ranges.
- Prevent Terraform operations if a variable is misconfigured.

For example, you can validate whether a variable value has valid AMI ID syntax.

variable "image_id" {
  type        = string
  description = "The id of the machine image (AMI) to use for the server."

  validation {
    condition     = length(var.image_id) > 4 && substr(var.image_id, 0, 4) == "ami-"
    error_message = "The image_id value must be a valid AMI id, starting with \"ami-\"."
  }
}

If you set the value of the image_id variable to a string without AMI ID syntax, the condition evaluates to false. 

When a variable validation fails, Terraform errors, displays the configured error_message, and stops the operation from proceeding. 

While provider APIs often error on these same validations, this helps your users avoid the error and issues a helpful error message. You can also use these validations to enforce your organization's design decisions, such as naming conventions.


