# Introduction

In AWS, there are two main types of storage attached to EC2 instances:

1. Instance Store (ephemeral/local storage)

1. EBS (Elastic Block Store)

They serve different purposes.

## EC2 Instance Store

Instance Store is physically attached storage on the host machine running your EC2 instance.

Think of it as:

* Local SSD/NVMe disks directly attached to the server
* Very fast temporary storage
* Lost when the instance stops/terminates

Why use instance store? Because it is :

* Very fast
* Vary low latency
* High IOPS
* Direct NVMe access
* No network overhead.

Key Characteristics :

* Does not survive stop/start of termination but survives a reboot.
* The cost is included as part of the instance price.
* No Snapshots capability.
* No Replication capability.

It is ideal for :

* Caching : Cache data is temporary anyway.Examples are Redis and Memcached.
* High-Speed Big Data / Analytics : Intermediate processing data can live on instance store. Examples are Apache Spark and Hadoop.
* Temporary processing and Buffering : Examples include video rendering, ETL scratch space, AI/ML training temp datasets, Sorting/Indexing operations.
* High Perfomance Databases : Some distributed databases use local NVMe for speed e.g Apache Cassandra, Elasticsearch. Replication happens at application level.

## EBS - Elastic Block Store

* A network-attached drive you can attach to your instances while they run. It is not a physical drive.Think of it as a "network USB stick", that you can pick from one computer to another..It's not physical though. It's attached through the network.
* Persistent : Allows us to persist data even if instance is terminated.
* Mobility : They can be detatched from one EC2 instance and attached to another quickly.

Key Characteristics :

* Latency : Being a network drive, it uses the network to communicate to the instance. This means there will be some latency unlike instance store which is physically attached to the instance.
* Bound to specific AZ : They are bound to a specific AZ so have to mounted to an Instance within the same AZ.
* Provision Capacy : Being a volume, you to provision capacity i.e size in GBs and IOPs. These 2 metrics determine the costs.
* "Delete on Termination" is selected for the root volume but not other volumes. Meaning root EBS volume is deleted alongside the instance being terminated.
  Any other volume is not deleted because it is disabled by default.
* Backup support : Snapshot enabled.

Why use EBS? Use when data matters :

* OS Disk
* Databases
* Long-term application data.
* Persisten logs
* Production workloads.

### EBS Snapshot

* A copy/backup(snapshort) of your EBS volume at a point in time.
* You don't need to detach your volume to do the snaposhot, but it is recommended.
* You can copy snaposhorts across AZ or Region

Features :

1. EBS Snapshot Archive

* Move a snapshot to an "archive tier" that is 75% cheaper.
* Takes within 24 to 72 hrs for restoring the archive.

1. Recycle Bin for EBS Snapshots

* Setup rules to retain deleted snapshots so you can recover them after an accidental deletion.
* Specify retention ( from 1 day to 1 yr)

1. Fast snapshot Restore (FSR)

* Force full initialization of snapshot to have no latency on the first use.
* Costs $$$

