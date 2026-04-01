"""   
=> Saga Pattern 
   
   -> In microservice architecture , each service has its own database
   -> So we cannot use ACID Txn across services 

  -> Exmaple 
     
     Order-Service     -> Create-Order 
     Payment-Service   -> deduct money
     Inventory-Service -> reserve stock 
     
   what if 
     
     -> order created 
     -> Payment failed 
     
     Now system is incosistent   
     
-----------------------------------------------------------------------------------------------------------
=> Saga Pattern = Sequence of local transaction + compensating actions
    
    So instead of one big transaction 
    each service runs its own txn and if something fails undo previous steps using compensation
    
    
    T1 → T2 → T3 → T4

    If T3 fails:
    run C2 (undo T2)
    run C1 (undo T1)   
    


-------------------------------------------------------------------------------------------------------------

1. Choreography (Event-Driven)

    
    -> No central controller 
    -> Service talks via events 
    -> Each service decide  , what to do next , how to react on failures 
  
  -> Everyone listen , react and emit , no boss ,

------------------------------------------------------------------------------------------------------------

=> Working 

   1. Order Service 
      -> Create order 
      -> Emits event 
             'Order-Created'
   
   2. Payment Service 
      -> Listen to OrderCreated 
      -> Try Payment
      
      -> Emits 
          
          PaymentSucceeded or PaymentFailed
   
   3. Inventory Service 
      
      -> Listen to PaymentSucceed
      -> Reserve stock 
      
      -> Emits 
         
         InventoryReserved or InventoryFailed
   
   4. Order-Service Again 
       
       -> Listen to failure events 
       
     PaymentFailed -> Cancel order 
     
     InventoryFailed -> CancelOrder -> Trigger Refund

-> Failure Flow 
    
    lets say inventory failed 
       
       Order-Created 
           |
       PaymentSucceeded
           |
       InventoryFailed 
   
   Compensation Trigger 
   
   InventoryFailed -> PaymentService.refund()
   InventoryFailed -> OrderService.cancel() 
   
------------------------------------------------------------------------------------------------------

=> Real Problem 
   
   -> Event Explosion
       
       OrderCreated
       PaymentStarted
       PaymentCompleted
       PaymentFailed
       InventoryCheckStarted
       InventoryReserved
       InventoryFailed
       OrderCancelled
       RefundInitiated
       RefundCompleted       


------------------------------------------------------------------------------------------------------

=> Good Event Design 
    
    
    {
  "eventType": "PaymentSucceeded",
  "orderId": "123",
  "userId": "456",
  "amount": 1000,
  "timestamp": "..."
}

=> Events can be delivere Twice 
    
    -> Use idempotence

=> Event Ordering 
     
     -> Kafka gurantee ordering within partition 
     
         -> Use same partition  key 
    
=> Retry + DLQ 
    
    -> Event processing fails 
     
     Retry -> Retry -> Retry -> DLQ 


=> Who handle Compensation 

   
   -> Depend on System                                            
       
                              
    
        
              
"""