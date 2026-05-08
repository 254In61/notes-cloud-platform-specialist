# Overview
- Podman is an open source tool that you can use to manage your containers locally. 
  With Podman, you can find, run, build or deploy OCI (Open Container Initiative) containers and container images.

- By default, Podman is daemonless. 
  A daemon is a process that is always running and ready for receiving incoming requests. 
  Some other container tools use a daemon to proxy the requests, which brings a single point of failure. 
  In addition, a daemon might require elevated privileges, which is a security concern. 
  Podman interacts directly with containers, images, and registries without a daemon.

- Podman comes in the form of a command-line interface (CLI), which is supported for several operating systems. 
  Along with the CLI, Podman provides two additional ways to interact with your containers and automate processes, the RESTful API and a desktop application called Podman Desktop.

# Pulling and displaying images
- A container is an isolated runtime environment where applications are executed as isolated processes. 
  The isolation of the runtime environment ensures that they do not interrupt other containers or system processes.

- A container image contains a packaged version of your application, with all the dependencies necessary for the application to run. 
  Images can exist without containers, but containers are dependent of images because containers use container images to build a runtime environment to execute applications.

     $ podman pull registry.redhat.io/rhel7/rhel:7.9 : pulls images from registry
  
  - After the execution of the pull command, the image is stored locally in your system. 
    You can list the images in your system by using the podman images command.
    $ podman images : Lists the images

# Running and Displaying Containers
- With the image stored in your local system, you can use the podman run command to create a new container that uses the image. 
- The RHEL image from previous examples accepts Bash commands as an argument. 
  These commands are provided as an argument and are executed within a RHEL container.

    [user@host ~]$ podman run registry.redhat.io/rhel7/rhel:7.9 echo 'Red Hat'
    Red Hat

- In the previous example, the echo 'Red Hat' command is provided as an argument to the podman run command. 
  Podman executes the echo command inside the RHEL container and displays the output of the command.

- If you run a container from an image that is not stored in your system then Podman tries to pull the image before running the container.   Therefore, it is not necessary to execute the pull command first.

- You can list the running containers by using the $ podman ps command.

[user@host ~]$ podman ps
CONTAINER ID  IMAGE       COMMAND     CREATED     STATUS      PORTS       NAMES

- By default, the podman ps command lists the following details for your containers:

1. the container's ID
2. the name of the image that the container is using
3. the command that the container is executing
4. the time that the container was created
5. the status of the container
6. the exposed ports in the container
7. the name of the container.

# Container lifecycle : Keep it running? Stop? Remove?
- When the container finishes the execution of echo, the container is stopped because no other process keeps it running. 

- You can start a continously running container with certain commands or options. For example :

  1. You can run the container with an interactive shell that keeps it running.
     
     $ podman run --name sexy -dit ubuntu

       This command will start the Ubuntu container and keep it running.
        -d: Runs the container in detached mode (in the background).
        -i: Keeps STDIN open to keep the container running.
        -t: Allocates a pseudo-TTY, allowing you to interact with the container.
  
  2. start a continuous container in Podman using Ubuntu with a sleep command.
     
     $ podman run --name ubuntu666 -d ubuntu sleep infinity
     
     This command will:
      -d: Run the container in detached mode (in the background).
      ubuntu: Use the Ubuntu image.
      sleep infinity: Make the container run indefinitely using the sleep command, preventing it from exiting.

- Checking the running containers you see the command that the container is executing.

  $ podman ps
CONTAINER ID  IMAGE                            COMMAND         CREATED        STATUS            PORTS       NAMES
f0014a8481a1  docker.io/library/ubuntu:latest  /bin/bash       5 minutes ago  Up 5 minutes ago              nostalgic_lalande
725ef17d4d7e  docker.io/library/ubuntu:latest  sleep infinity  3 seconds ago  Up 3 seconds ago              modest_jackson

- However, stopping a container is not the same as removing a container. 
  Although the container is stopped, Podman does not remove it. 
  You can list all containers (running and stopped) by adding the --all flag to the podman ps command.

 ** Check running containers

amaseghe@the-eagle:~$ podman ps
CONTAINER ID  IMAGE                            COMMAND         CREATED         STATUS             PORTS       NAMES
f0014a8481a1  docker.io/library/ubuntu:latest  /bin/bash       40 minutes ago  Up 40 minutes ago              nostalgic_lalande
725ef17d4d7e  docker.io/library/ubuntu:latest  sleep infinity  34 minutes ago  Up 34 minutes ago              modest_jackson

** But list all containers

amaseghe@the-eagle:~$ podman ps --all
CONTAINER ID  IMAGE                            COMMAND               CREATED         STATUS                    PORTS                   NAMES
f0014a8481a1  docker.io/library/ubuntu:latest  /bin/bash             41 minutes ago  Up 41 minutes ago                                 nostalgic_lalande
725ef17d4d7e  docker.io/library/ubuntu:latest  sleep infinity        36 minutes ago  Up 36 minutes ago                                 modest_jackson
0eeefbcca8a6  docker.io/library/nginx:latest   nginx -g daemon o...  7 minutes ago   Created                   0.0.0.0:8080->8080/tcp  nostalgic_lamarr
e576ff29d257  docker.io/library/nginx:latest   nginx -g daemon o...  6 minutes ago   Exited (0) 2 minutes ago  0.0.0.0:8088->8088/tcp  flamboyant_payne


- You can also automatically remove a container when it exits by adding the --rm option to the podman run command.

  [user@host ~]$ podman run --rm registry.redhat.io/rhel7/rhel:7.9 echo 'Red Hat'
Red Hat
[user@host ~]$ podman ps --all
CONTAINER ID  IMAGE                              COMMAND       CREATED       STATUS                   PORTS       NAMES

# Identifying containers
- If a name is not provided during the creation of a container, then Podman generates a random string name for the container. 
  It is important to define a unique name to facilitate the identification of your containers when managing their lifecycle.

  You can assign a name to your containers by adding the --name flag to the podman run command.

- Podman can identify the containers either by the Universal Unique Identifier (UUID) short identifier, which is composed of twelve alphanumeric characters, or by the UUID long identifier, which is composed of 64 alphanumeric characters, as shown in the example.

amaseghe@the-eagle:~$ podman ps --all
CONTAINER ID  IMAGE                            COMMAND         CREATED         STATUS             PORTS       NAMES
f0014a8481a1  docker.io/library/ubuntu:latest  /bin/bash       18 minutes ago  Up 18 minutes ago              nostalgic_lalande
725ef17d4d7e  docker.io/library/ubuntu:latest  sleep infinity  13 minutes ago  Up 13 minutes ago              modest_jackson

In the above example, f0014a8481a1/725ef17d4d7e  are the containers' ID, or UUID short identifier. 
Additionally, nostalgic_lalande/modest_jackson are listed as the container's name.

- If you want to retrieve the UUID long container ID, then you can add the --format=json flag to the podman ps --all command.

amaseghe@the-eagle:~$ podman ps --all --format=json
[
  {
    "AutoRemove": false,
    "Command": [
      "/bin/bash"
    ],
    "CreatedAt": "19 minutes ago",
    "Exited": false,
    "ExitedAt": -62135596800,
    "ExitCode": 0,
    "Id": "f0014a8481a1ba1b2a2531e6aef717fb905c43036a008583df0dfd18df4fadaf",      #  UUID long container ID
    "Image": "docker.io/library/ubuntu:latest",
    "ImageID": "edbfe74c41f8a3501ce542e137cf28ea04dd03e6df8c9d66519b6ad761c2598a",
    "IsInfra": false,
    "Labels": {
      "org.opencontainers.image.ref.name": "ubuntu",
      "org.opencontainers.image.version": "24.04"
    },
    "Mounts": [],
    "Names": [
      "nostalgic_lalande"
    ],
    "Namespaces": {

    },
    "Networks": null,
    "Pid": 1049738,
    "Pod": "",
    "PodName": "",
    "Ports": null,
    "Size": null,
    "StartedAt": 1726445628,
    "State": "running",
    "Status": "Up 19 minutes ago",
    "Created": 1726445628
  },
  {
    "AutoRemove": false,
    "Command": [
      "sleep",
      "infinity"
    ],
    "CreatedAt": "13 minutes ago",
    "Exited": false,
    "ExitedAt": -62135596800,
    "ExitCode": 0,
    "Id": "725ef17d4d7e6bba92cb726de869a17e9752e67861ba8744dba688c82517a875",               #  UUID long container ID
    "Image": "docker.io/library/ubuntu:latest",
    "ImageID": "edbfe74c41f8a3501ce542e137cf28ea04dd03e6df8c9d66519b6ad761c2598a",
    "IsInfra": false,
    "Labels": {
      "org.opencontainers.image.ref.name": "ubuntu",
      "org.opencontainers.image.version": "24.04"
    },
    "Mounts": [],
    "Names": [
      "modest_jackson"
    ],
    "Namespaces": {

    },
    "Networks": null,
    "Pid": 1060900,
    "Pod": "",
    "PodName": "",
    "Ports": null,
    "Size": null,
    "StartedAt": 1726445962,
    "State": "running",
    "Status": "Up 13 minutes ago",
    "Created": 1726445962
  }
]
amaseghe@the-eagle:~$

# Exposing containers
- Many applications, such as web servers or databases, keep running indefinitely waiting for connections. 
  Therefore, the containers for these applications must run indefinitely. 
  At the same time, it is usually necessary for these applications to be accessed externally through a network protocol.

- You can use the -p option to map a port in your local machine to a port inside the container. 
  This way, the traffic in your local port is forwarded to the port inside the container, thus, allowing you to access the application from your computer.

- The following example creates a new container that runs an Nginx HTTP server by mapping the 8088 port in your local machine to the 8088 port inside the container.
 
  amaseghe@the-eagle:~$ podman run -p 8088:8088 docker.io/nginx

- You can access the HTTP server at localhost:8080.

- If you want the container to run in the background, to avoid the terminal being blocked, then you can use the -d option.

# Using Environment Variables
- Environment variables are variables used in your applications that are set outside of the program. The operating system or the environment where the application runs provides the value of the variable. 

- You can access the environment variable in your application at runtime. For example, in Node.js, you can access environment variables by using process.env.VARIABLE_NAME.

- Environment variables are a useful and safe way of injecting environment-specific configuration values into your application. For example, your application might use a database hostname that is different for each application environment, such as the database.local, database.stage, or database.test hostnames.

- You can pass environment variables to a container by using the -e option. In the following example, an environment variable called NAME with the value Red Hat is passed. Then, the environment variable is printed by using the printenv command inside the container.

[user@host ~]$ podman run -e NAME='Red Hat' \
 registry.redhat.io/rhel7/rhel:7.9 printenv NAME
Red Hat

# Inspect containers $ podman inspect

- Gives lots of data.
- Narrow down to it by calling the specific fields.
 $ podman inspect sexy-guy
  [
    {
        "Id": "ee35ce357650578e512b2db621054364d6e44ac4544ee01c39749040d2370ebd",
        "Created": "2024-09-18T09:16:44.440767839+10:00",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "OciVersion": "1.0.2-dev",
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 45578,
            "ConmonPid": 45572,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2024-09-18T09:16:44.495604211+10:00",
            "FinishedAt": "0001-01-01T00:00:00Z",
            "Healthcheck": {
                "Status": "",
                "FailingStreak": 0,
                "Log": null
            },
            "CgroupPath": "/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-ee35ce357650578e512b2db621054364d6e44ac4544ee01c39749040d2370ebd.scope"
        },
        !
        !
        !
       ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "user.slice",
            "BlkioWeight": 0,
            "BlkioWeightDevice": null,
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DiskQuota": 0,
            "KernelMemory": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": 0,
            "OomKillDisable": false,
            "PidsLimit": 2048,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "CgroupConf": null
        }
    }
]



amaseghe@black-panther:~$ podman inspect sexy-guy -f '{{.Id}}'
ee35ce357650578e512b2db621054364d6e44ac4544ee01c39749040d2370ebd

amaseghe@black-panther:~$ podman inspect sexy-guy -f '{{.State}}'
{1.0.2-dev running true false false false false 45578 45572 0  2024-09-18 09:16:44.495604211 +1000 AEST 0001-01-01 00:00:00 +0000 UTC { 0 []} false /user.slice/user-1000.slice/user@1000.service/user.slice/libpod-ee35ce357650578e512b2db621054364d6e44ac4544ee01c39749040d2370ebd.scope}

amaseghe@black-panther:~$ 

amaseghe@black-panther:~$ podman inspect sexy-guy -f '{{.State.StartedAt}}'
2024-09-18 09:16:44.495604211 +1000 AEST

amaseghe@black-panther:~$ podman inspect sexy-guy -f '{{.State.CgroupPath}}'
/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-ee35ce357650578e512b2db621054364d6e44ac4544ee01c39749040d2370ebd.scope
amaseghe@black-panther:~$ 

# Accessing containiners 
## Container transparency - The challenge
- Developers commonly package applications as containers to, among other benefits, isolate the application process.
  However, process isolation also means the developers lose immediate visibility into the state of the containerized process and its environment.

- To regain the visibility, containerized tools such as Podman provide a way to start a new process within containers in the running state.
  This is useful for example when you want to read a log file, verify the value of the env variable, or debug a process.

## Container Layers
- Container images are characterized as immutable and layered.Each image layer consists of a set of file system differences, or diffs. 
  A diff signals a file system change from the previous layer, such as adding or modifying a file.

- When you start a container, the container creates a new ephemeral layer over its base container image layers called 'container layer'.
  This layer is the only read/write storage available for the container by default, and it is used for any runtime file system operations, such as creating working files, temporary files, and log files.

- Files that are created in the container layer are considered volatile, which means that the files are deleted when you delete the container. The container layer is exclusive to the running container, so if you create another container from the same base image, then the new container creates another container layer. This ensures that each container's runtime data is isolated from other containers.

Ephemeral container storage is not sufficient for applications that need to keep data beyond the life of the container, such as databases. You can use persistent storage to support such applications. 

