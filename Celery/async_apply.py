""" 
=> async_apply 
    
    -> is an another method to send task 
    -> gives you full control 
    
       1. schedule task
       2. retry handling
       3. routing (queues)
       4. countdown / eta 
       5. set task priority
"""
""" 
1. Basic Syntax 
    
    task.apply_async(args =[] , kwrgs = {})

2. Run task after delay 
   
   add.apply_async((2, 3) , countdown = 10)
   
3. Retry automatically 

        add.apply_async((2, 3), retry=True, retry_policy={
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 2,
    'interval_max': 10,
        })

4. send to specific queue 
        
         add.apply_async((2, 3), queue='high_priority')      
         
         payment -> high priority 
         emails -> low priority 

5. Set task expiration 
   
   => if not execute , expire / discard 
   
       add.apply_async((2, 3), expires=60)              
       
               
"""


