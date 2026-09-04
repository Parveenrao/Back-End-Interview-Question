""" 


=> Networking In Kubernetes

    -> WHy kubernetes need networking 

             Kubernetes Cluster

        Node 1                         Node 2
┌──────────────────────┐      ┌──────────────────────┐
│                      │      │                      │
│ Pod A                │      │ Pod C                │
│ 10.244.1.2           │      │ 10.244.2.2           │
│                      │      │                      │
│ Pod B                │      │ Pod D                │
│ 10.244.1.3           │      │ 10.244.2.3           │
│                      │      │                      │
└──────────────────────┘      └──────────────────────┘


    -> Kubernetes need to support communication such as

       Pod A -> Pod B 

       Pod A -> Pod c 

       Pod A -> internet 

       Internet -> Application

       Pod -> Service -> Pod

    -> First important Rule is 

        Every Pod gets its own Ip



=> Four Important Sceanrios

   1. Pod -> Pod on the same node 

          they should be able to communicate directly

    2. Pod -> Pod across different node 

    3. Pod  -> Node 

        Pod also need communicate with nodes 

    4. Pod -> Service 



=> Important Networking Requirements 

   -> Each Pod has unique cluster-wide Ip at a given time


=> Kubernetes define the networking model , CNi implements it 


=> Kubernetes uses a flat networking model where every Pod receives its own unique cluster IP. 
   Pods are expected to communicate with other Pods across nodes without applications having 
   to perform explicit NAT or host-port mapping. Nodes and Pods must also be able to 
   communicate with each other. Kubernetes defines these networking requirements, 
   while a CNI plugin such as Calico or Cilium implements the actual Pod networking.


"""