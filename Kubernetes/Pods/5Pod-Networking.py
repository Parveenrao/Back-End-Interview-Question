""" 


=> Pod Networking 

    -> Imagine we have two pods 

         Pod A -> python app

         Pod B -> Mysql


       the application needs to talk to mysql

       In docker , containers usually communicate over a Docker bridge Network 

       In Kubernetes , Pods communicate over the cluster network


 => Kubernetes Networking Model 

    1. Every Pod gets its own IP
          -> Pods do not share Ips

    2. Containers inside a Pod share one Ip


    3. Pods can communicate without NAT


=> Who Create the Network 

   -> The Responsibility belogs to a CNI (Container Network Interface) plugin


   -> How Pods get an IP

       Step 1. We create a Pod

       Step 2. API server store it in etcd 

       Step 3. Scheduler select a node 

       Step 4. Kubelet receives the Pod specification

       Step 5. Kubelet ask the container runtime

               The Pod sandbox (implemented by pause container) is created first 

      Step 6. The runtime ask the CNI pluging

               1. Create network namespace 
               2. Assign Ip
               3. Connect POD

      Step 7. CNI peform linux networking operation                  



"""