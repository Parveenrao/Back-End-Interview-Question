"""  
=> Worker in Celery
   
   -> A worker in celery is a separate process that 
      
      1. listen to queue 
      2. pick up task
      3. executes them 

----------------------------------------------------------------------------------

=> Flow 
   
   1. Task goes to redis queue 
   2. Worker is runing in background 
   3. Worker pick task 
   4. Worker execute function 

------------------------------------------------------------------------------------------

=> Start a worker 
         
         celery -A app.tasks.celery_app worker --loglevel=info  
         
     -> -A define where is celery_app defines

=> Concurrency 
     
     -> how many task a worker runs at same time 
     
     celery -A app.tasks.celery_app worker --concurrency=4

=> Multiple Queues 
   
   celery -A app.tasks.celery_app worker -Q high_priority --concurrency=4
   
      -> for high priority like payments 
   
   
   celery -A app.tasks.celery_app worker -Q low_priority --concurrency=2     
               
               - low priority like , email sending

=> Scaling 

         celery -A app worker --autoscale=10,3     
         
         min = 3 worker 
         max = 10 workers 

=> Prefetch 

   -> Worker grab many task in advance , other idle 
   
   -> prefetch ensure fair distribution 
   
   
   celery_app.conf.worker_prefetch_multiplier = 1                            
                  

"""