# Load Balancer Basics

## What's LB?

A Load Balancer is a system that distributes incoming network traffic across multiple servers or services.

Instead of users connecting directly to a single server: User -> Server.

They connect to a load balancer first:  User → Load Balancer → Multiple Servers

The load balancer decides which backend server should handle each request.

Why do we need a load balancer? :

* High Availability/Fault Tolerance : Multiple servers serving users. Even if one goes down, traffic is still served by other backend servers.
* Scalability : Ability to scale, since one can deal with different servers in the backend and users won't feel the impact.
* Better perfomance : No server is overloaded leading to slow perfomance. Load is distributed across different backend servers.

Think of a restaurant.
=> If customers are to make direct orders to the kitchen , the kitchen staff will be overwhelemed.
=> Having the person taking orders in between the customer, and then distributes the orders in the backend depending on which chef has capacity, that's a more efficient way.

                Internet
                    |
             +--------------+
             | Load Balancer|
             +--------------+
              /     |      \
             /      |       \
         Server1 Server2 Server3

The load balancer receives all requests and forwards them intelligently.

## Types of Load Balancing - Based on OSI layers

| Type                  | Layer       | Traffic Type |
| --------------------- | ----------- | ------------ |
| Layer 4 Load Balancer | Transport   | TCP/UDP      |
| Layer 7 Load Balancer | Application | HTTP/HTTPS   |

## Layer 4 - Transport Layer

Works with:

* IP
* TCP
* UDP

Makes decisions based on:

* Source IP
* Destination IP
* Port

Fast and efficient.

Example: Forward TCP port 443 traffic.

## Layer 7 (Application Layer)

Understands:

* URLs
* Headers
* Cookies
* HTTP methods

Can do advanced routing:

* /api → API servers
* /images → Image servers

Smarter but slightly heavier.

## Common Load Balancing Algorithms

1. Round Robin

Requests distributed sequentially.

Req1 → Server1
Req2 → Server2
Req3 → Server3

1. Least Connections

Send traffic to server with fewest active connections.

Good for uneven workloads.

1. Weighted Routing

More powerful servers receive more traffic.

Example:

Server1 = Weight 70
Server2 = Weight 30

1. IP Hash

Same client IP always goes to same backend.

Useful for sticky sessions.

## Health Checks

Load balancers continuously check if backend servers are healthy.

Example:

GET /health

If server fails:

* It is removed from rotation
* Traffic stops going there

This is critical for high availability.

## Active vs Passive Load Balancing

| Type           | Description                            |
| -------------- | -------------------------------------- |
| Active-Active  | All servers serve traffic              |
| Active-Passive | Backup server used only during failure |

## On-Prem vs Cloud Load Balancers

Traditional Appliances. These are Hardware-based.

Examples:

* F5 Networks BIG-IP
* Citrix ADC

Cloud Load Balancers i.e managed by cloud providers.

Examples:

* Amazon Web Services Elastic Load Balancing
* Microsoft Azure Load Balancer
