# REF
https://developer.hashicorp.com/terraform/language/validate

# Validate your configuration

Validation helps you verify that your Terraform configuration works as you intend. Using different types of validation you can:

- Verify input variables meet specific requirements.
- Prevent incorrect outputs from writing to your state.
- Ensure resources and data sources are configured correctly after Terraform applies them.
- Verify the broader behavior of your infrastructure.
- Document assumptions about your infrastructure.
- Use HCP Terraform to regularly verify your infrastructure.

When a validation fails, Terraform provides context that you can use in your error messages to help users understand and fix their issue. 

Terraform evaluates different ways of validation at different stages of Terraform's execution cycle, and they can either block further operation execution or continue execution with warnings.

For authors, adding validation to your configuration enforces your module's standards and requirements, helping module consumers understand and use your configuration.

Validating your configuration is flexible, and you can often use different kinds of validation to achieve the same result. 

When choosing a way of validating, consider whether or not you want the validation to block your operations, and during which phase of the Terraform workflow it should run.



# Terraform offers several ways of validating configuration:

1. Input variable validations : verify your configuration's parameters when Terraform creates a plan.

2. Preconditions: ensure individual resources, data sources, and outputs meet your requirements before Terraform tries to create them.

3. Postconditions: verifies that Terraform produced your resources and data sources with the expected and desired settings.

4. Checks:  let you validate that your resources work as expected without blocking Terraform operations based on the check's result.

# Continuous validation in HCP Terraform
If you enable health checks on a workspace, HCP Terraform continuously validates any check blocks, preconditions, and postconditions in your workspace's configuration to regularly verify your infrastructure. 

For example, you can use a check block to continuously monitor the validity of an API gateway certificate. Continuous validation alerts you when the condition fails, so you can update the certificate and avoid errors the next time you want to update your infrastructure.

