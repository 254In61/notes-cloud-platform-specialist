# Kubernetes and OpenShift Resources
- Kubernetes uses API resource objects to represent the intended state of everything in the cluster. 
- All administrative tasks require creating, viewing, and changing the API resources. 
- Use the $ oc api-resources command to view the Kubernetes resources.
- The SHORTNAME for a component helps to minimize typing long CLI commands. For example, you can use oc get cm instead of oc get configmaps.
** Some resources can only be listed using a super-admin, like kubeadmin in openshift local.
- The APIVERSION column divides the objects into API groups. The column uses the <API-Group>/<API-Version> format. The API-Group object is blank for Kubernetes core resource objects.
- The APIVERSION column divides the objects into API groups. The column uses the <API-Group>/<API-Version> format. The API-Group object is blank for Kubernetes core resource objects.
- The KIND is the formal Kubernetes resource schema type.

# Filter outputs
- The $ oc api-resources command can further filter the output with options that operate on the data.
- Examples:
  - --namespaced=true : If false, return non-namespaced resources, otherwise return namespaced resources
  - --api-group apps  : Limit to resources in the specified API group. Use --api-group='' to show core resources.
  - --sort-by name	: If non-empty, sort list of resources using specified field. The field can be either 'name' or 'kind'.

- For example, use the following oc api-resources command to see all the namespaced resources in the apps API group, sorted by name.

 $ oc api-resources --namespaced=true --api-group apps
NAME                  SHORTNAMES   APIVERSION   NAMESPACED   KIND
controllerrevisions                apps/v1      true         ControllerRevision
daemonsets            ds           apps/v1      true         DaemonSet
deployments           deploy       apps/v1      true         Deployment
replicasets           rs           apps/v1      true         ReplicaSet
statefulsets          sts          apps/v1      true         StatefulSet

# oc explain
- Each resource contains fields that identify the resource or that describe the intended configuration of the resource. 
- Use the $ oc explain command to get information about valid fields for an object. 
- Examples:
  $ oc explain role
  $ oc explain pod
  $ oc explain route
- Every Kubernetes resource contains the kind, apiVersion, spec, and status fields. However, when you create an object definition, you do not need to provide the status field. 

- Instead, Kubernetes generates the status field, and it lists information such as runtime status and readiness. The status field is useful for troubleshooting an error or for verifying the current state of a resource.

- You can use the YAML path to a field and dot-notation to get information about a particular field.
  $ oc explain pod.spec
  $ oc explain route.status

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

# resources added by OpenShift
Red Hat OpenShift Container Platform (RHOCP) adds the following main resource types to Kubernetes:

1. BuildConfig (bc)
Defines a process to execute in the OpenShift project. The OpenShift Source-to-Image (S2I) feature uses a BuildConfig to build a container image from application source code that is stored in a Git repository. A bc works together with a dc to provide an extensible continuous integration and continuous delivery workflows.

2. DeploymentConfig (dc)
OpenShift 4.5 introduced the Deployment resource concept to replace the DeploymentConfig default configuration for pods. Both concepts represent a set of containers that are included in a pod, and the deployment strategies to use.

3. Routes
Represent a DNS hostname that the OpenShift router recognizes as an ingress point for applications and microservices.

# Structure of resources
- Resources in Kubernetes consist of multiple objects. These objects define the intended state of a resource. When you create or modify an object, you make a persistent record of the intended state. Kubernetes reads the object and modifies the current state accordingly.

- All RHOCP and Kubernetes objects can be represented as a JSON or YAML structure.

- Almost every K8s object includes two nested object fields that govern the object's configuration: the object spec and the object status.

- The spec object describes the intended state of the resource, and the status object describes the current state. 

 $ cat nginx-storage.yaml 
apiVersion: v1                           * Identifier of the object schema version.
kind: Pod                                * Schema identifier.In this example, the object conforms to the pod schema.
metadata:                                * Metadata for a given resource, such as annotations, labels, name, and namespace.
  name: nginx-pv-volume                  * Creates a label with a name key that other resources in Kubernetes can use to find it.
  namespace: nginx-prjoject              * The namespace, or the RHOCP project where the resource is. 
  labels:                                * Key-value pairs that can connect identifying metadata with Kubernetes objects.
    name: wildfly                        * Creates a label with a name key that other resources in Kubernetes, usually a service, can use to find it.
spec:                                    * Defines the pod object configuration, or the intended state of the resource.
  containers:
    - resources:
        limits:
          cpu: 0.5
      image: quay.io/example/todojee:v1  * Defines the container image name.
      name: wildfly                      * Name of the container inside a pod. Container names are important for oc commands when a pod contains multiple containers.
      ports:
        - containerPort: 8080            * A container-dependent attribute to identify the port that the container uses.
          name: wildfly
      env:                               * Defines a collection of environment variables.
        - name: MYSQL_DATABASE
          value: items
        - name: MYSQL_USER
          value: user1
        - name: MYSQL_PASSWORD
          value: mypa55
...object omitted...
status:                                 * Current state of the object. K8s provides this field, which lists info such as runtime status, readiness, and container images.
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-08-19T12:59:22Z"
    status: "True"
    type: PodScheduled     
---

- You specify the spec section of the resource when you create the object. Kubernetes controllers continuously update the status of the object throughout the existence of the object. The Kubernetes control plane continuously and actively manages every object's actual state to match the desired state you supplied.

- For example, in Kubernetes, a Deployment object can represent an application that is running on your cluster. When you create a Deployment object, you might configure the deployment spec object to specify that you want three replicas of the application to be running. Kubernetes reads the deployment spec object and starts three instances of your chosen application, and updates the status field to match your spec object. If any of those instances fails, then Kubernetes responds to the difference between the spec and status objects by making a correction, in this case to start a replacement instance.

# labels
- Labels are key-value pairs that you define in the .metadata.labels object path, for example:

kind: Pod
apiVersion: v1
metadata:
  name: example-pod
  labels:
    app: example-pod
    group: developers
...object omitted...

- The preceding example contains the app=example-pod and group=developers labels. 
  Developers often use labels to target a set of objects by using the -l or the --selector option. 
  For example, the following oc get command lists pods that contain the group=developers label:

  $ oc get pod --selector group=developers
   NAME                          READY   STATUS    RESTARTS   AGE
   example-pod-6c9f758574-7fhg   1/1     Running   5          11d

