""" 

=> Worker Node

    -> Worker Node is a physical or virtual machine that runs your application Pods.

    -> The control plane decide what should happen

    -> Worker node does the work


=>            Worker Node

      +----------------------+
      | kubelet              |
      |----------------------|
      | kube-proxy           |
      |----------------------|
      | container runtime    |
      |----------------------|
      | Pods                 |
      +----------------------+    




====================================================================================

=> Kubelet 


    -> A kubelet is an agent that works on every worker node

    -> Its job is simple 

       1. Make sure the Pods assigned to this node are running exactly as specified

       2. Think of local manager of a worker node



                    Control Plane
                 +----------------+
                 |   API Server   |
                 +----------------+
                        ▲
                        │
                HTTPS (Kubernetes API)
                        │
                        ▼
             +------------------------+
             |      Worker Node       |
             |------------------------|
             | kubelet                |
             | kube-proxy             |
             | containerd             |
             | Pods                   |
             +------------------------+

   -> Each worker node has on kubelet

   -> 100 worker = 100 kubelet  


=> What does kubelet do


    1.  Watch for pods assigned to its node 

    2. Creats pods 

    3. Pulls container image 

    4. Start containers 

    5. Moniter container health

    6. Restart failed containers 

    7. Reports status to API Server 

    8. Mounts volume 

    9. Runs health probe

=> kubelet does not decide where pods should run



=> What is kubelet?

    -> A node agent that runs on every worker node and ensures the Pods assigned to 
       that node are running according to their specifications.

=> Does kubelet schedule Pods?

    -> The Scheduler chooses the node. kubelet only manages Pods that have already 
       been assigned to its node.      


=> Does kubelet create containers?

    -> It communicates with the container runtime through the 
       Container Runtime Interface (CRI), and the runtime creates and starts the containers.        
"""