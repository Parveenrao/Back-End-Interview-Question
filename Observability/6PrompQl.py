"""  
=> Instant value 
    
    -> Give the current value of a metric at this exact moment
    
    http_total_request 


=> Filter with labels 
    
    http_request_total{status = "500"}
    
    -> only error request

=> Rgex filtering 
     
     http_requests_total{status=~"5.."}
     
     -> ALL 5XX errors

=> Range queries
    
    -> Give me data over time period ,not just one point
    
    -> what happend in last one hour / 1 day / 5 min
    
    
    http_total_request[5m] -> all request data point from last 5 minutes
    
    cpu_usage[5m]
    
    memory_usage[30s]
   
   
   rate(http_total_request[5m])
   
     -> average request per second over last 5 minutes 
     
   increase(http_total_request)
   
     -> total request in last 5 minutes
    
   avg_over_time(cpu_usage[30s])
      
      -> Avg cpu over last 5 minutes 
    
    max_over_time(memory_usage[5m])
    min_over_time(memory_usage[5m]) 
  
  
  -> when to use Range queries 
     
     1. Averages 
     2. spikes 
     3. Trend
     4. Rates       
    
                 

"""