# Minimum Security Baseline

## Classic Load Balancer listeners should be configured with HTTPS or TLS termination

A listener defines:

* protocol
* port
* how traffic enters the load balancer.

Bad example :  HTTP : 80
Good examles : HTTPS : 443 OR TLS:443

Without encryption:

Client ---- plain text ----> Load Balancer

Attackers can:

* sniff passwords
* steal session cookies
* read sensitive data

With HTTPS/TLS:

Client ==== encrypted ==== > Load Balancer

The load balancer decrypts HTTPS traffic :

Client HTTPS
      |
      v
Classic Load Balancer
(SSL/TLS termination)
      |
HTTP or HTTPS
      |
Backend EC2

With TLS Termination on the Load Balancer, the following benefits are realized : 

1. Traffic is encrypted in transit.

Encryption in transit protects :

* Credentials
* APIs
* tokens
* personal data.

1. Centralized certificate management .

   Instead of certificates on every EC2 instance , install once on CLB.

1. Reduced backend CPU usage

   TLS encryption is CPU intensive. CLB handles it instead of application servers.

AWS recommends use of :

* HTTPS listeners and avoiding of plain HTTP only.
* TLS listeners

Example Listener Configuration :

| Frontend  | Backend |
| --------- | ------- |
| HTTPS:443 | HTTP:80 |

OR

| Frontend  | Backend   |
| --------- | --------- |
| HTTPS:443 | HTTPS:443 |

## Classic Load Balancers should have connection draining enabled

Connection draining allows in-flight requests to finish before removing a backend instance.

Without draining, EC2 backend is terminated immediately

Users may see:

* failed uploads
* broken sessions
* HTTP 500 errors

With Connection Draining

Flow:

Instance marked unhealthy  >> CLB stops NEW connections >> Existing requests finish >> Instance removed safely.

Common use cases :

* Auto Scaling : When instances scale in.
* Deployments : Rolling deployments when removing old server gracefully.
* Maintenance : Draining avoids abrupt disconnections.

## Classic Load Balancers with SSL listeners should use a predefined security policy that has strong configuration

What Is an SSL Security Policy?

Defines:

* TLS versions
* ciphers
* cryptographic algorithms

AWS provides managed policies like: ELBSecurityPolicy-TLS-1-2-2017-01

These enforce:

* strong encryption
* secure ciphers
* modern TLS

Recommended Modern Settings

Use:

* TLS 1.2+
* Forward secrecy ciphers
* Strong encryption suites

Avoid:

* SSLv2
* SSLv3
* TLS 1.0
* weak RC4 ciphers

