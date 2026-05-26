""" 
=> Distributed Task 

@celery_app.task(
    bind=True,
    autoretry_for=(ConnectionError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
    rate_limit="5/s"
)
def call_payment_gateway(self, data):
    ...
    


1. @celery_app.task()  
    
    -> Convert python object into celery task

2. Bind = True
   
   -> Give access to self(task instance)

3.  autoretry_for=(Exception,)
    
    -> auto retry if exception happens
    
    autoretry_for=(TimeoutError, ConnectionError)

4. retry_backoff=True
    
    -> Enable exponential backoff
    
    1st retry → 1s
    2nd retry → 2s
    
    3rd retry → 4s    
  
5. retry_kwargs={"max_retries": 3}

    -> Limits retry attempts

        After 3 failures → task is marked FAILED

        Without this → retries can go forever (bad idea)    

6. rate_limit="10/m"

   -> Limits task execution rate

       10 tasks per minute        
             

"""