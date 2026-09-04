""" 


=> LoadBalancer Service 

    -> A load balancer service expose application to internet by asking your cloud provider 
       to create an external load balancer 

    -> The load balancer receieves traffic from user and forward it to the kubernetes Services
       which then distribute request to the Pods


=> why do we need Load balancer service

    -> Imagine deployed application with 5 replicas

    -> without load balancer 


User
  |
  |
Node IP:30080 (NodePort)
  |
  |
Kubernetes Service
  |
  +----> Pod 1
  +----> Pod 2
  +----> Pod 3

  
  -> user must know Node Ip and Node port , which is not ideal for production 


  -> with load balancer 

                Internet
                   |
                   |
        35.201.10.25 (Public IP)
                   |
          Cloud Load Balancer
                   |
            Kubernetes Service
                   |
        +----------+----------+
        |          |          |
      Pod1       Pod2       Pod3


=> flow


User
   |
   |
Public IP
   |
Cloud Load Balancer
   |
NodePort Service
   |
ClusterIP Service
   |
Pod


=> A LoadBalancer Service automatically creates a NodePort Service, which in turn 
   includes a ClusterIP Service.


=> Why use a LoadBalancer Service?

    -> To expose an application to the internet using a cloud-managed external load balancer.   
"""