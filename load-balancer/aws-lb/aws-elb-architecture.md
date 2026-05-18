# AWS ELB Architecture

## Full AWS ALB Architecture

                    Internet
                        |
                 Route53 DNS
                        |
                 AWS WAF (optional)
                        |
               Application Load Balancer
                    Listener :443
                        |
         +--------------+--------------+
         |                             |
     Rule:/api                    Rule:/web
         |                             |
    Target Group API             Target Group WEB
         |                             |
   ECS / EC2 / EKS               ECS / EC2 / EKS

## Typical Modern AWS Architecture

Users
   |
CloudFront CDN
   |
AWS WAF
   |
Application Load Balancer
   |
Microservices (ECS/EKS)
   |
Databases

## ALB vs NLB summary - Making Architectural designs

| Feature          | ALB           | NLB             |
| ---------------- | ------------- | --------------- |
| Layer            | 7             | 4               |
| HTTP/HTTPS aware | Yes           | No              |
| TCP/UDP          | Limited       | Excellent       |
| Path routing     | Yes           | No              |
| WebSockets       | Yes           | Limited         |
| Performance      | High          | Extremely High  |
| Static IP        | No            | Yes             |
| Best For         | Web apps/APIs | High throughput |

Use ALB when:

* Building APIs
* Running web apps
* Using containers
* Need smart routing

Use NLB when:

* Need ultra-low latency
* TCP/UDP workloads
* Static IPs required
* Financial/gaming workloads.

## Example AWS Deployment Scenario - E- Commerce Platform

ALB routes requests based on URL paths.

Users
  |
CloudFront
  |
ALB
  |
+-------------------+
| /api  → API ECS   |
| /img  → Image ECS |
| /pay  → Payment   |
+-------------------+

## High Availability Design

AWS best practice:

ALB across multiple Availability Zones

Example:

AZ1 → EC2-1
AZ2 → EC2-2
AZ3 → EC2-3

If one AZ fails:

Traffic continues automatically.

## Best-Practice Architecture

Internet Users
        |
Encrypted HTTPS/TLS
        |
Classic Load Balancer

* TLS termination
* Strong security policy
* Connection draining enabled
        |
Backend EC2 Instances
