"""  
=> Health CHeck
    
    -> A command that tells docker  if your service is ready or not 
    
---------------------------------------------------------------------------------------------------

=> Basic syntax 
    
    healthcheck:
       test : ["CMD" , 'command']
       interval : 10
       timeout = 5
       retries = 5

1. Postgress 

    healthcheck:
       test : ["CMD-Shell" , "pg_isready  -U user"]
       interval : 5s
       timeout  : 5s
       retries  : 5

2. Redis 
    
    healthcheck:
       test " ["CMD-Shell" , 'redis-cli' , 'ping']


3. HTTP Endpoint 
           
           healthcheck:
               test: ["CMD", "curl", "-f", "http://localhost:8000/health"]                          

"""