# message-queue

## old setup

Frontend/API ---> Backend Service ---> Database/External API

If the backend becomes slow or unavailable:

* requests fail
* users see errors
* traffic spikes can crash services

## Message Queues - System Design

Message queues enable asynchronous communication between system components by acting as a buffer between producers and consumers.

They decouple services, allowing each component to operate independently and reliably even during delays or failures.

* Improves scalability and load handling by distributing work across consumers.
* Enhances fault tolerance by storing messages until they are processed.

A message queue decouples the systems:

Frontend/API ---> Msg Queue ---> Worker/Consumer ---> Database/API

Now:

* the frontend only needs to place a message into the queue
* workers process messages asynchronously
* spikes are absorbed safely

Think of message queue: like restaurant order tickets.

Without message queue:

Customer → Chef directly

If 100 customers arrive:

* chef overwhelmed
* orders lost

With message queue:

Customer → Order Queue → Chefs process one by one

Benefits:

* no lost orders
* kitchen handles bursts
* multiple chefs can work in parallel

## Example

Imagine an online shop.

When order placed:

Instead of:

Create order -> Charge card -> Send email -> Update inventory -> Generate invoice -> Notify shipping

all during one request…

You do:

Create order -> Push events/jobs to SQS -> Return success to user

Then workers asynchronously:

* send email
* update stock
* create invoice
* notify warehouse

Faster and more reliable.

## Message Structure

A typical message structure consists of two main parts:

1. Headers: These contain metadata about the message, such as unique identifier, timestamp, message type, and routing information.

1. Body: The body contains the actual message payload or content. It can be in any format, including text, binary data, or structured data like JSON.

## Message Components

A message queue system consists of different components that work together to send, store, and process messages asynchronously.

1. Message Producer: Messages are created and sent to the message queue by the message producer. Any program or part of a system that produces data for sharing can be considered this.

1. Message Queue: Until the message consumers consume them, the messages are stored and managed by a data structure or service called the message queue. It serves as a mediator or buffer between consumers and producers.

1. Message Consumer: Messages in the message queue must be retrieved and processed by the message consumer. Messages from the queue can be read concurrently by several users.

1. Message Broker (Optional): In some message queue systems, a message broker acts as an intermediary between producers and consumers, providing additional functionality like message routing, filtering, and message transformation.

## How message queues work

Step 1: Sending Messages: The message producer creates a message and sends it to the message queue. The message typically contains data or instructions that need to be processed or communicated.

Step 2: Queuing Messages: The message queue stores the message temporarily, making available for one or more consumers. Messages are typically stored in a first-in, first out (FIFO) order.

Step 3: Consuming Messages: Message consumers retrieve messages from the queue when they are ready to process them. They can do this at their own pace, which enables asynchronous communication.

Step 4: Acknowledgment (Optional): In some message queue systems, consumers can send acknowledgments back to the queue, indicating that they have successfully processed a message. This is essential for ensuring message delivery and preventing message loss.

## Importance

Message Queues are needed to address a number of challenges in distributed systems, including:

* Asynchronous Communication: Applications can send and receive messages without waiting for a response due to message queues. Building scalable and dependable systems requires this.

* Decoupling: Message queues decouple applications from each other, allowing them to be developed independently. This makes systems more flexible and easier to maintain.

* Scalability: Message queues can be scaled to handle large volumes of messages by adding more servers. This makes them ideal for high-traffic applications.

* Reliability: Message queues can be designed to be highly reliable, with features such as message persistence, retries, and dead letter queues. This ensures that messages are not lost even in the event of failures.

* Workflow Management: Message queues can be used to implement complex workflows, such as order processing and payment processing. This can help improve the efficiency and accuracy of these processes.

## Two main types of message queues in system design

1. Point-to-Point Message Queues

Point-to-point message queues store messages sent by a producer until a consumer retrieves them.

Once consumed, the message is removed from the queue and cannot be processed by others.

Point-to-point message queues can be used to implement a variety of patterns such as:

* Request-Response: A producer sends a request message to a queue, and a consumer retrieves the message and sends back a response message.

* Work Queue: Producers send work items to a queue, and consumers retrieve the work items and process them.

* Guaranteed Delivery: Producers send messages to a queue, and consumers can be configured retry retrieving messages until they are successfully processed.

1. Publish-Subscribe Message Queues

Publish-subscribe message queues deliver messages from a producer to all subscribed consumers. Consumers can subscribe to multiple queues and unsubscribe anytime, allowing flexible message handling.

Publish-Subscribe Message Queues are often used to implement real-time streaming applications, such as social media and stock market tickers.

They can also be used to implement event-driven architecture, where components of a system communicate with each other by publishing and subscribing to events.

## Message Routing

Message Routing involves determining how messages are directed to their intended recipients. 

The following methods can be employed:

1. Topic-Based Routing: Messages are sent to topics or channels, and subscribers express interest in specific topics. Messages are delivered to all subscribers of a particular topic.

1. Direct Routing: Messages are sent directly to specific queues or consumers based on their addresses or routing keys.

1. Content-Based Routing: The routing decision is based on the content of the message. Filters or rules are defined to route messages that meet specific criteria.

## Scalability

Scalability is essential to ensure that a message queue system can handle increased loads efficiently. To achieve scalability:

1. Distributed Queues: Implement the message queue as a distributed system with multiple nodes, enabling horizontal scaling.

1. Partitioning: Split queues into partitions to distribute message processing across different nodes or clusters.

1. Load Balancing: Use load balancers to evenly distribute incoming messages to queue consumers.

## Dead Letter Queues and Message Prioritization

These concepts help manage failed messages and control the order in which messages are processed in a system.

1. Dead Letter Queues

Dead Letter Queues (DLQs) are a mechanism for handling messages that cannot be processed successfully. This includes:

* Messages with errors in their content or format.
* Messages that exceed their time-to-live (TTL) or delivery attempts.
* Messages that cannot be delivered to any consumer.

DLQs provide way to investigate and potentially reprocess failed messages while preventing them from blocking the system.

1. Message Prioritization

Message Prioritization is the process of assigning priority levels to messages to control their processing order. 

Prioritization criteria can include:

* Urgency: Messages with higher priority may need to processed before lower-priority messages.
* Message Content: Messages containing critical information or commands may receive higher priority.
* Business Rules: Custom business rules or algorithms may be used to determine message priority.

