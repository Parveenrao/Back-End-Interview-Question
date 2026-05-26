""" 
=> Function in PrompQl
    
    -> Function take metrics (instant or range vector) and return processed results

-----------------------------------------------------------------------------------------------------

1. irate() 
     
     -> instant rate per second, use only last 2 points 
        
        irate(http_request_total[5m]) 
         
         -> look only last value and previous value 
     
     -> used when real time spike , sudden traffic jump  , debugging issue
     
     -> Not to use 
         
         1. Dashboard  -> because it is noisy 
         2. Alerts      -> gave false alert 
----------------------------------------------------------------------------------------------------------------
2. sum()
     
     -> add multiple time series into one 
     
     -> give me total across services , pods, instances 
     
     sum(http_total_request)
     
     -> add request 
         1. server 1
         2. server 2
         3. server 3   give me total request 
    
    -> Sum not use alone 
        
        1. with rate 
           
           sum(rate(http_requests_total[5m]))
           
           total request per second across all instances over last 5 minutes
        
        2. per service 
            
            sum(rate(http_total_request[5m])) by service
        
        3. by label() 
        
           sum(rate(http_total_request[5m])) by (status)
             
             status = 200 
             status = 500
        
        4. Error rate 
           
           sum(rate(http_total_request{status = "500}[5m]))
           /
           sum(rate(http_request_total[5m])) 
        
        5. Per Endpoint 
           
           sum(rate(http_requests_total[5m])) by (endpoint)

----------------------------------------------------------------------------------------------------------------

3. Avg() 
    
    -> average of multiple time series
   
  
  -> avg(rate(http_requests_total[5m])) 
     
     average request/sec per instance  
   
   -> avg(cpu_usage) by (service)
        
        average cpu_usage per service 
   
   -> avg(rate(http_request_total[5m])) by (endpoint)
       
       average load per endpoint (per instance)
    
   -> avg(cpu_usage) 
       
       average cpu across cluster 

----------------------------------------------------------------------------------------------------------

4. Max() 
    
    -> returns the highest value among multiple time series
     
     which server / endpoint is under the most load
    
    -> max(rate(http_request_total[5m]))
        
        server handling highest request/sec
    
    -> max(cpu_usage) by (service)
        
        highest cpu per service
    
    -> max(rate(http_requests_total[5m])) by (endpoint)
         
         for each endpoint 
           find the busiest                                      
               
                          
                   

"""