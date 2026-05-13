# Simple Queue Service

## SQS

It is a fully managed message queue service provided by Amazon Web Services.

At a high level:

* One application sends messages into a queue.
* Another application reads and processes them later.
* The queue acts like a buffer between systems.

## What SQS actually does

SQS provides:

1. Message buffering

It temporarily stores messages until consumers process them.

Example:

* E-commerce checkout sends “Create Order”
* Queue stores the request
* Order service processes it when ready

1. Decoupling services

Applications no longer depend on each other being immediately available.

Example:

* API service sends image-processing jobs
* Image processor can be offline temporarily
* Messages wait safely in SQS

This improves:

* reliability
* scalability
* fault tolerance

1. Asynchronous processing

Some work should be independent of the user request.

Example:

sending emails
generating PDFs
video processing
notifications
audit logging

Instead of making the user wait:

User Request -> Queue Job -> Background Worker Processes Later

1. Traffic spike handling - load leveling.

Imagine:

* normal load = 100 requests/min
* sudden spike = 50,000 requests/min

Without a queue , backend crashes

With SQS:

* messages pile up safely
* workers process gradually

## Common AWS architecture using SQS

Very common pattern:

API Gateway
    ↓
Lambda / App
    ↓
SQS Queue
    ↓
Workers / Lambda Consumers
    ↓
Database / External Systems

Used heavily with:

* Amazon Web Services Lambda
* ECS
* EC2
* microservices
* event-driven systems

## Types of SQS queues

1. Standard Queue

Best for:

* maximum throughput
* speed
* scalability

Characteristics:

* messages may arrive out of order
* duplicates are possible

Use cases:

* logs
* analytics
* background jobs
* FIFO Queue

FIFO = First In First Out

Characteristics:

strict ordering
no duplicate processing

Use cases:

* payment processing
* financial systems
* inventory management

## Key SQS concepts

1. Producer : Application sending messages.

Example:

* API
* web app
* Lambda

1. Consumer : Application reading messages.

Example:

* worker service
* Lambda function

1. Visibility Timeout

* When a consumer reads a message: SQS hides it temporarily
* If processing succeeds: message deleted
* If consumer crashes: message becomes visible again. This prevents message loss.

## Dead Letter Queue (DLQ)

Failed messages go here after repeated failures.

Useful for:

* debugging
* poison messages
* retries
