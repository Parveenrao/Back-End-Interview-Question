""" 

=> HostPath 

   -> A hostpath volume mounts a directory or file from the worker node filesystem into a pod

   -> instead of kubernetes creating a new storage area  , it uses an existing path on node 


Worker Node
┌────────────────────────────┐
│                            │
│ /data/logs                 │
│     │                      │
│     └──────────────┐       │
│                    │       │
└────────────────────┼───────┘
                     │
                     ▼
               Pod Container
           /app/logs (mounted)




     -> The container now read and write directly to /data/logs on the node 


=> Why do we need hostpath

   -> Sometime an application needs access to files that already exist on the node.

   -> Read docker / container runtime logs

   -> access system configuration files 

   -> access devices files

   -> read kubernetes logs for monitoring



=> 

Worker Node

/var/log/syslog
        │
        ▼
hostPath
        │
        ▼
Container

/logs/syslog


Now the container can access the host's logs.


=> working 

    1. suppose the worker node has 

       worker node 

       /data

       file1.txt 
       file2.txt

   2. Kubernetes mount the /data  into the container

      worker node /data -> container /app/data


   3. inside the container 

       ls /app/data



=> What if container restarts

    container crash -> Restart -> hostpath still mounted -> data remains


=> what if pod is deleted 

   -> Pod is removed , but the node's filesystem is unchanged

      Pod deleted -> /data still exist -> new pod can mount it again


=> What if pod moved to another node 

    1. Imagine 

       Worker Node 1

          /data

          pod is scheduled on Node 1

          everything works

          later kubernetes rescheduled the pod

          worker node 2

    2. Node 2 has

       /data

       may be it is empty or does not exist 


       -> application may 

           1. loose access to the expected data 
           2. fail to start
           3. see different files


=> Hostpath types 


   1. Directory  -> directory must exist 

   2. DirectoryorCreate -> create the directory if it does not exist 

   3. File -> File must already exist 

   4. Fileorcreate -> create the file if it not exist 



"""