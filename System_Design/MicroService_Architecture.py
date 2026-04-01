"""   
=> MicroService Architecture
     
     -> Splitting big system into small , independent services
     
---------------------------------------------------------------------------------------------------------

=> Each Services 
  
  1. Has its own responsibility 
  2. Runs independently 
  3. Communicate over HTTPS/messaging 
  4. Have its own database

  Example -> E-commerce App
    
    -> Instead of monolithic app
    
    -> You split into 
       1. User Service
       2. Order Service 
       3. Payment Service
       4. Inventory Service
       5. Notification Service 

--------------------------------------------------------------------------------------------------------------------

=> Why MicroServices 
    
    1. Independent Development
    2. Independent Deployment
    3. Independent Scaling 

-------------------------------------------------------------------------------------------------------------------

=> Core Building Block 
    
    1. Service Independence 
        
        Each Service has 
         ->  Own logic 
         ->  Own Db 
         ->  Own deployment
      
      -> No shared DB between services

    
    2. Communication 
       
       1. Sync (Rest api , grpc) 
          
          Order  -> Payment (wait for response) , Tight Coupling 
       
       2. Aysnc 
          -> Event Driven (Kafka / RabbitMq)
    
    3. Database Per Scaling 
        
        order Db
        User Db
        Payment Db 
        
        -> Independent Scaling
    
    4. API Gateway 
       
       -> Single Entry point 
           
           Handles 
           1. Authenticaton
           2. Rate Limiting
           3. Routing 
    
    5. Service Discovery 
       
       -> Service need to find each other dynamically
    
    6. Config Management 
       
       1. ENV flag
       
       Centralized 
    
    7. Observability 
       
       1. Logging 
       2. Tracing

--------------------------------------------------------------------------------------------------------------

=> Challenges 


    1. Distributed System Complexity 
        
        -> Network calls 
        2. Partial failure 
        -> Retry logic 
     
     -> Network in unreliable 
    
    
    2. Data Consistency 
       
       -> No single db , No ACID across services 
    
    3. Latency 
       
       -> Multiple service calls


------------------------------------------------------------------------------------------------------------------------

=> When not to use MicroServices 
    
    1. Small team
    2. Simple Product 
    3. Early age startup 
 
 -> Start with monolithic first 
 
 
---------------------------------------------------------------------------------------------------------------------------

=> When use MicroService 
   
   -> System is large and growing 
   -> Multiple teams 
   -> Frequent deployment
   -> Need Indepedent scaling
   
----------------------------------------------------------------------------------------------------------------------

=> Real World Example 

   User places order
         ↓
   Order Service → emits event
         ↓
   Payment Service → processes payment
         ↓
  Inventory Service → updates stock
         ↓
  Notification Service → sends email                 
     
             
                      
             
     
"""