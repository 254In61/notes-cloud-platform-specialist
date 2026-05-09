# intro
Using print() in production AWS code is a bit like debugging with sticky notes—it works briefly, but falls apart as soon as things scale or break in non-obvious ways. 

Proper logging isn’t just cleaner; it’s essential.

# 🆚 print() vs logging

print()
==========
- Writes plain text to stdout
- No structure, no severity levels
- Hard to filter/search
- Not designed for production systems

logging Using Python’s logging module:
======================================
- Supports log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Structured, consistent output
- Easily integrated with monitoring tools
- Can be routed, filtered, and formatted

# Why this matters in AWS

When running in AWS (Lambda, ECS, EC2, etc.), logs are typically sent to Amazon CloudWatch Logs.

This is where the differences become critical.

# Key reasons to use logging

1. Log levels = control and signal

With logging:

logger.debug("Payload received")
logger.error("Failed to process message")

You can:

- Show only errors in production
- Enable debug logs when troubleshooting

With print() → everything is just noise.

2. Structured logging (huge advantage)

You can log structured data: logger.info("Processing order", extra={"order_id": 123, "user_id": 456})

This enables:

- JSON logs
- Queryable fields in CloudWatch

3. Integration with monitoring & alerting

Logging integrates with:

- CloudWatch alarms
- SIEM tools
- Observability platforms

Example: Trigger alert when "ERROR" appears 5 times in 1 minute

👉 Impossible to do cleanly with raw print()

4. Easier debugging in CloudWatch 

CloudWatch lets you:

- Filter logs by keywords or patterns
- Search only errors or warnings
- Create alarms on specific log entries

👉 This only works well if logs are structured and leveled

5. Better observability for distributed systems

In your kind of setup (SQS, Lambda, APIs):

- Requests flow across multiple services
- Failures may happen asynchronously

Logging helps you:

- Trace execution
- Correlate events
- Understand system behavior over time

print() gives you a messy stream with no context.

