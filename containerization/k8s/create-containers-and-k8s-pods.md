# Creating Containers and Pods - oc/kubectl run
- Kubernetes and OpenShift offer many ways to create containers in pods. 
- You can use one such way, the run command, with the kubectl or oc CLI to create and deploy an application in a pod from a container image. 

  $ oc run web-server --image registry.access.redhat.com/ubi8/httpd-24

- Check created pod:
  $ oc get pod web-server

# -- command
- You can use several options and flags with the run command. 
- The --command option executes a custom command and its arguments in a container, rather than the default command that is defined in the container image. 
- You must follow the --command option with a double dash (--) to separate the custom command and its arguments from the run command options. 

  $ oc run RESOURCE/NAME --image IMAGE --command -- cmd arg1 ... argN
  
  Example:
  [user@host ~]$ oc run -it my-app --image registry.access.redhat.com/ubi9/ubi --command -- /bin/bash
  If you don't see a command prompt, try pressing enter.
  bash-5.1$

# restart policy
- You can also define a restart policy for containers in a pod by including the --restart option. 
  A pod restart policy determines how the cluster should respond when containers in that pod exit. 
  The --restart option has the following accepted values: Always, OnFailure, and Never.

- Always : 
  If the restart policy is set to Always, then the cluster continuously tries to restart a successfully exited container, for up to five minutes. 
  The default pod restart policy is Always. 
  If the --restart option is omitted, then the pod is configured with the Always policy.

- OnFailure:
  Setting the pod restart policy to OnFailure tells the cluster to restart only failed containers in the pod, for up to five minutes.

- Never
  If the restart policy is set to Never, then the cluster does not try to restart exited or failed containers in a pod. 
  Instead, the pods immediately fail and exit.

  The following example command executes the date command in the container of the pod named my-app, redirects the date command output to the terminal, and defines Never as the pod restart policy.

  [user@host ~]$ oc run -it my-app --image registry.access.redhat.com/ubi9/ubi --restart Never --command -- date
  Mon Feb 20 22:36:55 UTC 2023


  To automatically delete a pod after it exits, include the --rm option with the run command.
  
  [user@host ~]$ kubectl/oc run -it my-app --rm --image registry.access.redhat.com/ubi9/ubi --restart Never --command -- date
  Mon Feb 20 22:38:50 UTC 2023
  pod "date" deleted

