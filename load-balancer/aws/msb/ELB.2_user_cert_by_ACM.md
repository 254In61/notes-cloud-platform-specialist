# ELB.2 Classic Load Balancers with SSL/HTTPS listeners should use a certificate provided by AWS Certificate Manager

## Overview

This recommendation means your Classic Load Balancer HTTPS/SSL listeners should use certificates managed by AWS Certificate Manager (ACM) instead of older IAM-uploaded certificates.

IAM server certificates are legacy.

Using ACM certificates provides:

* automatic renewal
* centralized certificate management
* easier rotation
* improved security governance
* reduced risk of expired certificates

AWS checks whether the CLB listener certificate ARN belongs to ACM.

Good ==>  arn:aws:acm:region:account-id:certificate/xxxxxxxx
Not recommended ==> arn:aws:iam::account-id:server-certificate/example-cert

ACM certificates must exist in the same region as the load balancer.

This control commonly appears in:

* Amazon Web Services Security Hub
* Amazon Web Services Config
* CIS AWS Benchmark
* enterprise security baselines

## Remediation : Changing IAM Certificate → ACM Certificate

## Considerations

This is usually LOW RISK.

Normally NONE if:

* same domain name
* same public/private key
* same CA chain
* same SANs/wildcards

The TLS handshake still behaves the same.

Possible impacts:

1. Different certificate chain

Some old clients/devices may fail if:

* ACM uses different intermediate CA
* legacy trust stores missing CA

Rare but possible with:

* embedded systems
* old Java runtimes
* legacy Windows servers

1. Different expiration/renewal behavior

ACM auto-renews which is usually a benefit.

### Implementation Steps

1. Confirm the current IAM stored certificate used :

AWS CLI:

```bash
aws elb describe-load-balancers --load-balancer-name my-clb
```

Look for  ==> "SSLCertificateId": "arn:aws:acm:ap-southeast-2:123456789012:certificate/abcd"

If you see ==> "arn:aws:iam::123456789012:server-certificate/..." , then the load balancer is using an IAM certificate.

1. Import existing cert into ACM OR Create a new cert in ACM.

If creating a new public certificate:

```bash
aws acm request-certificate --domain-name example.com --validation-method DNS
```

1. Attach ACM Certificate to CLB

Update the listener:

Terraform Example:

listener {
  lb_port           = 443
  lb_protocol       = "https"
  instance_port     = 80
  instance_protocol = "http"
  ssl_certificate_id = aws_acm_certificate.example.arn
}

AWS CLI Example :

```bash
aws elb set-load-balancer-listener-ssl-certificate \
  --load-balancer-name my-clb \
  --load-balancer-port 443 \
  --ssl-certificate-id arn:aws:acm:ap-southeast-2:123456789012:certificate/abcd-1234
```

1. Actively monitor client perfomance.
