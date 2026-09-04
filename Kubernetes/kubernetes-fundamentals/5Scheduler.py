""" 

=> Scheduler In Kubernetes 

    -> Scheduler is Kubernetes control plane component that watches for new pods that don't have 
       node assigned and select the best worker node for each one 


    -> It does not create Pods and does not run containers

    -> Its Only responsibilties

        Unscheduled Pod -> CHoose Best Node  -> Bind Pod To Node 



=> Scheduler watch for Pending nodes

    -> scheduler continuously watches the API Server 


    Pending Pod -> Find Candidate Node -> Filter Nodes -> Score Nodes -> Choose Best Node -> Bind Pod 

    -> Done

-> Step 1. Suppose cluster 

             Node A
             Node B
             Node C
             Node D

-> Step 2. Filtering 

     -> Now the scheduler removes nodes that cannot run pods 

     -> This phase is called Filtering 


     -> What does filtering check 

        1. Available CPU 
        2. Availabe memory 
        3. Resource Request 
        4. Taints and tolerations 
        5. Node affinity 
        6. Pod affinity 
        7. Topology spread contrainst
        8. Volume compatibility
        9. Port conflict

-> Step 3 Scoring 

    Suppose filtering leaves

     Node A

     Node B 

     Node C

     whoch one kubernetes choose 

     It score them 


     Node A = 92 

     Node B = 80 

     Node c = 75


-> Step 4 Binding 

    After choosing a node 

    Pod -> Node B

    Scheduler send a binding reques to API server 


-> Step 5 kubelet starts the pod


=> Full Flow


Developer
     │
     ▼
kubectl apply
     │
     ▼
API Server
     │
     ▼
Deployment Controller
     │
     ▼
ReplicaSet
     │
     ▼
Pending Pod
     │
     ▼
Scheduler
     │
 Filter Nodes
     │
 Score Nodes
     │
 Choose Best Node
     │
 Bind Pod
     ▼
API Server
     │
     ▼
kubelet
     │
     ▼
Container Runtime
     │
     ▼
Running Pod




=> Complete Control Plane Architecutre 


                          Developer
                              │
                    kubectl apply -f app.yaml
                              │
                              ▼
                    +-------------------+
                    |    API Server     |
                    +-------------------+
                              │
            Authenticate / Authorize / Validate
                              │
                              ▼
                    +-------------------+
                    |       etcd        |
                    | (Desired State)   |
                    +-------------------+
                              ▲
                              │
        Watches               │             Watches
                              │
      +-----------------------+------------------------+
      │                                                │
      ▼                                                ▼
+----------------------+                     +----------------------+
| Controller Manager   |                     |      Scheduler       |
+----------------------+                     +----------------------+
| Deployment Ctrl      |                     | Find Pending Pods    |
| ReplicaSet Ctrl      |                     | Filter Nodes         |
| Node Ctrl            |                     | Score Nodes          |
| Job Ctrl             |                     | Bind Pod             |
| StatefulSet Ctrl     |                     +----------------------+
+----------------------+


"""