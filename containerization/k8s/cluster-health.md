# Operators
- Operators are important components of Red Hat OpenShift Container Platform (RHOCP). 
  Operators automate the required tasks to maintain a healthy RHOCP cluster that would otherwise require human intervention. 
  Operators are the preferred method of packaging, deploying, and managing services on the control plane.

- Operators integrate with Kubernetes APIs and CLI tools such as kubectl and oc commands. 
  Operators provide the means of monitoring applications, performing health checks, managing over-the-air (OTA) updates, 
  and ensuring that applications remain in your specified state.

- Because CRI-O and the Kubelet run on every node, almost every other cluster function can be managed on the control plane by using Operators. 
  Components that are added to the control plane by using operators include critical networking and credential services.

Operators in RHOCP are managed by two different systems, depending on the purpose of the operator :
1. Cluster version operator(CVO)
2. Operator Lifecycle Manager(OLM)

# Cluster Version Operator(CVO)
- Cluster operators perform cluster functions. These operators are installed by default, and the CVO manages them.

- Cluster operators use a Kubernetes kind value of clusteroperators, and thus can be queried via oc or kubectl commands. 

- As a user with the cluster-admin role, use the oc get clusteroperators command to list all the cluster operators.

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

- For more details about a cluster operator, use the describe clusteroperators operator-name command to view the field values that are associated with the operator, including the current status of the operator. The describe command provides a human-readable output format for a resource. As such, the output format might change with an RHOCP version update.

[amaseghe@sexy-guy openshift-local]$ oc describe clusteroperators dns

- For an output format that is less likely to change with a version update, use one of the -o output options of the get command. For example, use the following oc get clusteroperators command for the YAML-formatted output details for the dns operator.

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

# Operator Lifecycle Manager(OLM) Operators
- Optional add-on operators that the OLM manages can be made accessible for users to run in their applications.

- As a user with the cluster-admin role, use the get operators command to list all the add-on operators.

[user@host~]$ oc get operators
NAME                                 AGE
lvms-operator.openshift-storage      34d
metallb-operator.metallb-system      34d

- You can likewise use the describe and get commands to query details about the fields that are associated with the add-on operators.

# Operator pods
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

# Examining Cluster Metrics - examine the compute resource usage of cluster nodes and pods
- Another way to gauge the health of an RHOCP cluster is to examine the compute resource usage of cluster nodes and pods. 
- The oc adm top command provides this information. 
- For example, to list the total memory and CPU usage of all pods in the cluster, you can use the --sum option with the command to print the sum of the resource usage.

[user@host~]$ oc adm top pods -A --sum
NAMESPACE                 NAME                      CPU(cores)   MEMORY(bytes)
metallb-system            controller-...-ddr8v      0m           57Mi
metallb-system            metallb-...-n2zsv         0m           48Mi
...output omitted...
openshift-storage         topolvm-node-9spzf        0m           68Mi
openshift-storage         vg-manager-z8g5k          0m           23Mi
                                                   ------       --------
                                                    428m         10933M


- The -A option shows pods from all namespaces. Use the -n namespace option to filter the results to show the pods in a single namespace. Use the --containers option to display the resource usage of containers within a pod. 

- For example, use the following command to list the resource usage of the containers in the etcd-master01 pod in the openshift-etcd namespace.

[user@host~]$ oc adm top pods etcd-master01 -n openshift-etcd --containers
POD             NAME           CPU(cores)   MEMORY(bytes)
etcd-master01   POD            0m           0Mi
etcd-master01   etcd           71m          933Mi
etcd-master01   etcd-metrics   6m           32Mi
etcd-master01   etcd-readyz    4m           66Mi
etcd-master01   etcdctl        0m           0Mi

# Viewing Cluster Metrics on OpenShift web console
- The OpenShift web console incorporates graphs to visualize cluster and resource analytics. 
  Cluster administrators and users with either the view or the cluster-monitoring-view cluster role can access the Home → Overview page. 
  The Overview page displays a collection of cluster-wide metrics, and provides a high-level view of the overall health of the cluster.

- The Overview page displays the following metrics:
  - Current cluster capacity based on CPU, memory, storage, and network usage
  - A time-series graph of total CPU, memory, and disk usage
  - The ability to display the top consumers of CPU, memory, and storage

- For any of the listed resources in the Cluster Utilization section, administrators can click the link for current resource usage. 
  The link displays a window with a breakdown of top consumers for that resource. 
  Top consumers can be sorted by project, by pod, or by node. 
  The list of top consumers can be useful for identifying problematic pods or nodes. 
  For example, a pod with an unexpected memory leak might appear at the top of the list.

# View specific project metrics
- Home > Projects > Project of Interest
- The Project Details page displays metrics that provide an overview of the resources that are used within the scope of a specific project. 
  The Utilization section displays usage information about resources, such as CPU and memory, along with the ability to display the top consumers for each resource.
- All metrics are pulled from Prometheus. Click any graph to navigate to the Metrics page. View the executed query, and inspect the data further.
- If a resource quota is created for the project, then the current project request and limits appear on the Project Details page.

# Viewing resource metrics - 
- When troubleshooting, it is often useful to view metrics at a smaller granularity than for the entire cluster or project. 
- The Pod Details page displays time-series graphs of the CPU, memory, and file system usage for a specific pod. 
- A sudden change in these critical metrics, such as a CPU spike caused by high load, is visible on this page.

# Performing Prometheus Queries in the Web Console
- The Prometheus UI is a feature-rich tool for visualizing metrics and configuring alerts. 
- The OpenShift web console provides an interface for executing Prometheus queries directly from the web console.

- To perform a query, navigate to Observe → Metrics, enter a Prometheus Query Language expression in the text field, and click Run Queries. 
- The results of the query are displayed as a time-series graph

# Query Cluster Events and Alerts
- Some developers consider OpenShift logs to be too low-level, thus making troubleshooting difficult. 
  Fortunately, RHOCP provides a high-level logging and auditing facility called events. 
  Kubernetes generates event objects in response to state changes in cluster objects, such as nodes, pods, and containers. 
  Events signal significant actions, such as starting a container or destroying a pod.

- To read events, use the $ oc get events. 
  The command lists the events for the current RHOCP project (namespace). 
  You can display the events for a different project by adding the -n namespace option to the command. 
  To list the events for all the projects, use the -A (or --all-namespaces) option.

-  The following get events command prints events in the openshift-kube-controller-manager namespace.

[user@host~]$ oc get events -n openshift-kube-controller-manager
LAST SEEN  TYPE    REASON                 OBJECT                                MESSAGE
12m        Normal  CreatedSCCRanges       pod/kube-controller-manager-master01  created SCC...

- You can use the describe pod pod-name command to further narrow the results to a single pod. 
  For example, to retrieve only the events that relate to a mysql pod, you can refer to the Events field from the output of the oc describe pod mysql command:

[user@host~]$ oc describe pod mysql
...output omitted...
Events:
  FirstSeen   LastSeen    Count From         Reason          Message
  Wed, 10 ... Wed, 10 ... 1     {scheduler } scheduled       Successfully as...
...output omitted...

# Kubernetes Alerts
- RHOCP includes a monitoring stack, which is based on the Prometheus open source project. 
  The monitoring stack is configured to monitor the core RHOCP cluster components, by default. 
  You can optionally configure the monitoring stack also to monitor user projects.

- The components of the monitoring stack are installed in the openshift-monitoring namespace. 
  The Prometheus Operator in the openshift-monitoring namespace creates, configures, and manages platform Prometheus and Alertmanager instances. 
  An Alertmanager pod in the openshift-monitoring namespace receives alerts from Prometheus. 
  Alertmanager can also send alerts to external notification systems.

- Use the following get all command to display a list of all resources, their status, and their types in the openshift-monitoring namespace.

[user@host~]$ oc get all -n openshift-monitoring --show-kind
NAME                                              READY  STATUS   RESTARTS AGE
pod/alertmanager-main-0                           6/6    Running  85       34d
pod/cluster-monitoring-operator-56b769b58f-dtmqj  2/2    Running  34       35d
pod/kube-state-metrics-75455b796c-8q28d           3/3    Running  51       35d
...output omitted...

- The alertmanager-main-0 pod is the Alertmanager for the cluster. 
  The following logs command shows the logs of the alertmanager-main-0 pod, which displays the received messages from Prometheus.

[user@host~]$ oc logs alertmanager-main-0 -n openshift-monitoring
ts=2023-03-16T14:21:50.479Z caller=main.go:231 level=info msg="Starting Alertmanager" version="(version=0.24.0, branch=rhaos-4.14-rhel-8, revision=519cbb87494d2830821a0da0a657af69d852c93b)"
ts=2023-03-16T14:21:50.479Z caller=main.go:232 level=info build_context="(go=go1.19.4, user=root@232132c11c68, date=20230105-00:26:49)"
ts=2023-03-16T14:21:50.527Z caller=coordinator.go:113 level=info component=configuration msg="Loading configuration file" file=/etc/alertmanager/config_out/alertmanager.env.yaml
...output omitted...

# Check Node Status
- RHOCP clusters can have several components, including at least one control plane and at least one compute node. 
  The two components can occupy a single node. 
  The following oc command, or the matching kubectl command, can display the overall health of all cluster nodes.

[user@host~]$ oc cluster-info

- The oc cluster-info output is high-level, and can verify that the cluster nodes are running. 
  For a more detailed view into the cluster nodes, use the get nodes command.

[user@host~]$ oc get nodes
NAME       STATUS   ROLES                         AGE   VERSION
master01   Ready    control-plane,master,worker   35d   v1.27.6+f67aeb3

- The example shows a single master01 node with multiple roles. 
  The STATUS value of Ready means that this node is healthy and can accept new pods. 
  A STATUS value of NotReady means that a condition triggered the NotReady status and the node is not accepting new pods.

- As with any other RHOCP resource, you can drill down into further details of the node resource with the describe node node-name command. 
  For parsable output of the same information, use the -o json or the -o yaml output options with the get node node-name command.

- The output of the get nodes node-name command with the -o json or -o yaml option is long. 
  The following examples use the -jsonpath option or the jq processor to parse the get node node-name command output.

  [user@host~]$ oc get node master01 -o jsonpath=\
*'{"Allocatable:\n"}{.status.allocatable}{"\n\n"}
{"Capacity:\n"}{.status.capacity}{"\n"}'

Allocatable:
{"cpu":"7500m","ephemeral-storage":"114396791822","hugepages-1Gi":"0",
"hugepages-2Mi":"0","memory":"19380692Ki","pods":"250"}

Capacity:
{"cpu":"8","ephemeral-storage":"125293548Ki","hugepages-1Gi":"0",
"hugepages-2Mi":"0","memory":"20531668Ki","pods":"250"}

- The JSONPath expression in the previous command extracts the allocatable and capacity measures for the master01 node. 
  These measures help to understand the available resources on a node.

- View the status object of a node to understand the current health of the node.

[user@host~]$ oc get node master01 -o json | jq '.status.conditions'
[
  {
    "lastHeartbeatTime": "2023-03-22T16:34:57Z",
    "lastTransitionTime": "2023-02-23T20:35:15Z",
    "message": "kubelet has sufficient memory available",
    "reason": "KubeletHasSufficientMemory",
    "status": "False",
    "type": "MemoryPressure"      1 : 	If the status of the MemoryPressure condition is true, then the node is low on memory.
  },
  {
    "lastHeartbeatTime": "2023-03-22T16:34:57Z",
    "lastTransitionTime": "2023-02-23T20:35:15Z",
    "message": "kubelet has no disk pressure",
    "reason": "KubeletHasNoDiskPressure",
    "status": "False",
    "type": "DiskPressure"     2: If the status of the DiskPressure condition is true, then the disk capacity of the node is low.
  },
  {
    "lastHeartbeatTime": "2023-03-22T16:34:57Z",
    "lastTransitionTime": "2023-02-23T20:35:15Z",
    "message": "kubelet has sufficient PID available",
    "reason": "KubeletHasSufficientPID",
    "status": "False",
    "type": "PIDPressure"     3: If the status of the PIDPressure condition is true, then too many processes are running on the node.
  },
  {
    "lastHeartbeatTime": "2023-03-22T16:34:57Z",
    "lastTransitionTime": "2023-02-23T20:35:15Z",
    "message": "kubelet is posting ready status",
    "reason": "KubeletReady",
    "status": "True",
    "type": "Ready"          4: If the status of the Ready condition is false, then the node is not healthy and is not accepting pods.
  }
]

# Check Pod Status
- With RHOCP, you can view logs in running containers and pods to ease troubleshooting. 
- When a container starts, RHOCP redirects the container's standard output and standard error to a disk in the container's ephemeral storage. 
  With this redirect, you can view the container logs by using logs commands, even after the container stops. 
  However, the pod hosting the container must still exist.

- In RHOCP, the following command returns the output for a container within a pod:
[user@host~]$ oc logs <pod-name> -c <container-name>

Replace pod-name with the name of the target pod, and replace container-name with the name of the target container. 
The -c container-name argument is optional, if the pod has only one container. 
You must use the -c container-name argument to connect to a specific container in a multicontainer pod. 
Otherwise, the command defaults to the only running container and returns the output.

- When debugging images and setup problems, it is useful to get an exact copy of a running pod configuration, and then troubleshoot it with a shell. 
  If a pod is failing or does not include a shell, then the rsh and exec commands might not work. 
  To resolve this issue, the debug command creates a copy of the specified pod and starts a shell in that pod.

- By default, the debug command starts a shell inside the first container of the referenced pod. The debug pod is a copy of your source pod, with some additional modifications. For example, the pod labels are removed. The executed command is also changed to the '/bin/sh' command for Linux containers, or the 'cmd.exe' executable for Windows containers. Additionally, readiness and liveness probes are disabled.

- A common problem for containers in pods is security policies that prohibit a container from running as a root user. You can use the debug command to test running a pod as a non-root user by using the --as-user option. You can also run a non-root pod as the root user with the --as-root option.

- With the debug command, you can invoke other types of objects besides pods. For example, you can use any controller resource that creates a pod, such as a deployment, a build, or a job. The debug command also works with nodes, and with resources that can create pods, such as image stream tags. You can also use the --image=IMAGE option of the debug command to start a shell session by using a specified image.

If you do not include a resource type and name, then the debug command starts a shell session into a pod by using the OpenShift tools image.

[user@host~]$ oc debug

The next example tests running a job pod as a non-root user.

[user@host~]$ oc debug job/test --as-user=1000000
The following example creates a debug session for a node.

[user@host~]$ oc debug node/master01
Starting pod/master01-debug-wtn9r ...
To use host binaries, run chroot /host
Pod IP: 192.168.50.10
If you don't see a command prompt, try pressing enter.
sh-4.4# chroot /host
sh-5.1#

- The debug pod is deleted when the remote command completes, or when the user interrupts the shell.

# Collect Information for Support Requests
When opening a support case, it is helpful to provide debugging information about your cluster to Red Hat Support. It is recommended that you provide the following information:

Data gathered by using the oc adm must-gather command as a cluster administrator

The unique cluster ID

The oc adm must-gather command collects resource definitions and service logs from your cluster that are most likely needed for debugging issues. This command creates a pod in a temporary namespace on your cluster, and the pod then gathers and downloads debugging information. By default, the oc adm must-gather command uses the default plug-in image, and writes into the ./must-gather.local. directory on your local system. To write to a specific local directory, you can also use the --dest-dir option, such as in the following example:

1. [user@host~]$ oc adm must-gather --dest-dir ~/must-gather

$ ls ~/must-gather/
event-filter.html  must-gather.logs  quay-io-openshift-release-dev-ocp-v4-0-art-dev-sha256-138b9ff842768869dc7bc766a09df8a54fdd77a71c37290226e2cb6a30c99d24  timestamp
[amaseghe@sexy-guy openshift-local]$ ls -al ~/must-gather/
total 1064
drwxr-xr-x.  3 amaseghe amaseghe   4096 Aug 26 20:09 .
drwx-----x. 21 amaseghe amaseghe   4096 Aug 26 20:08 ..
-rw-r--r--.  1 amaseghe amaseghe 517549 Aug 26 20:09 event-filter.html
-rw-r--r--.  1 amaseghe amaseghe 550816 Aug 26 20:09 must-gather.logs
drwxrwxrwx. 14 amaseghe amaseghe   4096 Aug 26 20:09 quay-io-openshift-release-dev-ocp-v4-0-art-dev-sha256-138b9ff842768869dc7bc766a09df8a54fdd77a71c37290226e2cb6a30c99d24
-rw-r--r--.  1 amaseghe amaseghe    113 Aug 26 20:09 timestamp


2. Then, create a compressed archive file from the must-gather directory. For example, on a Linux-based system, you can run the following command:

[user@host~]$ tar cvaf mustgather.tar must-gather/
Replace must-gather/ with the actual directory path.

3. Then, attach the compressed archive file to your support case in the Red Hat Customer Portal.

Similar to the oc adm must-gather command, the oc adm inspect command gathers information on a specified resource. For example, the following command collects debugging data for the openshift-apiserver and kube-apiserver cluster operators.

[user@host~]$ oc adm inspect clusteroperator/openshift-apiserver \
clusteroperator/kube-apiserver
The oc adm inspect command can also use the --dest-dir option to specify a local directory to write the gathered information. The command shows all logs by default. Use the --since option to filter the results to logs that are later than a relative duration, such as 5s, 2m, or 3h.

[user@host~]$ oc adm inspect clusteroperator/openshift-apiserver --since 10m

# Summary of commands
Create the cli-review project. $ oc new-project cli-review 

Identify the cluster version.  $ oc version

Identify the supported API versions. $ oc api-versions

dentify the fields for the pod.spec.securityContext object. : $ oc explain pod.spec.securityContext

List the cluster operators. $ oc get clusteroperators

Identify the available namespaced resources. $ oc api-resources --namespaced

Identify the resources that belong to the core API group. $ oc api-resources --api-group ''

List the resource types that the oauth.openshift.io API group provides. $ oc api-resources --api-group oauth.openshift.io

List the events in the openshift-kube-controller-manager namespace. $ oc get events -n openshift-kube-controller-manager

Retrieve the conditions status of the etcd-master01 pod in the openshift-etcd namespace by using jq filters to limit the output. $ oc get pods etcd-master01 -n openshift-etcd \
  -o json | jq .status.conditions

List the compute resource usage of the containers in the etcd-master01 pod in the openshift-etcd namespace. $ oc adm top pods etcd-master01 -n openshift-etcd --containers

Get the number of allocatable pods for the master01 node by using a JSONPath filter. $ oc get node master01   -o jsonpath='{.status.allocatable.pods}{"\n"}'

List the memory and CPU usage of all pods in the cluster. $ oc adm top pods -A --sum

Retrieve the compute resource consumption of the master01 node.$ oc adm top node

Retrieve the capacity and allocatable CPU for the master01 node by using a JSONPath filter. $ oc get node master01 -o jsonpath=\
'Allocatable: {.status.allocatable.cpu}{"\n"}'\
'Capacity: {.status.capacity.cpu}{"\n"}'

Retrieve debugging information for the cluster. Save the output to the /home/student/DO180/labs/cli-review/debugging directory.: $ oc adm must-gather \
  --dest-dir /home/student/DO180/labs/cli-review/debugging

Generate debugging information for the kube-apiserver cluster operator. Save the output to the /home/student/DO180/labs/cli-review/inspect directory, and limit the debugging information to the last five minutes. : $ oc adm inspect clusteroperator kube-apiserver \
  --dest-dir /home/student/DO180/labs/cli-review/inspect --since 5m