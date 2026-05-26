""" 

=> Secret
    
    -> A secret store sensitive data 
        
        1. DB password
        2. API keys
        3. Token
        4. Certificate
  
--------------------------------------------------------------------------------

=> WHy not ConfigMap 
   
   1. ConfigMap = Plain text
   2. Anyone can with access can read it
   
   3. Secret give you controlled access + safer handling
   
   
   4. Kubernetes secrets are not encrypted by default (just base64 encoded)

=====================================================================================

-> Baisc Secret ymal 
     
     apiVersion : v1
     kind : secret 
     metadata :
        name : app-secret
     
     type : Opaque
     data : 
        DB_PASSWORD: cGFzc3dvcmQ=        

=========================================================================================

=> Ways to Use Secret
    
    
    1. AS Enviornment Variable
    
        env:
         - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secret
               key: DB_PASSWORD        
    
    
    2. Mount as File 
                
                
                volumeMounts:
                   - name: secret-volume
                     mountPath: /etc/secret

                volumes:
                     - name: secret-volume
                         secret:
                          secretName: app-secret                  


----------------------------------------------------------------------------------------------------------

=> Types of Secret 
   
   1. Opaque 
      
      type : Opaque
      
      -> Custom key-value par
      -> DB password
      -> API keys
   
   2. kubernetes.io/dockerconfigjson
       
       ->  Used for private container registries
       
           kubectl create secret docker-registry my-secret \
           --docker-username=user \
           --docker-password=pass \
           --docker-email=email   
   
   3. kubernetes.io/tls
       
       -> Used for tls and certificate
   
   4. kubernetes.io/ssh-auth
       
       -> For ssh keys

-------------------------------------------------------------------------------

=> What happens if you don't specify type?

     -> Defaults to Opaque           
            

"""