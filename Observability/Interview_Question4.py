"""
=> Target In Prometheus 

    Target = the thing  exposing /metrics that prometheus collects from data
    
    -> IF app runs http://my-app:8000/metrics
    
    my-app:8000  = target 
    
    /metrics = endpoint


-------------------------------------------------------------------------------------------

=> Flow 
    
    1. Target expose /metrics
    2. Prometheus send HTTP request 
    3. Target respond with metrics 
    4. Prometheus store data 

------------------------------------------------------------------------------------------

=> Type of Target 
     
     1. Application Target 
         
         -> Your own service 
            
            Backend API
            Microservices
            Web apps
     
     2. Exporter Target 
                 
                 Node Exporter → system metrics
                 MySQL Exporter → DB
                 Blackbox Exporter → uptime
            
             Exporter itself becomes the target  
     
     3. Infrastructure Target 
              
              
              Kubernetes pods
              EC2 instances
              Containers

               Discovered dynamically                     

"""