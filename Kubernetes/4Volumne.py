""" 
=> Volume
    
    -> Containers are ephemeral (temporary)
    
    -> If container restart , data inside lost
   
   -> VOlUME is a storage attached to a Pod that:
        
        1. Survive container restart 
        2. Can be shared between containers in the same pod
     
     
     apiVerson : v1
     kind : pod
     metadata:
         name : volume - pod
     
     spec:
        containers:
          -name : app
          image : nginx
        
           volumnemounts:
          
             -name : my-volume
              mountpath : /data
     
        
        volumes:
          -name : my-volumne
          empty_dir = {}
    
    
    -> empty_DIR = {}
       Created when pod restart 
       deleted when pod is deleted
       
       Temporary storage
       caching 
       shared data between containers

---------------------------------------------------------------------------------------------------

=> Types of Volume 
    
    
    1. Empty_DIR 
    
    
    2. Host Path
       
       hostpath:
         
         -> Access node filesystem
         
         -> NOt portable 
         -> Risk
    
    3. ConfigMap volumes  
        
        -> Mount config as files
    
    
    4. Secret volumes 
        
        -> Secure way to inject credentials as secret

=======================================================================================================

=> A Volume is storage attached to a Pod that allows data to persist across container restarts and 
    can be shared between containers in the same Pod.        
                                   
                        

"""