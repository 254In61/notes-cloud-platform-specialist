# you need to know namespaces first to get resources within the namespaces
 $ kubectl get namespaces
NAME              STATUS   AGE
countries         Active   74d
default           Active   103d
devops-tools      Active   85d
kube-node-lease   Active   103d
kube-public       Active   103d
kube-system       Active   103d
observability     Active   81d

# get pods within a certain namespace
 $ kubectl get pods -n devops-tools
NAME                                  READY   STATUS    RESTARTS       AGE
grafana-deployment-7d967f9fd5-6629l   1/1     Running   1 (2d3h ago)   4d
jenkins-deployment-c7b45ff9-8vn86     1/1     Running   1 (2d3h ago)   4d

# k8s main resources
- The following Kubernetes main resource types can be created and configured by using a YAML or a JSON manifest file, or by using OpenShift management tools:

** All these are defined under a specific project.
** To see them you go to a project, click on it and see the list.

1. Pods (pod)
Represent a collection of containers that share resources, such as IP addresses and persistent storage volumes. It is the primary unit of work for Kubernetes.

2. Services (svc)
Define a single IP/port combination that provides access to a pool of pods. By default, services connect clients to pods in a round-robin fashion.

3. ReplicaSet (rs)
Ensure that a specified number of pod replicas are running at any given time.

4. Persistent Volumes (pv)
Define storage areas for Kubernetes pods to use.

5. Persistent Volume Claims (pvc)
Represent a request for storage by a pod. PVCs link a PV to a pod so that its containers can use the provisioned storage, usually by mounting the storage into the container's file system.

6. ConfigMaps (cm) and Secrets
Contain a set of keys and values that other resources can use. ConfigMaps and Secrets centralize configuration values that several resources use. Secrets differ from ConfigMaps in that the values of Secrets are always encoded (not encrypted), and their access is restricted to fewer authorized users.

7. Deployment (deploy)
A representation of a set of containers that are included in a pod, and the deployment strategies to use. 

A deployment object contains the configuration to apply to all containers of each pod replica, such as the base image, tags, storage definitions, and the commands to execute when the containers start. 

Although Kubernetes replicas can be created stand-alone in OpenShift, they are usually created by higher-level resources such as deployment controllers.

# cluster into
 $ kubectl cluster-info
Kubernetes control plane is running at https://127.0.0.1:16443
CoreDNS is running at https://127.0.0.1:16443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

# list nodes in the cluster
 $ kubectl get nodes
NAME        STATUS   ROLES    AGE    VERSION
sexy-guy    Ready    <none>   103d   v1.31.6
the-eagle   Ready    <none>   103d   v1.31.6

The STATUS value of Ready means that this node is healthy and can accept new pods. 

A STATUS value of NotReady means that a condition triggered the NotReady status and the node is not accepting new pods.

# more detail on specific node
  $ kubectl describe node sexy-guy


# Authentication
- For users to interact with a cluster, they must first authenticate.

- A user is an entity that can make requests to the cluster API.
  A user object represents an actor that can be granted permissions in the system by adding
  roles to the user or to the user's groups.

- The authentication layer identifies the user that is associated with requests to the cluster Api.
  After authentication, the authorization layer then uses information about the requesting user to determine whether the request is allowed or not.

- Several types of users can exist :

1. Regular users
2. System users 
   - Infrastructure uses system users to interact with the API securely. 
   - Some system users are automatically created, including the cluster administrator, with access to everything.
   - By default, unauthenticated requests use an anonymous system user.

- Service accounts
  - ServiceAccount objects represent service accounts. 
  - Project administrators can create additional service accounts to define access to the contents of each project.

# operators
## Overview
- Operators automate the required tasks to maintain a healthy cluster that would otherwise require human intervention.

- Operators provide the means of monitoring applications, performing health checks, managing over-the-air (OTA) updates, and ensuring that applications remain in your specified state.

- Operators integrate with Kubernetes APIs and CLI tools such as kubectl and oc commands. Operators are the preferred method of packaging, deploying, and managing services on the control plane.

- Because CRI-O and the Kubelet run on every node, almost every other cluster function can be managed on the control plane by using Operators. 

- Components that are added to the control plane by using operators include critical networking and credential services.

- Operators in RHOCP are managed by two different systems, depending on the purpose of the operator :
1. Cluster version operator(CVO)
2. Operator Lifecycle Manager(OLM)

## Cluster Operators & Cluster Version Operator(CVO)
- Cluster operators perform cluster functions. These operators are installed by default, and the CVO manages them.

- Cluster operators use a Kubernetes kind value of clusteroperators, and thus can be queried via oc or kubectl commands. 

- As a user with the 'cluster-admin' role, use the oc get clusteroperators command to list all the cluster operators.

[amaseghe@sexy-guy openshift-local]$ oc get clusteroperators
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.16.4    True        False         False      6h30m   
config-operator                            4.16.4    True        False         False      27d     
console                                    4.16.4    True        False         False      6h31m   
control-plane-machine-set                  4.16.4    True        False         False      27d     
dns                                        4.16.4    True        False         False      6h32m   
etcd                                       4.16.4    True        False         False      27d     
image-registry                             4.16.4    True        False         False      6h32m   
ingress                                    4.16.4    True        False         False      27d     
...output omitted...

- For more details about a cluster operator, use the :
$ describe clusteroperators <operator-name>
to view the field values that are associated with the operator, including the current status of the operator. 

The describe command provides a human-readable output format for a resource. As such, the output format might change with an RHOCP version update.

[amaseghe@sexy-guy openshift-local]$ oc get clusteroperators dns -o yaml
apiVersion: config.openshift.io/v1
kind: ClusterOperator
metadata:
  annotations:
    include.release.openshift.io/ibm-cloud-managed: "true"
    include.release.openshift.io/self-managed-high-availability: "true"
    include.release.openshift.io/single-node-developer: "true"
  creationTimestamp: "2024-07-29T10:27:32Z"
  generation: 1
  name: dns
  ownerReferences:
  - apiVersion: config.openshift.io/v1
    controller: true
    kind: ClusterVersion
    name: version
    uid: 52254404-d382-4601-a6e3-8071daa551fd
  resourceVersion: "28236"
  uid: e0b8683f-307c-46db-9a81-208c1eaae546
spec: {}
status:
  conditions:
  - lastTransitionTime: "2024-08-25T04:43:03Z"
    message: DNS "default" is available.
...output omitted...


## Optional add-on operators & Operator Lifecycle Manager(OLM)
- OLM manages the optional add-on operators.

- As a user with the cluster-admin role, use the get operators command to list all the add-on operators.

[user@host~]$ oc get operators
NAME                                 AGE
lvms-operator.openshift-storage      34d
metallb-operator.metallb-system      34d

- You can likewise use the describe and get commands to query details about the fields that are associated with the add-on operators.


## Operator pods
- Operators use one or more pods to provide cluster services. 
  You can find the namespaces for these pods under the relatedObjects section of the detailed output for the operator. 

[amaseghe@sexy-guy openshift-local]$ oc get clusteroperators dns -o yaml
apiVersion: config.openshift.io/v1
kind: ClusterOperator
metadata:
  annotations:
    include.release.openshift.io/ibm-cloud-managed: "true"
  ...output omitted...
  name: dns
  ownerReferences:
  - apiVersion: config.openshift.io/v1
 ...output omitted...
  resourceVersion: "28236"
  uid: e0b8683f-307c-46db-9a81-208c1eaae546
spec: {}
status:
  conditions:
  - lastTransitionTime: "2024-08-25T04:43:03Z"
    message: DNS "default" is available.
  ...output omitted...
  extension: null
  relatedObjects:
  - group: ""
    name: openshift-dns-operator
    resource: namespaces
  - group: operator.openshift.io
    name: default
    resource: dnses
  - group: ""
 ...output omitted...
  - name: operator
    version: 4.16.4



- As a user with a cluster-admin role, use the -n namespace option on the get pod command to view the pods. 
- For example, use the following get pods command to retrieve the list of pods in the openshift-dns-operator namespace.

 $ oc get pods -n openshift-dns-operator
NAME                            READY   STATUS    RESTARTS   AGE
dns-operator-7bdf6fdb48-tg7gg   2/2     Running   0          27d

- Use the -o yaml or -o json output formats to view or analyze more details about the pods. 
  The resource conditions, which are found in the status for the resource, track the current state of the resource object. 
  The following example uses the jq processor to extract the status values from the JSON output details for the dns pod.

[user@host~]$ oc get pod -n openshift-dns-operator \
dns-operator-64688bfdd4-8zklh -o json | jq .status
{
  "conditions": [
    {
      "lastProbeTime": null,
      "lastTransitionTime": "2023-02-09T21:24:50Z",
      "status": "True",
      "type": "Initialized"
    },
...output omitted...

- In addition to listing the pods of a namespace, you can also use the --show-labels option of the get command to print the labels used by the pods. 
  The following example retrieves the pods and their labels in the openshift-etcd namespace.

[user@host~]$ oc get pods -n openshift-etcd --show-labels
NAME                   READY   STATUS      RESTARTS   AGE   LABELS
etcd-master01          4/4     Running     68         35d   app=etcd,etcd=true,k8s-app=etcd,revision=3
installer-3-master01   0/1     Completed   0          35d   app=installer