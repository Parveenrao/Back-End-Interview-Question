""" 

=> Saga Pattern 
    
    -> Before move on saga patter , lets discuss what problem saga solve 
    
    -> In monolithic architecutre , we use data txn (ACID)
    
    -> But in Microservice , each servive has its own db  , we cannot do single txn across services easlity

----------------------------------------------------------------------------------------------------------------

=> Working
    
    -> Saga is sequence of local transaction where each step
          
          1. Update its own db
          2. Publish an event
          3. is something fails , triggering compensation action

=> Example , Order System
     
     Order Service     -> creates order 
     Payment Service   -> deduct money 
     Inventory Service -> Reserve stock         
     
     Order created -> Payment deduct -> Inventory failed
     
     now we must 
       
       refund payment 
       
       Cancel order 
       
      These are called compensation action

-----------------------------------------------------------------------------------------------------------

=> 1. Choreography Saga 
    
    -> This is no central controller 
    
    -> Service will react to events 
    
    -> Each service 
       
       1. Listen to events 
       2. Decide what to do 
       3. Emits new events 
  
  
  -> Working 
      
      1. Create Order 
          
          -> order service create ordere in db 
          -> Publish event
                    
                     {
              "event": "OrderCreated",
              "orderId": 101,
              "amount": 500
             }
      
      2. Payment Service
           
           -> Listen to order created
           
           -> Deduct money
           
           -> EMit 
                   
                   {
             "event": "PaymentCompleted",
            "orderId": 101
             }      
      
      3. Inventory Service
           
           -> Listen to payment completed
           
           -> Reserve stock 
           
           -> Emits
           
               {
         "event": "InventoryReserved",
        "orderId": 101
        }        
      
      4. Final state 
          
          -> Order service marked confirm      

-------------------------------------------------------------------------------------------------

2. Orchestration Saga 
    
    -> A central service(orchestrator) control the entire worklow
    
    -> Instead of service react blindly to events 
    
    -> One service decides what happen next 
    
    -> call other serivce 
    
    -> Handle failure and compensation
  
  
  => Working 
      
      1. Start saga
          
          Client -> orchestration
          
      
      2. Orchestration -> order service 
          
          -> create order , if success move forward 
      
      3. Orchestration -> payment 
         
         deduct money 
      
      4. Orchestration -> inventory 
          
          reserve stock 
      
      5. Success
           
           -> mark completed 
           
           order => confirmed
    
    -> Failure case 
         
         let say inventory failed 
         
         now orchestration called payment service and order service 
   
   -> key component 
      
      1. Orchestrator (Brain)
          
          -> Track state , Decide next state , handle retries , trigger compensation
      
      2. Comunication 
          
          -> http / grpc
      
      3. State management 
          
          -> Current step 
          -> completed step 
          -> failed step                                                               



"""