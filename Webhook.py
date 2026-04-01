"""  
=> WebHook 
     -> Webhook is a way for one system to automatically send real time data to another system when an event happens
      
     -> Instead of asking repeadetly something happens
     
     -> System push data when something happens

--------------------------------------------------------------------------------------------------------------------------

=> Webhook Vs API
    
    -> APi is pull-based , you ask  "Hey server , any new orders"
    
    -> Webhook , push model , hey server tells you , Hey new order happens
    
-----------------------------------------------------------------------------------------------------------------------------

=> Working of Webhook 
   
   1. Register a webhook url
       
       -> We tell external service , when this event happens  , call this URl
       
       https://yourapp.com/webhook/payments
       
   2. Event happens 
      
      -> Inside external system (stripe)
      
      -> payment success
      -> Subscription created
      -> Refund process
      
      This event is triggered 
   
   3. Service send HTTP  Request 
       
       The service makes an post request to your server
      
      -> Example 
              POST /webhook/payment
              Content-Type: application/json     
              
              
              
              {
               "event": "payment.success",
                "user_id": "123",
                 "amount": 500
                }
          
          This is the core working 
          
          Event -> HTTP POST -> Your server
   
   4. Your server Receives it
       
       -> Backend receieve an endpoint      , system get notified
   
   5. Verify Authenticity 
       
       -> Did this request really come from stripe 
       
          They send an signature , xyz : abc1234
           
           you verify it 
           
   
   6. Process the event 
      
      based on event type
      
      data["event"] = "payment.success"
      
      # update db
      # mark order paid
      # send email
   
   7. Send Response
       
       -> You must respond quickly
          
          {status : Recieved}
          
          if you dont 
            
            service retry 
            
            you may get duplicate event
    
    8. Retry mechanism 
        
        -> server crash
        -> timeout                                      
         
"""