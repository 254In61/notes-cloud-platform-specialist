# aws lb listener

Before you start to use a load balancer, you must add one or more listeners.

A listener is a process that uses the configured protocol and port to check for connection requests.

Listeners can support both HTTP and HTTPS/TLS protocols. You should always use an HTTPS or TLS listener, so that the load balancer does the work of encryption and decryption in transit.

## terraform code

resource "aws_elb" "classic_lb" {
  for_each = local.classic_Lbs

  name                  = lb_name
  subnets               = subnet_id
  security_groups       = sec_group_id
  
  listener {
    lb_port             = 80      ==> Port on LB that clients communicate with. Unique lb port per listener.
    lb_protocol         = "HTTP"  ==> Protocol that clients <---> LB use to communicate.

    instance_port       = 8080    ==> Port on the backend EC2 instance
    instance_protocol   = "HTTP"  ==> Protocol that backend servers <----> LB use to communicate
  }

  listener {
    lb_port             = 80
    lb_protocol         = "HTTP"
    instance_port       = 8000
    instance_protocol   = "HTTP"
  }

  listener {
    lb_port             = 443
    lb_protocol         = "HTTPS" ==> For a secure protocol i.e SSL or HTTPS, ssl_cert MUST be included
    ssl_certificate_id  = var.certificate_arn  ==> Tells AWS: "Use THIS certificate for secure conversations."
    instance_port       = 8443
    instance_protocol   = "HTTPS"
  }

  listener {
    lb_port             = 444
    lb_protocol         = "HTTPS"
    ssl_certificate_id  = var.certificate_arn
    instance_port       = 8444
    instance_protocol   = "HTTP"
  }

  health_check {
    target              = "HTTP:80/"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }

  connection_draining = false

  idle_timeout                = 60
  instances                   = []

  tags = {
    Name                = "msb-demo-${each.key}"
  }
}

## Common Patterns

1. HTTPS → HTTP (Most Common)
=============================

listener {
  lb_port            = 443      --> Port exposed publicly on the ELB
  lb_protocol        = "HTTPS"  --> Protocol clients use to connect to ELB

  instance_port      = 8080     --> Port on the backend EC2 instance
  instance_protocol  = "HTTP"   --> Protocol ELB uses to talk to EC2

  ssl_certificate_id = var.cert_arn
}

Architecture:

Internet HTTPS ( Client connection is encrypted )
    ↓
ELB decrypts SSL
    ↓
Private VPC HTTP ( Backend traffic becomes plain HTTP )
    ↓
Application

Advantages:

* simpler backend
* lower CPU on instances
* ELB manages certificate

1. HTTPS → HTTPS - End-to-end encryption : SSL terminates at ELB >> ELB re-encrypts traffic to backend
======================================================================================================

listener {
  lb_port            = 443
  lb_protocol        = "HTTPS"

  instance_port      = 8443
  instance_protocol  = "HTTPS"
}

Architecture:

Internet HTTPS
    ↓
Encrypted
    ↓
ELB
    ↓
Still encrypted
    ↓
Backend

Used for:

* compliance
* zero-trust
* strict security requirements

1. HTTP → HTTP
===============

listener {
  lb_port            = 80
  lb_protocol        = "HTTP"

  instance_port      = 8080
  instance_protocol  = "HTTP"
}

No encryption anywhere.

## Important Rule

lb_port must be unique.
This is because the ELB receives incoming traffic on those frontend ports.

You cannot have:

* 443 → backend A
* 443 → backend B

because AWS would not know which listener should receive the traffic.

## Real-world Example

Suppose you run:

Service	    Backend Port
Web App	      8080
Admin App	  8443

You could configure:

listener {
  lb_port           = 80
  lb_protocol       = "HTTP"

  instance_port     = 8080
  instance_protocol = "HTTP"
}

listener {
  lb_port           = 443
  lb_protocol       = "HTTPS"

  instance_port     = 8443
  instance_protocol = "HTTPS"
}

Meaning:

users connect to:
* http://elb:80
* https://elb:443

Then ELB forwards traffic internally to different backend ports.

## Move away from Classic ELB

Classic ELB is old.

AWS generally recommends:

* Application Load Balancer (ALB)
* Network Load Balancer (NLB)

because ALB supports:

* host-based routing
* path routing
* multiple target groups
* HTTP/2
* WebSockets
* better TLS support

For modern apps, ALB is usually preferred.
