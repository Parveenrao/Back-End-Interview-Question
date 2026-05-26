""" 
=> Config Map 
   
   -> A config map is used to store non - sensitive configuration data outside your application
   
   -> Enviornments variables or config file managed by kubernetes instead of hardcoding in code


===========================================================================================================

1. AS Environment Variables
    
    ConfigMap yaml
    
    apiversion : v1
    kind : ConfiMap
    metadata:
        name : app-config
    
    data:
    DB_HOST  : mysql-service
    APP_MODE : production
    
  
  -> Use in Deployment 
     
     env:
       - name : DB_HOST
         
         valueFrom:
          configMapKeyRef:
             name : app-config
             key : DB_HOST


2. Import all keys (envFrom)
      
      envFrom:
       - configMapRef:
          name : app-config
          
      This loads all keys as environment variables
      
      
      -> can cause conflicts is keys are overlap


3. Mount as File 
        
        
        volumeMounts:
           - name: config-volume
              mountPath: /etc/config

        volumes:
          - name: config-volume
             configMap:
              name: app-config                              

           Each key becomes a file:


================================================================================================

=> Difference betweeen env and envfrom 
     
     env      -> specific key
     envfrom  -> import all keys     

==============================================================================================

=> Can ConfigMap store sensitive data?
    
    No 
    
    Stored in plain text (base64 not used here)
    Visible via kubectl get   

===============================================================================================

=> What happens when ConfigMap is updated?
       
       Env variables → ❌ not updated
       Volume mount → ✅ updated automatically       
       
       
       kubectl apply -f configmap.yaml
       
       
       To reflect changes:

       kubectl rollout restart deployment my-deployment     

"""