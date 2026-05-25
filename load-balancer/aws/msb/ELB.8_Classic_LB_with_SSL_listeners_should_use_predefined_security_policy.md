# ELB.8 Classic Load Balancers with SSL listeners should use a predefined security policy that has strong configuration

## Overview

A security policy is a combination of SSL protocols, ciphers, and the Server Order Preference option. Predefined policies control the ciphers, protocols, and preference orders to support during SSL negotiations between a client and load balancer.

This recommendation means your Classic Load Balancer SSL/HTTPS listeners should use a modern AWS-managed SSL negotiation policy instead of weak/default cipher settings.

Weak policies may allow:

* old TLS versions (TLS 1.0 / 1.1)
* weak ciphers
* vulnerable cryptographic algorithms

Your CLB listener should use an AWS predefined policy such as: ELBSecurityPolicy-TLS13-1-2-2021-06
or at minimum: ELBSecurityPolicy-TLS-1-2-2017-01

Avoid old policies like:

* ELBSecurityPolicy-2016-08
* ELBSecurityPolicy-TLS-1-1-2017-01

especially if they permit:

* TLS 1.0
* TLS 1.1
* RC4
* 3DES

## Why this Matters

Weak SSL policies can expose systems to:

* downgrade attacks
* weak cipher exploitation
* compliance failures
* insecure legacy clients

This control is commonly checked by:

* Amazon Web Services Security Hub
* Amazon Web Services Config
* CIS AWS Benchmark
* PCI DSS
* SOC2 audits

## Remediation

1. Check existing policy

aws elb describe-load-balancer-policies \
  --load-balancer-name my-clb

or inspect listeners :

aws elb describe-load-balancers \
  --load-balancer-name my-clb

Look for:

"PolicyNames": [
  "ELBSecurityPolicy-TLS13-1-2-2021-06"
]

1. Apply a strong predefined policy

aws elb set-load-balancer-policies-of-listener \
  --load-balancer-name my-clb \
  --load-balancer-port 443 \
  --policy-names ELBSecurityPolicy-TLS13-1-2-2021-06

Terraform example:

listener {
  lb_port           = 443
  lb_protocol       = "https"
  instance_port     = 80
  instance_protocol = "http"

  ssl_certificate_id = aws_acm_certificate.example.arn
}

policy_names = [
  "ELBSecurityPolicy-TLS13-1-2-2021-06"
]

OR

More commonly with separate policy attachment:

resource "aws_load_balancer_policy" "example" {
  load_balancer_name = aws_elb.example.name
  policy_name        = "example-ssl-policy"
  policy_type_name   = "SSLNegotiationPolicyType"
}

