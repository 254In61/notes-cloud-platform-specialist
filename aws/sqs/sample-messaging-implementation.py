import queue
import threading

# In a real-world scenario, you might want to consider using a dedicated message queue service like 
# RabbitMQ , AWS SQS, Azure Service Bus, or Apache Kafka for distributed systems

"""
Step 1: Define the Message Class
"""
class Message:
    def __init__(self, messageType, payload):
        self.messageType = messageType
        self.payload = payload
    # Add any other fields as needed

"""
Step 2: Create a Message Queue

Create a class for your message queue. 
This class should handle the operations like enqueue and dequeue.
"""
class MessageQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)

    def send(self, message):
        with self.not_empty:
            self.queue.put(message)
            self.not_empty.notify()

    def receive(self):
        with self.not_empty:
            while self.queue.empty():
                self.not_empty.wait()
            return self.queue.get()
       
"""
Step 3: Create Producers and Consumers
Implement functions or classes that act as producers and consumers. 
Producers enqueue messages, and consumers dequeue messages.
"""

# Producer function
def producer(mq, id, message):
    print(f'Producer {id} sending: {message}')
    mq.send(message)

# Consumer function
def consumer(mq):
    msg = mq.receive()
    print(f'Consumer received: {msg}')

if __name__ == '__main__':
    message_queue = MessageQueue()

    producer_thread = threading.Thread(target=producer, args=(message_queue, 1, 'Hello, World!'))
    consumer_thread = threading.Thread(target=consumer, args=(message_queue,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
