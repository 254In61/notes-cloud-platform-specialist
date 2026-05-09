# Overview

https://www.digitalocean.com/community/tutorials/how-to-setup-a-microk8s-kubernetes-cluster-on-ubuntu-22-04
https://microk8s.io/?_gl=1*17e7mex*_gcl_au*ODU1OTE4OTY0LjE3MDczNDY2NDc.&_ga=2.241700738.1608807376.1713140065-1573050557.1713140065

=> Finding a way to learn K8s cheaply with a cluster of my own.
=> Using the Canoncial MicroK8s single-node approach. Redhat's openshift local keeps dying on me..Resource intensive and needs an RHEL machine.

# nodes
master : sexy-guy
worker : the-eagle

# Installation
## install - In all nodes
$ sudo apt -y update && sudo apt -y upgrade             # Update your system
$ sudo snap install microk8s --classic                  # Install MicroK8s
$ sudo usermod -a -G microk8s $USER && newgrp microk8s  # Give user permissions to access MicroK8s by adding to the microk8s group then reload the user groups

## check status
 $ microk8s version                                      # Ensure the MicroK8s version is the same on all nodes
 $ microk8s status --wait-ready                          # Check status while K8s starts
 $ microk8s kubectl get all --all-namespaces             # Command to see all Kubernetes objects deployed in the cluster in all namespaces.

## adding a node on the cluster
1. Ensure microk8s is installed in all the nodes and of same version on all nodes.
   amaseghe@sexy-guy:~$ microk8s version
   MicroK8s v1.31.3 revision 7449

   amaseghe@the-eagle:~$ microk8s version
   MicroK8s v1.31.3 revision 7449

2. On the master node, enable the required add-ons
   $ microk8s enable dns
   $ microk8s enable ha-cluster # The ha-cluster add-on is necessary for clustering.

3. Networking -  Ensure both PCs can communicate over the network (e.g., no firewall blocks on the necessary ports).

4. On the master node generate a join token:

   $ microk8s add-node
   From the node you wish to join to this cluster, run the following:
   microk8s join 192.168.1.98:25000/68af084183fe922e50e2f8103b36d4f4/080f15621509

   Use the '--worker' flag to join a node as a worker not running the control plane, eg:
   microk8s join 192.168.1.98:25000/68af084183fe922e50e2f8103b36d4f4/080f15621509 --worker

   If the node you are adding is not reachable through the default interface you can use one of the following:
   microk8s join 192.168.1.98:25000/68af084183fe922e50e2f8103b36d4f4/080f15621509
   microk8s join 192.168.122.1:25000/68af084183fe922e50e2f8103b36d4f4/080f15621509
   microk8s join 2405:6e00:641:39be:e7a8:29ec:b65:5cfb:25000/68af084183fe922e50e2f8103b36d4f4/080f15621509
   microk8s join 2001:4479:9b04:7700:f1f8:6f4b:900b:7800:25000/68af084183fe922e50e2f8103b36d4f4/080f15621509

5. On the worker node, use the command provided from the master:

   $ microk8s join 192.168.1.98:25000/68af084183fe922e50e2f8103b36d4f4/080f15621509
   Contacting cluster at 192.168.1.98
   Waiting for this node to finish joining the cluster. .. .. .. ..
   Successfully joined the cluster.

6. After joining, verify the status from the worker node:
   
   $ microk8s status
microk8s is running
high-availability: no
  datastore master nodes: 192.168.1.98:19001   <---- That's the IP of the master
  datastore standby nodes: none
addons:
  enabled:
    dns                  # (core) CoreDNS
    ha-cluster           # (core) Configure high availability on the current node
    helm                 # (core) Helm - the package manager for Kubernetes
    helm3                # (core) Helm 3 - the package manager for Kubernetes
  disabled:
    cert-manager         # (core) Cloud native certificate management
    cis-hardening        # (core) Apply CIS K8s hardening
    community            # (core) The community addons repository

7. On the master node, check the nodes in the cluster:
   Ensure all the nodes are in a ready state :

   $ microk8s kubectl get nodes
    NAME        STATUS   ROLES    AGE     VERSION
    sexy-guy    Ready    <none>   46m     v1.31.3
    the-eagle   Ready    <none>   3m20s   v1.31.3

## assigning roles
- By default, MicroK8s does not enforce specific roles like "master" or "worker." 
  However, you can use Kubernetes taints and tolerations to ensure workloads run only on specific nodes.
  This prevents regular workloads from being scheduled on the 'tainted' node.

- Taint the master node :
  $ microk8s kubectl taint nodes sexy-guy node-role.kubernetes.io/master=master:NoSchedule
    node/sexy-guy tainted



# kubectl & oc install

## native microk8s kubectl 
- MicroK8s come pre-bundled with its version kubectl and can execute the native Kubernetes commands to inspect and work with the cluster.

  To avoid using microk8s as a prefix while running kubectl commands, you can add an alias if you don’t have an existing installation of kubectl:
  $ alias kubectl='sudo microk8s kubectl'

## install kubectl
- To install kubectl & oc, assured way for me :
  ** Since am learning, having both kubectl & oc is a good thing for me.

  a) Navigate to the OpenShift Container Platform downloads page on the Red Hat Customer Portal.
     https://access.redhat.com/downloads/content/290?extIdCarryOver=true&sc_cid=701f2000001Css5AAC
  
  b) Download the OpenShift v4.8 Linux Client entry and save the file.

  c) Unpack the archive: $ tar xvzf <file> . You'll get kubectl and oc bin files there.

  d) Mv kubectl and oc to your $PATH


- What if you already had a native installed kubectl like what I have done above?
  a) copy the MicroK8s generated kubeconfig to the ~/.kube/config file.

$ microk8s kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://127.0.0.1:16443
  name: microk8s-cluster
contexts:
- context:
    cluster: microk8s-cluster
    user: admin
  name: microk8s
current-context: microk8s
kind: Config
preferences: {}
users:
- name: admin
  user:
    client-certificate-data: DATA+OMITTED
    client-key-data: DATA+OMITTED



$ microk8s kubectl config view --raw > ~/.kube/config  
** No, you can't have info of other clusters in same file.. It confuses the command!.. 1 cluster at a time???
** Now, you can use the native kubectl as well to run the commands.

$ kubectl get pods -A
NAMESPACE     NAME                                       READY   STATUS    RESTARTS   AGE
kube-system   calico-kube-controllers-759cd8b574-cbgjn   1/1     Running   0          59m
kube-system   calico-node-dfpc7                          1/1     Running   0          59m
kube-system   coredns-7896dbf49-wzrsf                    1/1     Running   0          59m

$ oc get pods -A
NAMESPACE     NAME                                       READY   STATUS    RESTARTS   AGE
kube-system   calico-kube-controllers-759cd8b574-cbgjn   1/1     Running   0          60m
kube-system   calico-node-dfpc7                          1/1     Running   0          60m
kube-system   coredns-7896dbf49-wzrsf                    1/1     Running   0          60m



# dashboard access

- Access the Kubernetes dashboard 
 - ** Either use a different terminal to start or push command to the background.
 - This also starts the dashboard https://127.0.0.1:10443

  $ microk8s dashboard-proxy &

- A token will be generated that will be used to login...** Token is always the same once installation is done?**

- ** Not coming up in sexy-guy..But what the fuck?.. I don't need it now... CLI for life!

# Addons for MicroK8s

- In the earlier step, you have verified the status of Kubernetes objects deployed in the MicroK8s cluster by default.
  Now to the different options and addons available in MicroK8s.
- The default installation of MicroK8s comes with the essential Kubernetes components to get the cluster up and running. 
  Installing additional components using the addons functionality provided by MicroK8s is possible.

 $ microk8s status                # Check status and see what addons have been enabled/disabled : 

 $ microk8s enable <addon name>   # Enable addon
 $ microk8s disable <addon name>  # disable addon

# Stop & Uninstall MicroK8s

- stop all the running Kubernetes components in the virtual machine. : $ sudo microk8s stop
- uninstall the MicroK8s : $ sudo snap remove microk8s

# deploy apps
- Check apps/README.md and the sample apps deployed