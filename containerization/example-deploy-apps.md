# What is needed?


=> All this is done using .yaml files.
=> You define everything on .yaml files then "$ kubectl apply -f <.yml file>"

# Steps to Deploy mysql

1. Define Persistent Volume:
   - Define the PV to be created in the .yaml file.
   - Define the PV claim in a .yaml file. This is resposible for claiming the allocated PV above.
   - These are defined in mysql-storage.yaml

     $ kubectl apply -f mysql-storage.yaml
       persistentvolume/mysql-pv-volume created
       persistentvolumeclaim/mysql-pv-claim created
   - PV will be defined under Cluster
   - PV claim is found under Config & Storage

   Want to delete a PV?

   // Delete the associated pvc first.
   $ kubectl get persistentvolumeclaims // Lists all persistent pvc
   $ kubectl delete -n default persistentvolumeclaim <pvc-claim>

   // Delete the PV next
   $ kubectl get persistentvolumes // Lists all persistent volumes.
   $ kubectl delete persistentvolume <pv name>

2. Secret : DB needs credentials to access, right?
   - Define the secret to be deployed in a .yaml file.
   - Apply the changes.

     $ kubectl apply -f mysql-secret.yaml 
       secret/mysql-secret created

   - Secret is defined under Config and Storage


3. Deploy the DB and then expose it to the outside world as K8s service.
   - Define the deployment and service in a .yml file.
   - Apply the changes
  
     $ kubectl apply -f mysql-deployment.yaml
       deployment.apps/mysql created
       service/mysql created

  Delete deployment?

  $ kubectl get deployments # Lists all the deployments
  $ kubectl delete -n default deployment <deployment name>
  ** default = Name space

# Confirmation & access to MySQL instance

1. List pods
 $ kubectl get pod
   NAME                     READY   STATUS    RESTARTS      AGE
   mysql-85d5bb8d57-9ng7v   1/1     Running   0             47m
   nginx-7854ff8877-jdqjv   1/1     Running   1 (11h ago)   27h

 Deleting a pod?:
 $ kubectl get pods  # Lists all your pods.
 $ kubectl delete -n default pod <pod name>
  ** default = Name space

2. Get a shell for the pod by executing the following command:
 $ kubectl exec --stdin --tty <pod name> -- /bin/bash

 $ kubectl exec --stdin --tty mysql-85d5bb8d57-9ng7v -- /bin/bash
   bash-4.4#

3. access the MySQL shell and type in the password created when building the secret using mysql-secret.yml.
  ** So, how does one store this password securely??**

bash-4.4# mysql -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.3.0 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> 

# Update Your MySQL Deployment

To update any part of the deployment, all you need to do is edit the relevant YAML file with the updates followed by applying the changes:

kubectl apply -f <.yaml file>

# Delete Your MySQL Instance


If you intend to remove the entire deployment, use kubectl to delete each of the Kubernetes objects related to it:

kubectl delete deployment,svc mysql
kubectl delete pvc mysql-pv-claim
kubectl delete pv mysql-pv-volume
kubectl delete secret mysql-secret
This series of commands delete the deployment, the service, PV, PVC, and the secret you created. The system confirms the successful deletion