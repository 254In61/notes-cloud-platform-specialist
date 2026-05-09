# overview - How does an LB choose the backend server to forward traffic to?

A load balancing algorithm is the logic that a load balancer uses to distribute network traffic between servers (an algorithm is a set of predefined rules).

There are two primary approaches to load balancing. 

- Dynamic load balancing : uses algorithms that take into account the current state of each server and distribute traffic accordingly. 

- Static load balancing :  distributes traffic without making these adjustments. Some static algorithms send an equal amount of traffic to each server in a group, either in a specified order or at random.


# Dynamic load balancing algorithms

1. Least connection: 
- Checks which servers have the fewest connections open at the time and sends traffic to those servers. 
- This assumes all connections require roughly equal processing power.

2. Weighted least connection: 
- Gives administrators the ability to assign different weights to each server, assuming that some servers can handle more connections than others.

3. Weighted response time: 
- Averages the response time of each server, and combines that with the number of connections each server has open to determine where to send traffic. 
- By sending traffic to the servers with the quickest response time, the algorithm ensures faster service for users.

4. Resource-based: 
- Distributes load based on what resources each server has available at the time. 
- Specialized software (called an "agent") running on each server measures that server's available CPU and memory, and the load balancer queries the agent before distributing traffic to that server.

# Static load balancing algorithms

1. Round robin: 

- Round robin load balancing distributes traffic to a list of servers in rotation using the Domain Name System (DNS).
- An authoritative nameserver will have a list of different A records for a domain and provides a different one in response to each DNS query.


2. Weighted round robin: 

- Allows an administrator to assign different weights to each server. 
- Servers deemed able to handle more traffic will receive slightly more. Weighting can be configured within DNS records.

3. IP hash: 

- Combines incoming traffic's source and destination IP addresses and uses a mathematical function to convert it into a hash. 
- Based on the hash, the connection is assigned to a specific server.