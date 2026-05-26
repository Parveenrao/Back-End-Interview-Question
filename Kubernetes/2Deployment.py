""" 
=> A Deployment is a Kubernetes controller that manages Pods and ensure 
       number of replicas are always are running
       
-------------------------------------------------------------------------------------------

=>  Deployment => Automation layer  over Pods
        
        1. Creation
        2. Scaling
        3. Updates
        4. Recovery
        
-------------------------------------------------------------------------------------------------

=> Why Deployments Exist 
   
   Pod dies --> gone 
   NO scaling
   No updating 
   
   
 -> Deployment solves:

   Auto-healing ✔️
   Scaling ✔️
   Rolling updates ✔️            
       
       
------------------------------------------------------------------------------------------------------
=> Commands 
   
   1. Create command 
      
      kubectl apply -f deploy.yaml
   
   2. View deployments 
       
       kubectl gets deployments 
   
   3. Scaling 
       
       kubectl scale deployment nginx-deploy --replicas=5
   
   4. Rolling update 
   
        change image 
           kubectl set image deployment/nginx-deploy web=nginx:1.25
   
   5. check rollout 
        kubectl rollout status deployment nginx-deploy
    
   6. Rollback 
   
      kubectl rollout undo deployment nginx-deploy 
      
   7. Describe deployment
       kubectl describe deployment nginx-deploy
   
   8. Get deployment yaml 
   
        kubectl get deployment nginx-deploy -o yaml
   
   9. change deployment yaml
        
        kubectl edit deployment nginx-deploy
   
   10. Delete deployment 
         kubectl delete deployment nginx-deploy
         
         delete deployment , pod, replica set 
   
   11. watch real time 
        
        kubectl get pods -w                       

---------------------------------------------------------------------------------------------

=> “How do you update an application?”

    -> I update the image using kubectl set image, then monitor rollout using kubectl rollout status. 
    If something fails, I rollback using kubectl rollout undo.
                                       
       

=> What is Replica-Set
     
     A Replica-set ensure that specific no. of pods replica are always running
      
    -> maintain desired count 
    -> Recreate pod if they 
    -> use label selector to manage pods


=> Deployment 
   
   -> A Deployment is a higher-level abstraction that manages Replicaset
   
   -> It addd
      
      1. Rolling updates (zero downtime)
      2. Rollbacks        
      3. Verisioning
      4. Declartive update

--------------------------------------------------------------------------------------------------

=> How Does kubernetes ensure desired number of pods
    
    -> Kubernetes use a control loop (reconciliation loop)
    
    flow 
    
    1. You define desired state replica = 3
    2. Controller Replicaset watch actual state 
    3. if mismatch 
        
        less pod - create new
        more pods - delete extra 
    
    Kubernetes constantly compares desired vs actual state and fixes differences automatically.

==============================================================================================================

-> Rolling Update
   
   1. Updating pod gradually , not all once
   
   -> New Replic set created 
   -> New pod start 
   -> Old pod terminated slowly
   
   -> Zero downtime
   
   strategy:
    type: RollingUpdate
    rollingUpdate:
     maxUnavailable: 1
     maxSurge: 1             

=> What happen in deployment fail 
   
   -> Kubernetes pause rollout
   
   kucbectl rollout undo deployment my-deployment


=> Pod Stuck in Pending 
    
    1. Not enough CPU/memory
    2. No matching node 
    3. Image pull issue
    4. Persistant volumne not exist
  
  -> debug
      
      kubectl describe pod <pod-name>


=> Pod in CrashLoopBackOff
    
    -> Pod keep crashing again and again 
    
    1. Wrong app config
    2. Port config
    3. DB not reachable 
    4. Code crash
    
    kubectl logs <pod-name>

=>  What happens when Node dies?
       
       All Pods on that node → lost
       Controller detects missing Pods
       New Pods created on other nodes

       
       This is self-healing    


=>  How does scaling work
          
          kubectl scale deployment my-deployment --replicas=5                       
         
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       """