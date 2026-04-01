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
                                       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       """