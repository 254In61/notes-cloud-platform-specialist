
# AMI ( Amazon Machine Image)
- AMI are a customization of an EC2 instance.
- You add your own sw, config, os, monitoring etc.
- Faster boot/configuration time because all your sw is pre-packaged.
- AMIs are built for specific region and can be copied across regions.
- You can launch EC2 instances from : 
  a) A public AMI : AWS Provided
  b) Your own AMI : You make maintain them yourself.
  c) AWS Marketplace AMI : An AMI someone else made and potentially sells.


If building AMI from an existing EC2 instance : 
- Start an EC2 instance and customize it.
- Stop the instance ( for data integrity)
- Build an AMI -this will also create EBS snapshots
- Launch instances from the new AMI

