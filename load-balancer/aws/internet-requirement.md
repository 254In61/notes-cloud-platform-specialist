# internet requirement

## Error

╷ │ Error: creating ELB Classic Load Balancer (msb-demo-clb-2): operation error Elastic Load Balancing: CreateLoadBalancer, https response error StatusCode: 400, RequestID: 34d8e415-a20a-4bcf-bc3d-1ee9f5c878e7, InvalidSubnet: VPC vpc-66ae7d03 has no internet gateway │ │ with aws_elb.classic_lb["clb-2"], │ on ec2.tf line 33, in resource "aws_elb" "classic_lb": │ 33: resource "aws_elb" "classic_lb" { │ ╵

## Explanation

This error means your Classic ELB is being created as an internet-facing load balancer, but the subnet/VPC does not have Internet Gateway access.

AWS requires:

Internet-facing ELB
    ↓
Must be in public subnet
    ↓
Public subnet must route to Internet Gateway (IGW)

Your VPC:

vpc-66ae7d03 currently has no Internet Gateway attached OR the subnet route table does not route to it.

AWS checks whether that subnet is public.

A subnet is considered public when:

Route Table: 0.0.0.0/0 → igw-xxxxxxxx exists.

Since it doesn't, ELB creation fails.

## Two Possible Architectures

1. Option 1 — Public / Internet-facing ELB

Users from internet can access it.

Architecture:

Internet
   ↓
Internet Gateway
   ↓
Public Subnet
   ↓
ELB

You need:

// Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
}

// Public Route
resource "aws_route" "internet_access" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.igw.id
}

// Associate Route Table to Subnet
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

1. Option 2 — Internal ELB : No Internet Gateway required.

If the ELB is only for internal/private traffic:

internal = true
// By default, this is false..So LB created are internet-facing.
// And AWS expects public subnet, IGW and internet route

Example:

resource "aws_elb" "classic_lb" {
  name     = "internal-elb"
  internal = true

  subnets = [aws_subnet.private.id]
}

Architecture:

Private App
    ↓
Internal ELB
    ↓
Private Instances
