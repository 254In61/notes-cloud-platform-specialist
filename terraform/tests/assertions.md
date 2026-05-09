# Assertions

Assertion arguments in Terraform run blocks help you validate your configuration. Each assert block contains a condition argument and an error_message argument.

At the conclusion of a Terraform test command execution, Terraform presents any failed assertions as part of a tests passed or failed status.

Assertion References
=====================

Assertions within tests can reference any existing named values that are available within the main Terraform configuration.

Additionally, test assertions can directly reference outputs from current and previous run blocks. For example, this is a valid condition: condition = output.bucket_name == "test_bucket".