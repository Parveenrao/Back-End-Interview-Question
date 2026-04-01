"""   
=> Event Driven Architecture 
   
   -> Event driven architecture is a design pattern where components communicate by producing and consuming events  , instead 
      of directly calling them
      
      An event happend  = something happened in the system 
      Example -> OrderPlaced , PaymentCompleted , UsersignedUp


------------------------------------------------------------------------------------------------------------------------------

=> Core Idea:
    
    -> Instead of service calling:
    
       Order Service -> Payment Service -> inventory Service 
     
        Tight Coupling 
   
   -> We do this loose coupling 
       
       Order Service emits "OrderPlaced"
              |     
          Payment Service listen
          Inventory Service listen
          Notification Service listen
-----------------------------------------------------------------------------------------------------------------------

=> Key Components 
  
   1. Event Producer 
       -> Generate Events 
       Example : Order Service 
   
   2. Event Consumer
      -> Listen and react 
       Example : Email Service 
   
   3. Event Broker
       
       -> Middleman that routes events 
          Apache kafka , RabbitMq , Amazon EventBridge 
-------------------------------------------------------------------------------------------------------------------
=> Working 

   1. User places an order 
   2. Order service emits -> Order-Placed
   3. Broker store events/distribute 
   4. Multiple Service listen/react independently
       
       -> Payment Service = process payment
       -> Inventory       = update stock
       -> Notification    = send email
    
   
   -> No service directly dependent on another
--------------------------------------------------------------------------------------------------------------------

=> Pros 
  
   1. Loose coupling = easier to scale 
   2. High scalability 
   3. Async Processing 
   3. Fault tolerance  -> if one service down  , does not mean whole system down

=> Cons 
   
   -> Eventual Consistency = Not immediately consistency
   
   -> Complex monitoring
   
   -> Hard debugging 
   
------------------------------------------------------------------------------------------------------------------

=> Types of Event Processing 
   
   1. Event Notification 
       
       -> Just singnal something happend
   
   2. Event-carried-state-transfer 
      
      -> event contains data 
         
         order place with items , price , user_id
   
-------------------------------------------------------------------------------------------------------------------

=> What Problem EDA solve 
   -> Tight COupling and Scalability 

----------------------------------------------------------------------------------------------------------------

=> Eventual Consistency 
    -> Data may not be immediately consistent across services , but will consistent over time 
    
---------------------------------------------------------------------------------------------------------------

=> When not to use EDA
   -> Simple CRUD API
   -> Strong consistency 
   -> Small system                     
   
            










                           
"""