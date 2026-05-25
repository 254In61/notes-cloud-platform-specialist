# AWS Elastic Load Balancing (ELB)

ELB automatically:

* Distributes traffic
* Scales automatically
* Performs health checks
* Integrates with AWS services

## AWS Load Balancer Types

AWS provides 4 main load balancers.

1. Layer 7 Load Balancer

Understands HTTP/HTTPS.

Best for:

* Web applications
* APIs
* Microservices
* Container workloads

Internet
    |
[Application Load Balancer]
    |
+-----------+-----------+
|                       |
Target Group A     Target Group B
|                       |
EC2/API Pods        EC2/Web Pods

Features include :

* Path-based routing : /api → API target group  , /images → Image target group
* Host-based routing : app.example.com → App servers , api.example.com → API servers.
* WebSocket support.
* SSL termination : ALB handles HTTPS certificates.

1. Network Load Balancer (NLB) - Layer 4 Load Balancer

NLB Flow : 

Client
   |
[NLB]
   |
TCP Traffic
   |
Backend Servers

Very fast and low latency.

Handles:

* TCP
* UDP
* TLS

Best for:

* Gaming
* Financial systems
* High-performance apps

Key Features :

* Millions of requests/sec
* Static IP support
* Preserves client IP
* Ultra low latency

1. Gateway Load Balancer (GWLB)

Used for:

* Firewalls
* Security appliances
* Packet inspection

Common with:

* Palo Alto Networks
* Fortinet
* Check Point Software Technologies

Purpose : Allows transparent insertion of network appliances into traffic flow.

1. Classic Load Balancer (CLB) - Legacy load balancer.

Supports:

* Layer 4
* Basic Layer 7

Mostly replaced by:

* ALB
* NLB

Avoid for new deployments.
