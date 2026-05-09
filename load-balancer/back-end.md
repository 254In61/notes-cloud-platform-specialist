# Backend Server Health Monitoring 

Load balancers continuously monitor backend servers to ensure that requests are only sent to healthy servers. This helps maintain application availability and performance.

1. Active Health Checks / Heartbeat Monitoring

Ensures servers are online and responding before sending traffic to them.

The load balancer periodically sends test requests (like HTTP, TCP, or ICMP pings) to servers to verify they are online and responding correctly.

Heartbeat signals are lightweight messages sent at regular intervals to confirm server availability. If a heartbeat fails multiple times, the server is considered unhealthy.

2. Passive Health Checks
Detects failing servers by monitoring real user traffic.

The load balancer monitors real client traffic for errors or timeouts.
If a server consistently fails to respond or returns errors, it is marked as down automatically without waiting for active tests.

# Automatic Failover and Recovery
Prevents downtime by rerouting traffic away from unhealthy servers.

When a server is detected as down, the load balancer immediately stops sending traffic to it, preventing failed requests from reaching clients.

Once the server recovers and passes health checks or heartbeat monitoring, it is automatically reinstated into the pool.

This ensures seamless failover with minimal disruption to end users.

# How does the load balancer choose the backend server? - Load balancing algorithm

A load balancing algorithm is the logic that a load balancer uses to distribute network traffic between servers (an algorithm is a set of predefined rules).

There are two primary approaches to load balancing. 

- Dynamic load balancing : uses algorithms that take into account the current state of each server and distribute traffic accordingly. 

- Static load balancing :  distributes traffic without making these adjustments. Some static algorithms send an equal amount of traffic to each server in a group, either in a specified order or at random.

# How do load balancers handle state?

Some applications require that a user continues to connect to the same backend server. 

A Source algorithm creates an affinity based on client IP information. 

Another way to achieve this at the web application level is through sticky sessions, where the load balancer sets a cookie and all of the requests from that session are directed to the same physical server.

