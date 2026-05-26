""" 
=> SLI 
   
   -> A metric that measure how your service is actually behaving
    
    -> What numbers tell me if users are happy or not

------------------------------------------------------------------------------------------------

=> SLI 1 Request Rate    
        
        
             sum(rate(http_requests_total{status!~"5.."}[5m]))
             /
             sum(rate(http_requests_total[5m]))    

   how many request are successful
   
=> SLI 2 Latency 
     
     How fast is the response
      
      p95 latency
      p99 latency


=> SLI 3 Traffic 
     
     how many request per second 
        
        rate(http_requests_total[5m])

=> SLI 4 Saturation 
     
     how close are we to limits 
     
     CPU usuage
     Memory pressure
     Disk busy


----------------------------------------------------------------------------------------------------

=> Golden Signal 
    
    1. Latency 
    2. Traffic
    3. Errors
    4. Saturation 
 
--------------------------------------------------------------------------------------------------

=> How SLI become SLO 
    
    SLi => success rate 
    
    current_rate  = 98.7%
    
    now define 
    
    slo > 99.9


----------------------------------------------------------------------------------------------------

=> Types OF SLI 
   
   1. Request Based SLI 
       
       -> % successfull request
       -> latency distribution
   
   2. Time based SLI 
       
       -> uptime over time 
   
   3. Resource based SLI 
        
        saturation (CPU , memory)            
    
             
                      

"""