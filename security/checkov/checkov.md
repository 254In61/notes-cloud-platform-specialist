# Checkov by BridgeCrew
https://www.checkov.io/

Checkov is a static code analysis tool for infrastructure-as-code.

It scans cloud infrastructure provisioned using Terraform, Cloudformation, Kubernetes, Serverless or ARM Templates and detects security and compliance misconfigurations.

There are a number of default best-practice unit tests when scanning your terraform code repository will highlight deviation from best practices — such as having VM a port 22 open to the world (0.0.0.0/0) for example, evident from the security configuration.

Tests available are here : https://github.com/bridgecrewio/checkov/tree/master/tests/terraform/checks/resource/aws

# Getting it done
1. Install : $ pipx install checkov  ** Not using pip3 on an external environment..Works with a venv**

2. Initialise terraform directory : $ terraform init

3. Run checkov on that directory : $ checkov -d . 
