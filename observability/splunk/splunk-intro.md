# Splunk

REF : https://www.geeksforgeeks.org/devops/what-is-splunk/

## The challenge

In the modern age of computers, organizations produce huge quantities of machine data from networks, servers, applications, and security systems. 
Analyzing and managing such data manually is almost impossible.

Having a tool to manage the logs and perform data analytics is critical for an organization.

The tool should be able to :

* Collect logs
* Analyze the logs
* Create a visualization of the data in real-time.

## Enter Splunk

The name "Splunk" was derived from spelunking (cave exploration), as an analogy of digging deep into concealed data for value.

Splunk is an enterprise analytics platform built for :

* real-time searching
* monitoring
* analyzing machine data (such as logs)​.

It operates by collecting and indexing data into a searchable index, from which graphs, reports, alerts, dashboards, and visualizations can be created by users​.

Splunk converts enormous amounts of raw IT data into actionable information, enabling the detection of patterns, resolution of issues, and business decision-making​.

## History of Splunk

Splunk was founded in 2003 by Michael Baum, Rob Das, and Erik Swan​.

The founders were inspired by cave exploration (“spelunking”) as a metaphor for exploring the depths of IT data​.

Early on, the product focused on a powerful search engine to scan and store IT log files, addressing the need to derive value from the “everything” that generates data in an organization. 

In 2023, Splunk marked its 20th anniversary and announced it would be acquired by Cisco for $28 billion, a deal completed in March 2024​.

## Why Use Splunk?

* It provides a unified way to handle diverse log and event data for multiple purposes. Splunk’s core value is turning machine data into insight – it helps IT operations teams quickly search and troubleshoot issues across complex infrastructures, and helps security teams detect and investigate threats from a multitude of sources in one place​.

* Unlike traditional tools, Splunk can ingest any text-based data (from servers, applications, network devices, sensors, etc.) and make it searchable and correlated. This versatility means Splunk can be used for everything from monitoring website performance to analyzing user behavior. Its flexibility as a “horizontal” technology (not limited to a single domain) allows use cases in application management, cybersecurity, compliance auditing, web analytics, business intelligence and more.

## Use Cases of Splunk

Splunk’s versatility means it can be applied to a wide array of use cases across IT, security, and business functions. 

Some of the most common use cases include:

* IT Operations Monitoring: Splunk is widely used by IT operations and DevOps teams to monitor the health and performance of infrastructure and applications. By aggregating logs and metrics from servers, network gear, operating systems, databases, and cloud services, Splunk gives a unified real-time view of an organization’s tech stack.

* Cybersecurity and Threat Intelligence: One of Splunk’s strongest domains is cybersecurity. Security Operations Center (SOC) teams leverage Splunk as their SIEM platform to collect and correlate security-relevant data: firewall logs, intrusion detection alerts, endpoint logs, authentication events, etc. Splunk can continuously monitor for threat indicators (e.g., multiple failed logins, traffic to known malicious domains) and generate alerts for analysts

* Compliance and Auditing: Many organizations have compliance requirements (PCI-DSS, HIPAA, GDPR, SOX, etc.) that mandate logging of certain activities and regular reporting. Splunk is often used to meet these needs.

* Application Performance Monitoring (APM): Developers and site reliability engineers use Splunk to ensure applications are performing well and to troubleshoot issues in the software stack. While Splunk isn’t an APM tool in the traditional sense, it becomes one by analyzing application logs and metrics

## Core features of Splunk

1. Data Ingestion, Indexing and Search

Splunk can collect data from practically any source or format – logs, metrics, events, configurations, etc. – regardless of where it is coming from servers, network devices, applications, cloud services, or databases.

Example Data Sources:

| Source        | Example Data        |
| ------------- | ------------------- |
| Linux servers | `/var/log/messages` |
| Cisco devices | Syslog              |
| Azure/AWS     | Cloud audit logs    |
| Web apps      | HTTP requests       |
| Firewalls     | Traffic events      |
| Kubernetes    | Pod logs            |
| APIs          | JSON payloads       |
| Windows       | Event Viewer logs   |


On ingestion, Splunk’s indexing engine processes the raw data into searchable events, adding the timestamps and also add the metadata (like host, source, source type) to each event​

This indexing allows extremely fast search and retrieval the huge data sets. Users can also query the data using the Splunk’s Search Processing Language (SPL).

1. Log Management and Analysis

At its heart, Splunk is often used as a central log management system. Splunk continuously collects and aggregates logs from the distributed systems into one place.

Splunk then provides tools to analyze these logs for operational intelligence. 

It can also parse raw text logs into structured fields and also apply transformations (like masking sensitive data or discarding unwanted events) and perform real-time analysis on the log data.

Example:

Search all failed SSH logins
Find application crashes
Trace API failures

Splunk also supports statistical analysis of logs (through commands like stats or timechart in SPL) to derive metrics and trends from qualitative log data. This turns unstructured logs into valuable analytics such as error rate over time, user activity trends, or frequency of specific messages.

1. Real-Time Monitoring and Alerting

Splunk excels not only at retrospective analysis but also at real-time data monitoring.

As data is ingested and indexed, Splunk can continuously evaluate it against conditions or thresholds you define. Searches can be scheduled to run on a regular interval or even set to run in real-time, updating as new events stream in.

Based on these searches, Splunk can trigger alerts when certain criteria are met – for instance, if a specific error message appears, if the number of failed login attempts exceeds a threshold in a 5-minute window, or if a server’s CPU usage stays above 90% for too long. 

Alerts can be delivered through various channels (email, SMS, creating a ServiceNow ticket, executing a script, etc.). This real-time alerting capability means Splunk can function as a monitoring system for IT operations and security.

Example:

CPU spikes
Slow API responses
Memory leaks
Error rates

1. Dashboards and Visualization
To make sense of large data sets, Splunk offers robust visualization and reporting features. 

Users can build interactive dashboards that display charts, graphs, tables, maps, and other visualizations reflecting the data in Splunk​. 

These dashboards are highly customizable – you can create panels for different metrics (e.g., a line chart of website response times, a pie chart of log severity levels, a single value showing the count of active alerts, etc.)

Splunk also provides many out-of-the-box reports and the ability to generate PDF reports on a schedule. This visualization capability turns raw data into at-a-glance insights for technical and non-technical audiences alike.

1. Security and Threat Detection Features

Splunk has evolved into a leading platform for security information and event management (SIEM).

It includes features specifically aimed at security analysis: the ability to ingest data from security devices (firewalls, IDS/IPS, antivirus, etc.), perform correlation across disparate data sources, and detect anomalies or known threat patterns.

Example:

Detect brute-force attacks
Detect privilege escalation
Correlate suspicious activity
Investigate incidents

Splunk also provides access controls and audit capabilities to ensure security of the data it stores: data can be encrypted in transit and at rest, role-based access can restrict what certain users can search or see, and all user activity in Splunk can be audited​.

1. Integration with Third-Party Tools

Splunk is designed to be extensible and to fit into a larger ecosystem of IT and DevOps tools.

It provides a wide range of integrations and open interfaces. Splunk can ingest data from message queues, APIs, databases, and applications; it supports standards like syslog, and can receive data via HTTP (using the HTTP Event Collector) for custom integrations.

For example, ingesting AWS CloudWatch logs, or pulling data from Kubernetes, or integrating with Salesforce. Splunk also offers an SDK and REST API, so developers can programmatically search data or manage the platform from external scripts and applications.

## Common Alternatives

| Tool               | Focus                      |
| ------------------ | -------------------------- |
| Elastic Stack      | Open-source search/logging |
| Grafana + Loki     | Metrics + logs             |
| Datadog            | Cloud observability        |
| Microsoft Sentinel | Azure SIEM                 |
| Sumo Logic         | SaaS logging               |


## Strengths

| Strength          | Why It Matters            |
| ----------------- | ------------------------- |
| Powerful search   | Extremely flexible        |
| Fast indexing     | Near real-time            |
| Massive ecosystem | Thousands of integrations |
| Strong SIEM       | Industry-leading          |
| Good dashboards   | Operational visibility    |

## Weaknesses

| Weakness           | Impact                         |
| ------------------ | ------------------------------ |
| Expensive          | Large ingest costs             |
| SPL learning curve | Takes practice                 |
| Storage-heavy      | Logs grow quickly              |
| Complex at scale   | Requires architecture planning |

## Licensing

Splunk licensing is usually based on:

Daily ingest volume

Example:

100 GB/day
500 GB/day
1 TB/day

## Deployment Models

1. Splunk Enterprise - Self-hosted.

You manage:

Servers
Storage
Scaling

1. Splunk Cloud - Managed by Splunk.

Less infrastructure management.
