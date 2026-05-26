""" 
2. Rolling Updates
    
    -> We update instance one by one 
    
    -> Assume we have 3 servers / containers
        
        Server A (old)
        Server B (old)
        Server C (old)
    
    
    1. Update Server A -> new version
    2. Wait health check
    3. Update Server B 
    4. Wait 
    5. Update Server C

---------------------------------------------------------------------------> 

=> Implementation 
   
   1. Run 3 Docker instance 
   
   docker run -d --name app1 -p 8001:8000 your-app
   docker run -d --name app2 -p 8002:8000 your-app
   docker run -d --name app3 -p 8003:8000 your-app    
   
   
   upstream backend {
    server localhost:8001;
    server localhost:8002;
    server localhost:8003;
     }

     server {
         location / {
           proxy_pass http://backend;
       }
    }    
    
    
    -> Update one container at a time 

--------------------------------------------------------------------------------------

=> App must be stateless
    
    -> Don't store session in memory 
    -> Use state locally 

=> Backward Compatability 
     
     -> Old + new version run together

=> Zero Downtime 
     
     -> Single server = no rollign deployment     
             
"""