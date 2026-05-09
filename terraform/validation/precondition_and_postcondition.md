# Preconditions

Use precondition blocks when you want to verify your configuration's assumptions for resources, data sources, and outputs before Terraform creates them.

Terraform evaluates preconditions on resources, data sources, and outputs when Terraform creates a plan. 

Preconditions take precedence over any argument errors raised by providers on incorrectly configured resources, data sources, and outputs.

The following example uses a precondition to verify that the AMI configured for anaws_instance uses the x86_64 CPU architecture.

resource "aws_instance" "example" {
  instance_type = "t3.micro"
  ami           = data.aws_ami.example.id

  lifecycle {
    # The AMI ID must refer to an AMI that contains an operating system
    # for the `x86_64` architecture.
    precondition {
      condition     = data.aws_ami.example.architecture == "x86_64"
      error_message = "The selected AMI must be for the x86_64 architecture."
    }
  }
}

The precondition detects if the caller accidentally selected an AMI for a different architecture, which may not be able to run the software this instance hosts. Terraform evaluates the precondition while it builds its plan, and if the precondition fails Terraform throws an error with the error_message argument and stops the current operation. 

An output block can also include a precondition to verify a module's output. Use preconditions on outputs to validate that your output values meets your requirements before Terraform exposes them or stores their values in state.

For example, you can use a precondition to ensure a server's security group has at least one ingress rule to allow traffic on ports 80 or 443:

output "instance_public_ip" {
  value = aws_instance.web.public_ip

  precondition {
    condition     = length([for rule in aws_security_group.web.ingress : rule if rule.to_port == 80 || rule.to_port == 443]) > 0
    error_message = "Security group must allow HTTP (port 80) or HTTPS (port 443) traffic."
  }
}

Use preconditions for assumptions that you want to verify before Terraform creates the target block. For example, you may want to verify that the AMI selected for an aws_instance has x86_64 CPU architecture before trying to create the instance. 

Using preconditions for assumptions helps future maintainers understand the values a resource, output, or data source should allow.

# Postconditions

Terraform evaluates postcondition blocks after planning and applying changes to a resource, or after reading from a data source.

For example, you can use a postcondition to detect if a user accidentally provided an AMI intended for the wrong system component.

data "aws_ami" "example" {
  executable_users = ["self"]
  most_recent      = true
  owners           = ["self"]

  filter {
    name   = "name"
    values = ["myami-*"]
  }

  lifecycle {
    # The AMI ID must refer to an existing AMI that has the tag "nomad-server".
    postcondition {
      condition     = self.tags["Component"] == "nomad-server"
      error_message = "tags[\"Component\"] must be \"nomad-server\"."
    }
  }
}

Unless the component has the "nomad-server" tag, the postcondition fails, which prevents using the incorrect AMI to provision a server. If the postcondition fails, Terraform throws an error with the error_message argument and stops the current operation.

Adding postconditions can prevent cascading changes to other dependent resources.

Postconditions can serve as static guardrails to enforce mandatory configuration aspects on your data and resource blocks. 

Use postconditions for guarantees that you need to verify after Terraform creates the resource or reads from the data source. For example, you may want to ensure that an aws_instance is launched in a network that assigns it a private DNS record. 

Use postconditions for guarantees to help future maintainers understand which behaviors they must preserve when changing configuration.