""" 

=> Kube-proxy 


    -> Kube proxy is the network component that enables communication between Pods and 
       Service inside an kubernetes cluster 


=> Why do we need Kube-proxy 

    -> Suppose we have three backend pods

        backend pod 1
        10.0.1.5

        backend pod 2
        10.0.1.8

        backend pod 3
        10.0.1.12

    Now another application wants to call the backend 

    -> suppose pod 1 crash

        New pod start 

        Old ip -> 10.0.1.5

        New ip -> 10.0.2.18

        Pods in kubernetes are empemeral

        Their Ips are change constantly 


=> Kubernetes Solution 

   1. Instead of exposing Pods IP 

   2. Kubernetes creates a Service 

      Service 

      backend-Service 

      ClusterIP

      10.96.0.15

  3. Application Call

     10.96.0.15


     Now kubernetes decide 

     which backend pod should recieve this request 


     Thats why kube-proxy comes in


    
Frontend Pod                   
      │
      │
      ▼
backend-service
10.96.0.15
      │
      │
 kube-proxy
      │
      ▼
Chooses Pod

10.0.1.5     

Frontend

↓

Service

↓

kube-proxy

↓

10.0.1.8


=> It perform load balancing among the available pods


=> one Kuber proxy per node


=> Responsibilities of kube-proxy
    1. Watches the API Server for Service and Endpoint changes.
    2. Configures networking rules (iptables, IPVS, or nftables depending on mode and environment).
    3. Provides Service-based load balancing across Pods.
    4. Removes unhealthy or deleted Pods from routing.
    5. Updates rules when Pods are created or removed.
    6. Enables stable virtual IPs (ClusterIPs) for Services.


"""