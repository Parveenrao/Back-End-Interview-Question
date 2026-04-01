"""  
=> Celery 
   
   -> Background job processing system
   
   -> Instead of doing heavy work inside your api request , you send it to celery
   
   -> Example:
      
      User upload Image 
       
       -> Celery 
          
          1. Resize image 
          2. upload to s3
          3. sends notification


--------------------------------------------------------------------------------------------------------

=> Component 
    
    1. Producer (Your App / Api)
        -> send taks 
    
    2. Broker (Message Queue)
       
       -> Middle man (store task) , redis , rabbitmq
    
    3. Worker
        
        -> Execute task , scale horizontally
    
    4. Result, backend 
       
       -> Store result 

--------------------------------------------------------------------------------------------------------------

=> Why heav work not do in api 
    
    -> Let say user upload picture (takes 10 second)
    
        1. user waits
        2. Server blocked
        3. Bad performance
       
                                    

"""
