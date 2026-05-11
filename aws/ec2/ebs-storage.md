### HDD vs SDD

1. HDD(Hard Disk Drive)

* HDDs use spinning magnetic platters like a record player. Data is stored magnetically on rotating disks.
* There's mechanical moving read/write heads. To read data the disk spins, Read/Write head moves physically as data is accessed.
* Because it has moving parts, it is slower, higher latency and more wear and tear.
* Very low cost per TB and has huge capacities like 8TB, 16TB, 20TB+. This makes it great for archives, backups and large datasets.
* Disadvantages include :
  1. slow random access : Mechanical movement causes delays.
  1. Fragile : moving parts can fail.
  1. Higher Latency : Typically 5-15ms latency as compared to SSD whose latency is in microseconds.

1. SSD(Solid State Drive)

* Data is stored electronically in NAND flash cells. There are no spinning disks , no mechnical movement.
* Good examples include USB flash storage, Memory cards and RAM-Like architecture.
* SSD are as a result much faster, reliable and low latency. In addition there's lower power usage which is important for laptops, DCs and Cloud Infra.
* Are used in OS Boot, Databases, Gaming, Cloud Workloads.

Why SSD Is Dominating Modern Infrastructure?

Modern systems need:

* Fast boot times
* High IOPS
* Low latency
* Cloud-native performance

SSD provides all of these.That’s why:

* Most laptops use SSD
* Cloud providers default to SSD
* Kubernetes/database workloads prefer SSD

When HDD Still Makes Sense?

HDD is still useful for:

* Backups
* Cold storage
* Media archives
* Massive cheap storage

Because cost/TB matters more than speed.

### EBS Volume Types

Amazon Elastic Block Store provides several volume types optimized for different workloads.

They fall into two major categories:

### SSD-Backed Volumes

Best for:

* Databases
* Boot volumes
* Low latency apps
* Transactional workloads

A) gp2/gp3

===========
General purpose SSD volume that balances price and perfmance for a wide variety of workloads.
You can only use any of these as the boot volumes for EC2.

gp2 — Previous Generation SSD - Amazon EBS gp2

* Older generation but still widely used.
* Perfomance tied to volume size. Must increase volume size to gain IOPS.
* Use gp3 for new deployments and consider migrating gp2 --> gp3 where possible.

gp3 — General Purpose SSD (Recommended Default) - Amazon EBS gp3

Best for :

* Most workloads
* EC2 boot volumes.
* Web servers
* Dev/Test
* Medium databases

gp3 is preffered over gp2 for a number of reasons :

* gp3 is cheaper.
* gp3 is faster
* Separate IOPS/throughput tuning.
* Better perfomance consistency.

AWS recommends gp3 for most workloads.

Key notes :

* gp2/3 are cost effective storage, low latency.
* Are mainly used for system boot voluments, virtual desktops, Dev and Test environments.
* Size can vary from 1 GiB to 16 TiB
* gp3(new version of IOPS):

  * Baseline of 3,000 IOPS and throughput of 125 MiB/s/
  * Can increase IOPS up to 16,000 and throughut up to 1000 MiB/s independently i.e not linked.

* gp2 
  * Small gp2 volumes can burst IOPS to 3,000.
  * Size of the volumes and IOPS are linked, max IOPS is 16,000
  * 3 IOPS per GiB, means at 5,334 GiB at the max IOPS.



B) io1/io2 - Provisioned IOPS (PIOPS) SSD

===========

Highest perfomance SSD volume for mission-critical low-latency or high-throuput workloads.

They support EBS multi-attach.

You use these when :

* Deploying critical business applications with sustained IOPS perfomance.
* Applications that need more than 16,000 IOPS.
* Database workloads sensitive to storage perfomance and consistency.

io1 - Amazon EBS io1

* Older version of io2.
* Usually existing workloads only

* 4GiB - 16 TiB
* Max PIOPS: 64,000 for Nitro EC2 instances and 32,000 for other.
* Can increase PIOPS independently from storage size.

io2 (Recommended) - Amazon EBS io2

* 4 GiB - 64 TiB
* Sub-millisecond latency.
* Max PIOPS: 256,000 with an IOPS:GiB ratio of 1,000:1

Best for :

* Oracle Database
* Microsoft SQL Server
* SAP HANA
* High-end transactional systems



### HDD-Backed Volumes

Cannot be a boot volume.

125 GiB to 16 TiB.

Best for :

* Large sequential workloads.
* Throughput-oriented systems
* Cheap storage.

A) st1 - Throuput optimized HDD - Amazon EBS st1

Low cost HDD volume designed for frequently accessed, throughput-intensive workloads.

Max throughtput 500 MiB/s - Max IOPS 500.

Best for :

* Big data
* Data warehouses
* Log processing
* Streaming workloads.

| Feature        | Value      |
| -------------- | ---------- |
| Optimized for  | Throughput |
| Random IOPS    | Poor       |
| Sequential I/O | Excellent  |

* Max throughput 5000 MiB/s and max IOPs 500.

B) sc1 - Cold HDD - Amazon EBS sc1

Lowest cost HDD volume designed for less frequently accessed workloads.

Max throughput 250MiBs - Max IOPS 250.

Best for :

* Infrequently accessed data
* Archives
* Cheap storage

## EBS Multi-Attach - io1/io2 family

Enables attaching the same EBS volume to multiple EC2 instances within the SAME AZ.

Only io1/2 family allows this.

Each instance has full read and write permissions to the high-perfomance volume.

Upto 16 EC2 instances can multi-attach to the EBS volume.

Must use a file system that's cluster-aware and not XFS, EXT4 etc.

Use cases :

* Achieve higher application availability in clustered Linux applications e.g Teradata.
* Applications must manage concurrent write operations.


## EBS Encryption

When you create an encrypted EBS volume you get the following:

* Data at rest is encrypted inside the volume.
* All the data in flight moving between the instances and the volume is encrypted.
* All snapshots are encrypted.
* All volumes created from the snapshots are encrypted.

Encryption and decryption are handled transparently, you have nothing to do.

Encryption has minimal impact on latency.

EBS Encryption leverages keys from KMS (AES-256)

NB : Any snapshot created from a non-encrypted volume will NOT be encrypted.
     To encypt the snapshot, you create a copy of the snapshot then encrypty that new snapshot.You select the KMS Key.
     You can then create a volume which wil be automatically encrypted.

NB : You could also take the un-encrypted snapshot and create a volume from it. WWhile creating the volume select "Encrypt this volume" and the necessary KMS key.
     That way, you will have created an encrypted EBS volume.
