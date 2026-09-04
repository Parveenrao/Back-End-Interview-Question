""" 

=> Persistent Volumes

    -> Persistent Volume solve the problem of storing data beyond the lifetime of Pod.

    -> Imagine we have a MySQL database running in kubernetes 

          Pod
┌─────────────────┐
│ MySQL           │
│ Database Files  │
└─────────────────┘

    -> Suppose the pod crash

        Pod delete

    -> Kubernetes creates a new pod

          New Pod
┌─────────────────┐
│ MySQL           │
│ Empty Database  │
└─────────────────┘


    -> everything is gone

    -> pod storage is ephemeral

    
=> Problem 

   -> Let say application store 

      1. Customer information 
      2. orders 
      3. Images 
      4. videos 
      5. Logs 
      6. db files


=> Solution

    -> Instead of storing data inside the pod

    -> storing it outside the pod

                        Kubernetes Cluster

        +-----------------------------+
        |                             |
        |     Persistent Volume       |
        |                             |
        +--------------▲--------------+
                       │
                mounted inside
                       │
                +------+------+
                |             |
                |    Pod      |
                |             |
                +-------------+


    -> now if the pods dies

       old pod -> deleted -

       persistent volume -> new pod

    -> New pod mounts the same storage 

    -> No data loss


=> What is Persistent Volume 

    -> A persisent volume is simply a piece of storage in the kubernetes cluster that exist 
       independently of any pod

    -> Think of it as 

       1. SSD
       2. HDD
       3. NFS share 
       4. AWS EBS 
       5. Azure disk 
       6. Google persisten disk


=> characteristics of persistent volumes 

    1. survive pod deletion 
    2. can be resued 
    3. is independent of pods
    4. is managed by kubernetes
    5. can be backed by storage system


=> Where does the storage come from

    -> depends on environemnt 

    1. Local cluster -> Local disk 

    2. AWS -> AWS EBS 

    3. Azure -> Azure disk 

    4. Google cloud -> Persistent disk 

    5. On-premise 

       NFS -> Ceph -> SAN -> NAS


=> Kubernetes Storage Architecture 


Application
      │
      ▼
     Pod
      │
      ▼
Persistent Volume Claim
      │
      ▼
Persistent Volume
      │
      ▼
Actual Storage


=> Static Provising

   -> An administrator creates storage beforehand 

      Admin -> creates -> PV

    -> developer request storage

       PVC -> gets existing PV


=> Dynamic Provising 

   Developer request storage 

     PVC -> Storage classes -> Automatically creates pV



"""