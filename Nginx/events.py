"""  
=> Events 
    -> events {} control how nginx handles connection internally
        
        no http logic , not routing 
    
    -> Its about 
         
         how nginx talks to os and handles thousand of clients 
     
     example -> 
     
       events {
           worker_connection = 1024;
       }   
    
    
    -> Nginx 
       
        Use event loop (async model) 
        one worker handle many connection
 
-----------------------------------------------------------------------------------------
2. Workers (Processes) 
     
     -> worker_process auto;
     
     Nginx create multiple worker processes 
     
     -> Each worker runs independently
     -> Each use event loop
   
   -> auto means 
       
       no of cpu cores 
       
       -> If your machine has 
          1 core = 1 worker
          2 core = 2 worker 
          3 core = 3 worker  

--------------------------------------------------------------------------------------------

=> worker_connections 
     
    -> How many connection one worker can handle at the same time 
    
    -> Total connection = worker_prcoesses * worker_connections 
    
    worker_processes 4;
    
    events {
        worker_connections = 1024;
    }
    
    -> Total = 4 * 1024 = 4096

----------------------------------------------------------------------------------------------

=> Use epoll
    
    -> High performance event system in epoll
    -> Handles massive concurrent connections
  
  -> Epoll is linux kernel features used for 
      Efficiently monitoring many connections
   
   -> Without epoll
       Nginx check connection again and again -> Waste cpu
   
   -> with epoll
       
       Os tell nginx -> this connection is ready 
       
       events {
              use epoll;
               worker_connections 1024;
           }         
     
    -> "Use Linux epoll system for handling events"

---------------------------------------------------------------------------------------------------

=> multi_accept on;

    -> It control how worker accept new incoming connections
    
    -> Default behavior (multi_accept of;)
        
        worker accept one connection at a time 
         
         new connection arrive ->worker pick one ->  user process -> next     
    
    -> with multi_accept on;
          worker accept all availabe connection at once 
          
          New connections arrive → worker grabs all of them immediately
    
    -> When to use 
        1. high traffic system
        2. Sudden traffic brust 
        3. Load balancer / gateways 
    
    -> Trade off
       1. One worker may grab too many connection 
       2. other worker may stay idle 
       3. Can increase CPU usuage 
       
   -> Real scenario
             
             events {
              worker_connections 1024;
              multi_accept on;
         }          
  







                
"""