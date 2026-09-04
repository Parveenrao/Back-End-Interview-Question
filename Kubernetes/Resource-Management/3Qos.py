""" 


=> QoS (Quality of service)

   -> Kubernetes use Qos Classs to categorize Pods based on their CPU and memory request 
      and limit

   -> This become especially important when a node under resource pressure

   -> Qos influence which Pods are more protected and which are more likely to be evicted


=> Why do we need QoS

    -> Imagine a node has

        memory = 8GiB

    -> Several pods are running

        Pod A -> database 

        Pod B -> backend API

        Pod C -> temporary worker 

    -> Eventually node experience sever memory pressure

         Node 8GiB -> Memory Pressure -> Which pod should loose resource / be evicted first         


         
=> 1. Guranteed

     -> Highest QoS Classes


     -> For a pod to be Guranteed , every container in the Pod must have both CPU and 
         memory request and limit for each resources


         request === limit 

         CPU:
          request = 500m
          limit   = 500m

         Memory:
         request = 512Mi
         limit   = 512Mi

        Qos Guranteed 

        THere is no brust range between request and limit

=> 2. Brustable

    resources:
  requests:
    cpu: "250m"
    memory: "256Mi"

  limits:
    cpu: "1"
    memory: "1Gi"

    Because 

    request < limit

    the Pod is not Guranteed

    But it has resource request / limit , so it is not Besteffort either


=> BestEffort

    -> Specify nothing

    -> so effectively there are no CPU/memory request for limits configured for the 
       containers

     -> QoS become BestEffort


     -> Under the NOde pressur , Pds have become the lowest protection


=>                  QoS Classes

                    Pods
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼

   Guaranteed     Burstable    BestEffort

 request=limit   request/limit    no CPU/
 CPU + memory     configured      memory
 every container  but doesn't     requests
                  qualify as      or limits
                  Guaranteed

       ↑              ↑              ↑
    Highest         Medium          Lowest
   protection      protection      protection


=> Kubernetes always kills every BestEffort Pod before touching any Burstable Pod.          

"""