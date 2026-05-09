# Order of validation

Terraform validates different aspects of your configuration as early as it can. 

Generally, Terraform executes evaluations in the following order:

1. Terraform executes input variable validations immediately, before generating a plan.
2. Terraform executes preconditions after generating a plan but before creating the resource, data source, or output.
3. Terraform executes postconditions after planning and applying changes.
4. Terraform executes checks at the end of plan and apply operations and every time health assessments run on a workspace in HCP Terraform.

The precise order that Terraform executes check blocks, preconditions, and postconditions can depend on whether Terraform has information about a condition's value before or after applying your configuration. 

- If the relevant value is available BEFORE an apply operation, then Terraform performs the validation during the planning phase. For example, if Terraform has access to a resource's image ID during planning, it can execute any validations that rely on that ID.

- If Terraform only knows the value AFTER applying, then Terraform delays checking that validation until the apply phase. For example, AWS assigns the root volume ID when it starts an EC2 instance, so Terraform cannot reference the root volume ID until the apply is complete.

During the apply phase, a failed precondition prevents Terraform from implementing planned actions for the associated resource, data source, or output. 

A failed postcondition halts processing and prevents further downstream actions that rely on the resource or data source, but does not undo any actions Terraform has already taken.
