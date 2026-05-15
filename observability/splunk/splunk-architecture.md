# Splunk Architecture

Splunk’s architecture is modular and scalable, consisting of several key components that work together in a data pipeline. 

The primary components are forwarders, indexers, and search heads, with additional supporting roles for management and coordination.

### Forwarder - collect logs and send them to Splunk.

A Splunk Forwarder is a lightweight agent installed on source systems (servers, network devices, applications) to collect data and send it to the Splunk indexer.

Example:

Linux VM sends syslogs
Cisco router sends syslog
Azure diagnostic logs forwarded

Forwarders continuously monitor specified log files, system metrics, network ports, etc., and forward that data to the indexing layer.

There are two types of forwarders in Splunk:

* Universal Forwarder (UF) which simply sends raw data as is (with minimal overhead).
* Heavy Forwarder (HF) which can parse and preprocess data before sending.

### Indexer - Where the raw data lives

The Splunk Indexer is the heart of the Splunk architecture – it receives raw data (from forwarders or other inputs), processes it, and stores it as searchable events in indexes.

Indexers:

Receive data
Compress/store it
Build searchable indexes

When data arrives at an indexer, it goes through parsing (if not already done by a heavy forwarder): breaking the stream into individual events, identifying timestamps, extracting default fields (host, source, sourcetype), and applying transformations (like dropping debug events or masking fields as configured)​.

A raw log might look like:

''' Jul 10 10:22:01 web01 sshd[1234]: Failed password for admin from 10.1.1.5 '''

Splunk extracts fields automatically:

| Field  | Value    |
| ------ | -------- |
| host   | web01    |
| source | sshd     |
| user   | admin    |
| src_ip | 10.1.1.5 |


After parsing, the indexer writes the data to disk in a structured way: it stores the raw data (usually compressed) and builds index files (often called tsidx files) that map keywords/terms to locations in the raw data.

Splunk stores:

Raw event data
Indexed metadata

| Concept    | Meaning            |
| ---------- | ------------------ |
| Index      | Storage location   |
| Sourcetype | Type/format of log |
| Source     | File/source input  |
| Host       | Origin system      |

Example:

index=linux
sourcetype=syslog
host=web01

## Search Head - UI/query engine.

The Splunk Search Head is the component that provides the user interface (web or CLI) for users to search and analyze data.

It accepts search requests from users (for example, a query string in SPL) and distributes those searches to the indexers which contain the data​.

1. Other Components

Splunk Enterprise includes additional components for management and coordination. 

* A Deployment Server is a Splunk instance (often the same as a search head or a dedicated node) that centrally manages configuration for other Splunk instances.

* A License Master (or license manager) is responsible for managing Splunk license usage. Splunk’s traditional license is based on the volume of data indexed per day, and a license master ensures that all indexers stay within licensed limits, pooling the quota across a deployment. It will disable searching if the license is grossly violated.

* In clustered environments, there may also be a Cluster Master node (for indexer clusters) and a Deployer (to push configs to search head clusters)

## How Splunk works - High Level Flow

Data Sources
    ↓
Forwarders / Collectors
    ↓
Indexers
    ↓
Search Head
    ↓
Dashboards / Alerts / Reports

## Installing Splunk on Linux

https://www.geeksforgeeks.org/linux-unix/how-to-install-splunk-on-linux/

## What is a Data Model?

In Splunk, a data model is:

* a structured abstraction layer
* normalized fields
* optimized for dashboards and acceleration

Think of it like:

Raw Logs
   ↓
Normalized Schema
   ↓
Data Model
   ↓
Dashboard Queries

This is common in:

* security dashboards
* compliance dashboards
* SIEM apps
