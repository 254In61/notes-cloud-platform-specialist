# REF
- #1 : https://auth0.com/blog/what-is-caching-and-how-it-works/

# definitions
- Cache : A cache is a software or hardware component aimed at storing data so that future requests for the same data can be served faster.

- Caching: The process of storing and accessing data from a cache.

# overview
- Data is usually stored on the data storage layers which is persistent memory.
- Application accessing the data in these layers can take a long time to access this data from the persisten memory.

- So, when data is retrieved or processed, it should be stored in a more efficient memory. This memory is the cache, which can be thought of as a high-speed data storage layer, whose priamry purpose is to reduce the need to access slower data storage layer.

- Cache are usually implemented by using fast access hardware such as RAM(Random-Access Memory) plus a software component.

- Thanks to caches, it is possible to implement a mechanism to efficiently reuse previously retrieved or computed data. Whenever a new request arrives, the requested data is searched first in a cache. A "cache hit" occurs when the requested data can be found in a cache. On the contrary, a "cache miss" occurs when it cannot. Obviously, reading the required data from caches is assumed to be faster than recomputing the result or reading it from the original data store. So, the more requests can be served from a cache, the faster the system will be.

# Why Caching is important.

Neither users nor developers want applications to take a long time to process requests.

The truth is that no one loves wasting their time looking at loading messages and one could easily loose customers if App/Web Page is that slow.The importance of offering high performance is so critical that caching has rapidly become an unavoidable concept in computer technology. 

As a consequence, if we want to compete with the multitude of applications on the market, we are required to properly implement caching systems.

Caching allows us to avoid making new requests or reprocessing data every time.

1. We get to avoid overhead and reduce CPU usage, especially if requests involve complex elaborations. 
   This can prolong the life of machines and servers.
  
2. By voiding making new requests reduces the overall amount of requests needed, which may decrease the cost of your infrastructure. 

# Challenges

Caching is by no means a simple practice, and there are inevitable challenges inherent in the subject.

Coherence Problem
==================

Since whenever data is cached, a copy is created, there are now two copies of the same data. This means that they can diverge over time. 

This is the coherence problem, which represents the most important and complex issue related to caching. There is not a particular solution that is preferred over another, and the best approach depends on the requirements. 

Identifying the best cache update or invalidation mechanism is one of the biggest challenges related to caching and perhaps one of the hardest challenges in computer science.

Choosing Data to Be Cached
==========================

- Virtually any kind of data can be cached. This means that choosing what should reside in our cache and what to exclude is open to endless possibilities. Thus, it may become a very complex decision.

- If we expect data to change often, we should not want to cache it for too long. Otherwise, we may offer users inaccurate data. This depends on how much time we can tolerate stale data.

- Cache should always be ready to store frequently required data taking a large amount of time to be generated or retrieved. Identifying this data is not an easy task, and you might risk filling our cache with useless data.

- By caching large data, you may fill your cache very rapidly, or worse, using all available memory. If your RAM is shared between your application and your caching system, this can easily become a problem, which is why you should limit the amount of your RAM reserved for caching.

Dealing with Cache-misses
==========================

Cache misses represent the time-based cost of having a cache. 

In fact, cache misses introducing latencies that would not have been incurred in a system not using caching. 

So, to benefit from the speed boost deriving from having a cache, cache misses must be kept relatively lows. In particular, they should be low compared to cache hits. 

Reaching this result is not easy, and if not achieved, our caching system can turn into nothing more than overhead.

# Types of Caching

Although caching is a general concept, there a few types that stand out from the rest. They represent key concepts for any developers interested in understanding the most common approaches to caching, and they cannot be omitted. Let’s see them all.

In-memory Caching
=================

In this approach, cached data is stored directly in RAM, which is assumed to be faster than the typical storing system where the original data is located. 

The most common implementation of this type of caching is based on "key-value" databases. 

Essentially, this means that each piece of data is identified by a unique value. By specifying this value, the key-value database will return the associated value. Such a solution is fast, efficient, and easy to understand. 

This is why it is usually the preferred approach by developers that are trying to build a caching layer.

Database Caching
=================

Each database usually comes with some level of caching. 

Specifically, an internal cache is generally used to avoid querying a database excessively. By caching the result of the last queries executed, the database can provide the data previously cached immediately. 

This way, for the period of time that the desired cached data is valid, the database can avoid executing queries. 

Although each database can implement this differently, the most popular approach is based on using a hash table storing key-value pairs. Just like seen before, the key is used to look up the value. 

Note that such type of cache is generally provided by default by ORM (Object Relational Mapping) technologies.


Web Caching
============

This can be divided into two further subcategories:

1. Web Client Caching

This type of cache is familiar to most Internet users, and it is stored on clients. 

Since it is usually part of browsers, it is also called Web Browser Caching. 

It works in a very intuitive way. The first time a browser loads a web page, it stores the page resources, such as text, images, stylesheets, scripts, and media files. The next time the same page is hit, the browser can look in the cache for resources that were previously cached and retrieve them from the user’s machine. 

This is generally way faster than download them from the network.

2. Web Server Caching

This is a mechanism aimed at storing resources server-side for reuse. 

Specifically, such an approach is helpful when dealing with dynamically generated content, which takes time to be created.

Conversely, it is not useful in the case of static content. Web server caching avoids servers from getting overloaded, reducing the work to be done, and improves the page delivery speed.

3. CDN Caching

CDN stands for Content Delivery Network, and it is aimed at caching content, such as web pages, stylesheets, scripts, and media files, in proxy servers. 

It can be seen as a system of gateways between the user and the origin server, storing its resources. When the user requires a resource, a proxy server intercepts it and checks to see if it has a copy. If so, the resource is immediately delivered to the user; otherwise, the request is forwarded to the origin server. 

These proxy servers are placed in a vast number of locations worldwide, and user requests are dynamically routed to the nearest one. 

Thus, they are expected to be closer to end-users than origin servers, which implies a reduction in network latency. Plus, it also reduces the number of requests made to origin servers.