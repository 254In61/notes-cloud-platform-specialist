# aws lb ssl cert

## SSL Certificate ID

The ssl_certificate_id tells the load balancer: “Which SSL/TLS certificate should I use for HTTPS connections?”
It is used when the ELB is handling HTTPS or SSL traffic.

Think of ELB as a receptionist : Client ---> Reception desk ---> Backend servers

If visitors speak securely (HTTPS):

* receptionist needs ID badge + encryption keys
* that's the SSL certificate

ssl_certificate_id tells AWS: "Use THIS certificate for secure conversations."

The certificate is attached to the frontend listener (lb_port), not the backend instance.
This is because the ELB is acting as an HTTPS server to the client.

lb_protocol = "HTTPS"

requires : ssl_certificate_id = ...

## What the Certificate Does

When a browser connects: https://example.com

the ELB must:

* Present a certificate
* Prove it owns the domain
* Negotiate encryption keys
* Establish secure TLS communication

The certificate contains:

* domain name
* public key
* issuer (CA)
* expiration

Example:

CN = api.example.com
Issuer = Amazon RSA 2048 M02

## Where AWS Stores It

Classic ELB supports:

* ACM certificates
* IAM server certificates

Most modern setups use: AWS Certificate Manager (ACM)

Terraform example:

resource "aws_acm_certificate" "app" {
  domain_name       = "example.com"
  validation_method = "DNS"
}

Then:

ssl_certificate_id = aws_acm_certificate.app.arn

## Example 

listener {
  lb_port            = 443
  lb_protocol        = "HTTPS"

  instance_port      = 8080
  instance_protocol  = "HTTP"

  ssl_certificate_id = aws_acm_certificate.app.arn
}

This means:

Client
   |
   | HTTPS request
   |
   v
ELB uses certificate to:

* prove identity
* encrypt traffic
* establish TLS session
   |
   v
Forward to backend

Without a certificate, HTTPS cannot work.
