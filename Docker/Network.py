"""   => DOCKER NETWORK 

      1. Why we need docker network
         -> By default every container is islolated 
         -> If you run 
            # docker run postgres
            # docker run fastapi-app
            
          They cannot talk to each other by name 
          
           Your fastapi would not know 
            -> What is postgres
            -> What ip it has 
            -> how to connect
    
     2. Docker network allow containers
        -> Communicate securely 
        -> Discover each other by name 
        -> Stay isolated from other container 
     
     3. What happens without custom network 
     
       -> if you dont create a network 
       
          1. Docker put container in default bridge network 
          2. You must connect using  IP address (bad idea)
          3. IP change when conatiner restart 
     
     
     4. Step-By-Step  Creat and use docker network 
     
         1. Create network 
         
           # Docker network create my-network 
         
         2. Check network 
         
            # docker network ls 
        
         3. Run postgress in that network 
         
            docker run -d --name postgress --network my-network -e POSTGRES_PASSWORD = 1234 postgres
            
            container name postgres 
         
         4. Run fastapi in that network 
         
           docker run -d --name api --network my-network -p 8000:8000 fastapi-app 
           
        
         5. How it work internally 
          
            1. When container are on the same user - defined network 
            2. Docker run an internal DNS server 
            3. Container name become host name 
            4. They can ping each other 
            
          eg.  # docker exec it api ping postgres
          
         6. Types of Docker Network 
         
            1. Bridge Network (Default for single host)
            
            2. Host network 
               
               Container share host network                  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """