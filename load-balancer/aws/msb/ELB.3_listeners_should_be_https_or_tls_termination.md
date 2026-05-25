# ELB.3 Classic Load Balancer listeners should be configured with HTTPS or TLS termination

## Overview

For a Classic Load Balancer (CLB) in AWS, listeners should terminate encrypted traffic using:

* HTTPS (for HTTP applications)
* SSL / TLS (for TCP applications)

This ensures traffic between clients and the load balancer is encrypted.
Usually because:

* HTTP listeners expose plaintext traffic
* TCP listeners on 443 without SSL termination bypass TLS inspection

The following Listener patterns are secure :

1. HTTPS Traffic termination :

* HTTPS:443 → HTTP:80
* HTTPS:443 → HTTPS:443

1. TCP Applications :

* SSL:443 → TCP:443 for TCP Applications

These Listener patterns are insecure:

* HTTP:80 → HTTP:80
* TCP:443 → TCP:443

This requirement commonly appears in:

* Amazon Web Services Config
* Amazon Web Services Security Hub
* CIS AWS Foundations Benchmark
* PCI-DSS controls

## Remediation : Changing HTTP → HTTPS or TCP → SSL

NB : Being a client/user-centric issue, there's no common automation toolkit built that cuts across everyone.

### Considerations

This is a behavioural protocol change.

Clients must now:

* use TLS
* trust the certificate
* negotiate supported ciphers/TLS versions.
* possibly use a different port.

If applications aren't changed to communicate over the secure protocols before changing on the Load Balancer :

* They will fail unless updated.
* Health checks may fail.
* Integrations may break.

### Implementation Steps

1. Update client applications to use the secure protocols.

This might involve :

* Updating the code base.
* Updating the API design.

1. create a new secure listener on the AWS ELB

Terraform Example:

listener {
  lb_port           = 443
  lb_protocol       = "https"
  instance_port     = 80
  instance_protocol = "http"
  ssl_certificate_id = aws_acm_certificate.example.arn
}

AWS CLI - HTTPS Example:

```bash
aws elb create-load-balancer-listeners \
  --load-balancer-name my-clb \
  --listeners Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80,SSLCertificateId=arn:aws:acm:ap-southeast-2:123456789012:certificate/abcd-1234
```

AWS CLI - SSL Example:

```bash
aws elb create-load-balancer-listeners \
  --load-balancer-name my-clb \
  --listeners Protocol=SSL,LoadBalancerPort=8443,InstanceProtocol=TCP,InstancePort=443,SSLCertificateId=arn:aws:acm:ap-southeast-2:123456789012:certificate/abcd-1234
```

1. Test traffic flow with a section of users to the new Listener using the new secure port.

* redirect traffic
* update DNS/App configs

1. Update clients gradually to utilize the new secure ports and protocols as you monitor the perfomance.

1. Remove the old listener from the load balancer (optional).
