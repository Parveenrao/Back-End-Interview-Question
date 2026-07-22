"""


=> What is etcd

    -> etcd is a distributed , strongly consistent key-value database used by kubernetes
        to store all cluster state 

    -> It is a single source of truth for the cluster 

    -> without etcd kubernetes has no memory

    -> Every component plane component depends on etcd 


=> What does etcd store

    1. Almost every kubernetes object 

Cluster
│
├── Pods
├── Deployments
├── ReplicaSets
├── StatefulSets
├── DaemonSets
├── Services
├── Secrets
├── ConfigMaps
├── Nodes
├── Namespaces
├── RBAC
├── Events
├── Persistent Volumes
└── Leases

=> It does not store your container images or application files. 
   Those live in container registries or persistent storage.

   
=> Strong consistency

    -> Imagine three control plane nodes

        etcd - 1

        etcd - 2

        etcd - 3

    You update a deployment 

        replica = 5

    with strong consistency , all read will agree on the same committed value

      etcd 1 -> 5

      etcd 2 -> 5

      etcd 3 -> 5

      etcd 4 -> 5

      This is achieved uisng Raft-consensus algorithm


=> Distributed database

   -> A production kubernetes cluster usually runs multiple etcd members 

etcd Cluster

+---------+
| etcd-1  |
+---------+

+---------+
| etcd-2  |
+---------+

+---------+
| etcd-3  |
+---------+


All members replicate the same data.

If one member fails, the cluster can continue operating as long as it still has a quorum.


=> Read - Write flow

kubectl

↓

API Server

↓

Leader etcd

↓

Replicate

↓

Majority confirms

↓

Committed


=> Watches 

    -> kubernetes component  do not continuously ask 

        1. Any update 
        2. Any update 
        3. Any update

    -> Instead they use watch mechanism via the API server 


    -> Deployment Updated = API server receive change = controlled in notified = create pod


=> Does Every component have etcd 

   -> No


   -> Scheduler = API Server = etcd 

   -> Controller = API Server = etcd

=> API Server is the only kubernetes component that directly reads from and writes to etcd


=> What happen if etcd crash 

   -> Existing Pods on worker nodes usually keep running because the kubeletes continue managing
      them

   -> However , the control plane cannot reliabily make changes to cluster state

   -> This is why regular etcd backups are critical in production   


=> Security 

   -> etcd often store sensitive kubernetes resources , including secrets

   -> Because of that 

       1. Communication is typically protected with TLS

       2. Access is tightly restricted 

       3. Backups should be encrypted and protected


=> etcd Backups 

    1. A common production practice is taking periodic snapshot 

       etc = snapshot = Backup storage

      if the control plane is lost , administrators can restore the cluster state from
      a snapshot 

=> What does etcd store?

    -> Cluster objects such as Pods, Deployments, Services, ConfigMaps, Secrets, Nodes, 
       Namespaces, RBAC policies, and other Kubernetes resources.       



=> Internal Flow 

Developer
    │
    ▼
kubectl apply
    │
    ▼
API Server
    │
    ▼
etcd (Leader)
    │
    ▼
Replicate to Followers
    │
    ▼
Majority Commit
    │
    ▼
API Server updates watches
    │
    ▼
Scheduler / Controller Manager react
"""