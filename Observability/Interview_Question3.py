""" 
=> Pull Based Monitoring 
    
    -> Pull based monitoring means the monitoring system actively request metrics from service instead of waiting for them
       to send
       
       Prometheus -> ask -> target respond
       
    
    1. Prometheus sends HTTP request to /metrics 
    2. Target return the current metrics
    3. Prometheus store them

------------------------------------------------------------------------------------------------------------------------------

=> Pull 
    
    -> Monitoring system ask for data 
    
    -> Prometheus hit endpoints every 15s
    
    -> Collects current state 
    
    -> Stores with timestamps

=> Push 
   
   -> App decide when/how to send
   
   -> Neet retry  , batching  error handling     
       

"""