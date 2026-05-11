# Amazon EFS - Elastic File System

It is a Managed NFS(Network File System) that can be mounted on many EC2s.

Highly available and scalable.

Very expensive compared to gp2. It is 3xgp2 cost.

It allows multiple EC2 instances to:

* Read
* Write
* Share
* Access the same files simultaneously

across multiple Availability Zones.

Uses NFSv4.1 protocol.

Uses security group to control access to EFS

Compatible with Linux based AMI(not Windows).

You can enable encryption at rest using KMS.

Uses standard POSIX file system(~ Linux) as the standard file API.

No need to plan in advance. It will expand automatically and you pay per GiG use.

## Architecture

* You create your EFS filesystem
* Surround it with Security Group
* Then connect to as many EC2s as you want.


## Why Does EFS Exist?

Because distributed systems often need:

* Shared files
* Shared storage
* Centralized file access

without managing your own file server.

## Common Problems EFS Solves

1. Multiple EC2 Instances Need Shared Files

Example: 10 web servers behind a load balancer

Each server needs access to:

* Uploaded images
* Shared configs
* Static files

Without EFS:

* Files exist only on one server
* Syncing becomes difficult

With EFS:

* All servers see the same filesystem

1. Kubernetes Shared Persistent Storage

Example: Kubernetes , Amazon Elastic Kubernetes Service

Containers are ephemeral. If a pod dies, local storage disappears

EFS provides,shared persistent storage across pods/nodes.

Useful for:

* Shared uploads
* CMS content
* ML models
* Shared configs

1. Lift-and-Shift Legacy Apps

Many old enterprise apps expect:

* Shared POSIX file systems
* NFS mounts

EFS lets those apps run in AWS without redesigning storage.

1. Shared Content Management

Example: WordPress

Multiple WordPress servers need shared:

* Images
* Themes
* Plugins

EFS solves that.

## How EFS Works

EFS uses:

* NFS protocol
* Network-attached storage

EC2 instances mount it like this:

 $ sudo mount -t nfs4 fs-xxxxx:/ /mnt/efs

Then all instances can access: /mnt/efs like a normal Linux filesystem.

## Why Not Use S3 Instead?

Amazon S3 is object storage, not a filesystem.

S3:

* No POSIX filesystem
* No file locking
* No normal Linux file operations

Applications expecting:

/var/www/uploads

cannot directly use S3 easily.

EFS behaves like a real Linux filesystem.

## Perfomance and Storage Classes

1. EFS Scale
   * Thousands of concurrent NFS clients, 10GB+/s throughput.
   * Grow to Petabyte-scale network file system, automatically.

1. Perfomance Mode (set at NFS creation time):
   * General Purpose (default) - Latency-sensitive use cases e.g web server, CMS etc.
   * Max I/O - Higher latency, throughput, highly parallel (big data, media processing).

1. Throughput Mode 
   * Bursting - 1 TB = 50 MiB/S + burst up to 100MiB/s
   * Provisioned - Set your throughput regardless of storage size , example: GiB/s for 1 TB storage
   * Elastic - Automatically scales throughout up or down based on your workloads.
     * Upto 3GiB/s for reads and 1GiB/s for writes.
     * Used for unpredictable workloads.

## Storage Classes

Storage Tiers : Lifecycle management feature - Move file over N days

* Standard : For frequently accessed files.
* Infrequence Access (EFS-IA): Cost to retrieve files, lower proce to store.
* Archive: Rarely accessed data(few times each year), 50% cheaper.


Implement lifecycle policies to move files between storage tiers after certain time.

Availability and Durability : 
* Standard : Multi-AZ, great for Prod.
* One Zone : One AZ, great for dev, backup enabled by default, compatible with IA(EFS One Zone-IA)

