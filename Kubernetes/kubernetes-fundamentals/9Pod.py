""" 


=> Pod 

   -> A pod is the smallest deployable unit in kubernetes 

   -> You do not deploy a container directly in container 

   -> Instead we deploye container , the Pod contains one or more container


=> Pod Architecture 


                Pod
+--------------------------------------+
|                                      |
|  App Container                       |
|                                      |
|  Logging Container                   |
|                                      |
|  Monitoring Container                |
|                                      |
|--------------------------------------|
| Shared Network Namespace             |
| Shared Storage Volumes               |
| Shared IPC                           |
+--------------------------------------+


-> A pod is not a container 

-> A pod is a wrapper around one or more tightly coupled containers


-> In reality 

   One Pod -> One container


=> Every pod has their own IP


=> Unlike docker , Pods do not share bridge across node 

=> Kubernetes aims for pod to pod communication across cluster 


=> Multiple conatainers share 

   1. Network 
   2. Localhost 
   3. Storage volumes 
   4. IPC namespace (depending upon configuration)


=> Pods are Ephemeral 

   -> Pods are temporary

   -> pods crash 

   -> Kubernetes create a replacement

   -> The Ip change 


   -> This is why application shoudl communicate through Services , Not directly using Pods Ips


=> kubectl apply
       │
       ▼
API Server stores Pod in etcd
       │
       ▼
Scheduler selects a node
       │
       ▼
Kubelet on that node watches the API Server
       │
       ▼
Container runtime pulls the image
       │
       ▼
Creates the Pod sandbox and containers
       │
       ▼
Pod becomes Running







"""