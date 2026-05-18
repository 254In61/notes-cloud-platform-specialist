# AWS Load Balancer Components


## Listener

A Listener checks for incoming connection requests.

Example:

Protocol: HTTPS
Port: 443

The listener waits on a port and applies rules.

Example :

HTTPS:443
    |
Rule:
IF path=/api
THEN forward to API Target Group

## Listener Rules

These define routing behavior.

Example :

| Condition | Action             |
| --------- | ------------------ |
| /api/*    | API Target Group   |
| /images/* | Image Target Group |
| default   | Web Target Group   |

## Target Group

A Target Group is a collection of backend resources.

Targets can be:

* EC2 instances
* Containers
* IP addresses
* Lambda functions

## Health Checks in Target Groups

ALB periodically checks: /health

If unhealthy --> Target removed automatically.

## Internal vs Internet-Facing Load Balancers

1. Internet-Facing - Publicly accessible.

Example:

* Public website

1. Internal Load Balancer - Private only.

Used between:

* Microservices
* Internal APIs
* Backend tiers

## Cross-Zone Load Balancing

Without cross-zone:

AZ1 traffic → AZ1 targets only
AZ2 traffic → AZ2 targets only

With cross-zone: Traffic evenly distributed across all AZs.

Improves utilization.

## Sticky Sessions (Session Affinity)

Load balancer keeps user tied to same backend.

Useful for:

* Legacy apps
* Session-based authentication

But less common in modern stateless apps.

## SSL/TLS Termination

Instead of backend handling HTTPS:

* Client HTTPS → Load Balancer HTTPS
* Load Balancer HTTP → Backend

Benefits:

* Simpler backend
* Lower CPU usage
* Centralized certificate management

## Integration with AWS Services

ELB integrates with:

| Service                          | Purpose                          |
| -------------------------------- | -------------------------------- |
| Amazon Web Services Auto Scaling | Add/remove servers automatically |
| Amazon Web Services ECS          | Container routing                |
| Amazon Web Services EKS          | Kubernetes ingress               |
| Amazon Web Services WAF          | Web firewall                     |
| Amazon Web Services CloudWatch   | Metrics/logging                  |

