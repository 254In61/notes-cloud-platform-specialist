# Terraform Standards

## shared modules

* Anything 'TF' path is shared with everyone in the company.
* Anything in 'CPT' path is for cloud platform ?
* Anything in "PC" is for Public Cloud?

## Generate and inject documentation
All Terraform core and pattern modules must include a .terraform-docs.yml file in the root of the repository. This file controls which sections are generated and where the output is written.

With mode: inject, terraform-docs will insert or update a block of generated content between two special comment markers in README.md or it will append the generated content to the end of the file if the markers are not present. The markers look like this:

<!-- BEGIN_TF_DOCS -->
[generated content is written here automatically]
<!-- END_TF_DOCS -->

Do not manually edit the content between them — it will be overwritten on the next run. To generate and inject documentation, run the following command from the root of the repository:

terraform-docs .

The .terraform-docs.yml file in the repository root is automatically discovered. The output.file setting directs the output to README.md and the mode: inject setting updates the content between the markers without affecting the rest of the file.

NOTE: If you have not yet added the <!-- BEGIN_TF_DOCS --> and <!-- END_TF_DOCS --> markers to your README.md, terraform-docs will append the generated content to the end of the file on the first run.
