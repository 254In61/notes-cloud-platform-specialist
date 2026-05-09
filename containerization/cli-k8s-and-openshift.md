# overview
- You can manage an OpenShift cluster from the web console or by using the kubectl or oc command-line interfaces (CLI). 
- The kubectl commands are native to K8s, and are a thin wrapper over the K8s API.
- The OpenShift oc (OpenShift cli) commands are a superset of the kubectl commands, and add commands for the OpenShift-specific features. 

# managing resources using oc
- Before you can interact with your RHOCP cluster, you must authenticate your requests. 

- $ cluster-info 
   - prints the address of the control plane and other cluster services.

- $ oc api-versions 
   - prints the supported API versions on the server, in the form of "group/version".

- $ oc get clusteroperator
   - The cluster operators that Red Hat ships serve as the architectural foundation for RHOCP. 
   - RHOCP installs cluster operators by default. 
   - Use the oc get clusteroperator command to see a list of the cluster operators:

- $ oc get
   - Use the get command to retrieve information about resources in the selected project. 

- $ oc get all 
   - command to retrieve a summary of the most important components of a cluster.

- $ oc describe <resource> 
  - If the summaries from the get command are insufficient, this one comes in handy to retrieve additional information. 

- $ oc create
  - Use the create command to create a RHOCP resource in the current project. 
  - This command creates resources from a resource definition. 
  - Typically, this command is paired with the oc get RESOURCE_TYPE RESOURCE_NAME -o yaml command for editing definitions. 
  - Developers commonly use the -f flag to indicate the file that contains the JSON or YAML representation of an RHOCP resource.

- $ oc status
  - The oc status command provides a high-level overview of the current project. 
  - The command shows services, deployments, build configurations, and active deployments. 
  - Information about any misconfigured components is also shown. 
  - The --suggest option shows additional details for any identified issues.

- $ oc delete
  -  Use the delete command to delete an existing RHOCP resource from the current project. You must specify the resource type and the resource name.
  - For example, to delete the quotes-ui pod, use the following command:$ oc delete pod quotes-ui
  - deleting managed resources, such as pods, results in the automatic creation of new instances of those resources. When a project is deleted, it deletes all the resources and applications within it.
  - Each of these commands is executed in the current selected project. To execute commands in a different project, you must include the --namespace or -n options.