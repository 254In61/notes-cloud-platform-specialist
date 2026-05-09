# Command Outputs
- kubectl/oc provide many output formating options.
- By default, many commands display a small subset of the most useful fields for the given resource type in a tabular output. 
  Many commands support a -o wide option that shows additional fields.

  $ oc get pods : Outputs NAME, READY, STATUS,RESTARTS, AGE
  $	oc get pods -o wide  : The above outputs + IP,NODE, NOMINATED NODE , READINESS GATES

# human readable output : oc describe
- The describe subcommand shows a detailed description of the selected resource and related resources.
- For example, the following command first looks for an exact match on the TYPE object and the NAME-PREFIX object. If no such resource exists, then the command outputs details for every resource of that type with a name with a NAME_PREFIX prefix.
- $ oc describe TYPE NAME-PREFIX
- The describe subcommand provides detailed human-readable output. 
- However, the format of the describe output might change between versions, and thus is not recommended for script development. Any scripts that rely on the output of the describe subcommand might break after a version update.

# YAML output
- The -o yaml option provides a YAML-formatted output that is parsable and still human-readable.
[user@host ~]$ oc get pods -o yaml
apiVersion: v1
items:
  - apiVersion: v1
    kind: Pod
    metadata:
      annotations:
...object omitted...

 $ oc get clusteroperators dns -o yaml
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
...object omitted...


- You can use any tool that can process YAML documents to filter the YAML output for your chosen field. For example, you can use the yq tool at https://mikefarah.gitbook.io/yq/ to process YAML and JSON files.

- The yq processor uses a dot notation to separate field names in a query. The following example pipes the YAML output to the yq command to parse the podIP field.

[user@host ~]$ oc get pods -o yaml | yq r - 'items[0].status.podIP'
10.8.0.60

- The [0] in the example specifies the first index in the items array.

# JSON Output
Kubernetes uses the JSON format internally to process resource objects. Use the -o json option to view a resource in the JSON format.

[user@host ~]$ oc get pods -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {

- You can use other tools to process JSON documents, such as the jq tool at https://jqlang.github.io/jq/. 
  Similar to the yq processor, use the jq processor and dot notation on the fields to query specific information from the JSON-formatted output.

[user@host ~]$ oc get pods -o json | jq '.items[0].status.podIP'
"10.8.0.60"

- Alternatively, the example might have used .items[].status.podIP for the query string. The empty brackets instruct the jq tool to query all items.

# Custom Output
- Kubernetes provides a custom output format that combines the convenience of extracting data via jq styled queries with a tabular output format. Use the -o custom-columns option with comma-separated <column name> : <jq query string> pairs.

[user@host ~]$ oc get pods \
-o custom-columns=PodName:".metadata.name",\
ContainerName:"spec.containers[].name",\
Phase:"status.phase",\
IP:"status.podIP",\
Ports:"spec.containers[].ports[].containerPort"
PodName                  ContainerName   Phase     IP          Ports
myapp-77fb5cd997-xplhz   myapp           Running   10.8.0.60   <none>
Kubernetes also supports the use of JSONPath expressions. JSONPath is a query language for JSON. JSONPath expressions refer to a JSON data structure; they filter and extract formatted fields from JSON objects.

- In the following example, the JSONPath expression uses the range operator to iterate over the list of pods to extract the name of the pod, its IP address, and the assigned ports.

[user@host ~]$ oc get pods  \
-o jsonpath='{range .items[]}{"Pod Name: "}{.metadata.name}
{"IP: "}{.status.podIP}
{"Ports: "}{.spec.containers[].ports[].containerPort}{"\n"}{end}'
Pod Name: myapp-77fb5cd997-xplhz
IP: 10.8.0.60
Ports:

- You can customize the format of the output with Go templates, which the Go programming language uses. Use the -o go-template option followed by a Go template, where Go expressions are inside double braces, {{ }}.

[user@host ~]$ oc get pods  \
-o go-template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}'
myapp-77fb5cd997-xplhz