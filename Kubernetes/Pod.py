""" => A Pod is a single instance of running process in your cluster  and can contain one or more container


       -> A pod is the smallest deployable unit  in kubernetes that runs one or more container 
       
       
           POD => Wrapper around container that gave him shared environment
     
    
    
    1. Network (Same IP)
    
       -> All containers in  a pod share same ip address
       -> They communicate via localhost
       
       👉 Example:

       App container → localhost:5000
       Sidecar container → can call it directly
       
       
    2. Storage(Volumes)
    
        -> Shared storage between containers
        
    3. LifeCycle 
        
        -> Stop together  , Start together
    
    
    Kubernetes does not manage containers directly  , they manage pods          
    
----------------------------------------------------------------------------------------------

=> POD Lifecycle 
   
   -> Pod are ephemeral   
      1. They can die anytime 
      2. They are not permanent
    
   -> Lifecycle 
      
      1. Pending  -> being created 
      2. Running  -> active 
      3. Succeeded/Failed -> finished
      4. Terminated 
    
    -> If a pod die
        1. kuberneted does not restart it directly 
        2. Deployment creates a new pod 
    
    
    A Pod itself is not self-healing. If it crashes, it won't 
    
    automatically restart unless managed by a higher-level controller like a Deployment.               
    

----------------------------------------------------------------------------------------------------------

-> Containers in pod share network  and storage  and are tightly coupled

-> Containers in pod share same ip and communicate via localhost 

-> If a pod crash , it not  automatically restarted unless managed by controller like Deployment


----------------------------------------------------------------------------------------------------------

=> Commands 
  
   1. Create POd 
      
      kubectl apply -f pod.ymal
   
   2. List Pods
      
      kubectl get pods
      
   3. Describe pods 
   
      kubectl describe pods my-ngnix    , show pod id , event , container
   
   4. Access inside pod 
   
        kubectl exec -it my-ngnix --/bin/bash
   
   5. kill the pod 
       
       kubectl delete pod my-ngnix


--------------------------------------------------------------------------------------------------

=>  Difference between Pod and Container?

    A container runs an application, while a Pod is a wrapper that manages one or more containers and 
    provides shared networking and storage.  
    

=>  Can we use Pods directly in production?

    No, in production we usually use controllers like Deployments because Pods alone are not 
    self-healing or scalable.                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """