""" 
=> Poison Pill Msg
     
     -> Casuse your consumer to fail every time
     -> Gets re-read again and again 
     
     -> Prevent the system to moving forward


-----------------------------------------------------------------------------------

=> Wht it is dangerous 

   -> kafka working 
       
       Read -> Process -> commit offset 
   
   -> if processing fail 
        
        Read -> Crash -> No commit -> Read again -> loop
          
          you stuck at infinity loop




---------------------------------------------------------------------------------------

=> Causes
    
    1. Schema mismatch 
        
        producer send {amount : "500"}
        
        consumer expect int(amount)
        
        crash every time 
    
    2. Business logic fail every time 
        
        if balance < amount 
            raise Exception(Insufficient funds)
            
            always fail for that message



---------------------------------------------------------------------------------------

=> Use try catch block 
    
    try:
    process(msg)
    consumer.commit()

except Exception as e:
    handle_failure(msg, e)
    consumer.commit()  # skip it
    
    Key: commit even on failure to avoid loop
 
 
=> Dead letter queue
    
    -> Send message to another queue
    
    main flow continue


=> Retry before giving up 
   
   main topic -> retry 1 -> retry 2 -> give up       


"""