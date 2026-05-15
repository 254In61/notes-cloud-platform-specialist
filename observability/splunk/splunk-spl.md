# Splunk's Search Processing Language

## Introduction

It is a powerful query language in splunk that supports statistics, filtering, and formatting. 

The search capability is a cornerstone of Splunk: through simple keywords or complex SPL queries, users can quickly locate specific logs, correlate events from different sources, and extract meaningful information.

## Step 1 — Open the Search Behind a Dashboard Panel

Every dashboard panel is powered by SPL.

* Look for "Search"
* Opens a place you can put in the commands and do quick searching.
* Avoids need to do those long XL sheets dumps!!!

## Structure of SPL - Read SPL Left to Right

### Questions to ask 

What index is used?
What is being filtered?
What command transforms data?
What output is shown?
Can I modify it?

### SPL is a pipeline - There's a logic of flow

Think:

Get data
→ Filter
→ Transform
→ Aggregate
→ Display

Example:

index=web status=500            ==> Search the web index ; Only HTTP 500 errors 
| stats count by host           ==> Count errors per server
| sort -count                   ==> Highest counts first 


### "Base Search" - First part before the first '|' - determines a) Where data comes from b) What logs are searched i.e filters

This determines:

* Where data comes from
* What logs are searched

Usually includes : 

* index : Storage location
* sourcetype : Log format/type
* host : Source system
* source : File/source path

NB : This part is obstructed when Data Model is implemented.

### Next - Most important SPL commands - Covers most dashboards

Think as a pipeline, one step feeds into the next : 

Get data
→ Filter
→ Transform
→ Aggregate
→ Display

1. What index? - Storage Location

index=?

2. What data? - Log format/type

sourcetype=?

3. What filter?

error
status=500

4. What transformation?

eval  ==> calculated fields
rex   ==> 

5. What Aggregation?

stats ==> aggregation

6. What visualization?

table ==> show colums
timechart ==> Graphs over time
chart     ==> 


### Common Dashboard Patterns

1. Pattern — Count Events

index=web
| stats count

2. Pattern — Group By Something

index=web
| stats count by status

3. Pattern — Top Talkers

index=firewall
| top src_ip

4. Pattern — Error Analysis

index=app error
| stats count by exception

### Pipe '|' - core of SPL.

Each command transforms data.

Example:

index=web
| where status >= 500
| stats count by host
| sort -count

Flow:

Search logs
    ↓
Filter rows
    ↓
Aggregate
    ↓
Sort

## Real Example Dashboard Query

Example:

index=apim_logs
| where response_time > 3000
| stats avg(response_time) as avg_rt by backend
| sort -avg_rt

Meaning:

| Step                  | Meaning                |
| --------------------- | ---------------------- |
| Search APIM logs      | `index=apim_logs`      |
| Slow requests only    | `response_time > 3000` |
| Average response time | `avg()`                |
| Per backend           | `by backend`           |
| Highest first         | `sort -avg_rt`         |

## Current splunk :)

** Sample search ... Gotten from history 

| datamodel MSB_Findings search                               ==> Search the MSB_Findings data model. Equivalent idea: SELECT * FROM MSB_Findings
| search Group="*"                                            ==> Filter events where Group exists and is not empty. Meaning: Group field must contain a value
| search Severity=*                                           ==> Only include findings with a severity value.
| search ControlID=*                                          ==> Only findings with a control ID. Likely compliance/security controls.
| search workspace_id=*                                       ==> Only records associated with a workspace.
| search service_owner_name="*"                               ==> Only findings that have a service owner.
| search environment IN (prod,nonprod)                        ==> Filter environments. Equivalent to: environment = prod OR nonprod
| search PlatformOrCustomer IN (Platform,Customer,Both)       ==> Filter by ownership type.
| search Region IN (ap-southeast-2,ap-southeast-4,us-east-1)  ==> AWS Cloud regions filter
| eval arnFilter=if("All"="All", "%", "All")                  ==> This creates a variable called arnFilter. eval creates/calculates fields. Syntax : | eval newfield=calculation 
| where like(Resource, arnFilter)                             ==> Filter rows where: Resource matches arnFilter. Since: arnFilter = "%" this currently matches ALL resources.
| stats count by service_owner_name                           ==> Aggregation. Equivalent SQL idea: SELECT service_owner_name, COUNT(*); GROUP BY service_owner_name
| sort -count                                                 ==> Descending sort. Highest counts first.


Human Translation? 

Search security/compliance findings
→ Only valid findings
→ Filter environments/regions
→ Filter resources
→ Count findings per service owner
→ Show highest first

Simplified ChatGPT query : 

| datamodel MSB_Findings search
| search Group=* Severity=* ControlID=* workspace_id=* service_owner_name=*
    environment IN (prod,nonprod)
    PlatformOrCustomer IN (Platform,Customer,Both)
    Region IN (ap-southeast-2,ap-southeast-4,us-east-1)
| stats count by service_owner_name
| sort -count

## Splunk Data Model 

Starts with this instead of index=... This means the dashboard is querying a Splunk Data Model.

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

## Examples

==> Get everything

| datamodel MSB_Findings search
| search Group=* Severity=* ControlID=* workspace_id=* service_owner_name=*
    environment IN (prod,nonprod)
    PlatformOrCustomer IN (Platform,Customer,Both)
    Region IN (ap-southeast-2,ap-southeast-4,us-east-1)
| stats count by service_owner_name
| sort -count

==> Get Craig's total vulnerabilities

| datamodel MSB_Findings search
| search Group=* Severity=* ControlID=* workspace_id=* service_owner_name="Craig Gurnett"
    environment IN (prod,nonprod)
    PlatformOrCustomer IN (Platform,Customer,Both)
    Region IN (ap-southeast-2,ap-southeast-4,us-east-1)
| stats count by service_owner_name
| sort -count

* Time range is 24 hrs
* Response under "Statistics".. Click on the output to open up more details
* Graph in "Visualization"

==> Get Craig's SNS in Prod

| datamodel MSB_Findings search
| search Group="SNS" Severity=* ControlID=* workspace_id=* service_owner_name="Craig Gurnett"
    environment IN (prod)
    PlatformOrCustomer IN (Platform,Customer,Both)
    Region IN (ap-southeast-2,ap-southeast-4,us-east-1)
| stats count by service_owner_name
| sort -count

==> Get Craig's SQS in Prod

| datamodel MSB_Findings search
| search Group="SQS" Severity=* ControlID=* workspace_id=* service_owner_name="Craig Gurnett"
    environment IN (prod)
    PlatformOrCustomer IN (Platform,Customer,Both)
    Region IN (ap-southeast-2,ap-southeast-4,us-east-1)
| stats count by service_owner_name
| sort -count
