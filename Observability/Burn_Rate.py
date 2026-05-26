"""" 
=> Burn Rate 
     
     -> How fast you are consuming your error budget 


----------------------------------------------------------------------------------------------

=> Example 
   
   Burn rate  = Current Error rate / Allowed Error rate 
   
   SLO = 99%
   Allowrd errors = 1%
   
   
   if current rate = 5%
    
    You are burning budget 5x faster than allowed


----------------------------------------------------------------------------------------------------

=> Interpret Burn Rate 
    
    1x   --->   normal (within SLO)
    >1x  --->   budget draining
    >10x --->   serious issue
    >50x --->   outage-level


-----------------------------------------------------------------------------------------------------

=> PrompQL 
    
    1. Error rate 
        
        sum(rate(http_request_total{status =!"5..."}[5m]))
        / sum (rate(http_request_total[5m])) 
    
    
    2. Burn rate (for slo = 99%)
    
        Allowed Error = 0.01
        
     (
      sum(rate(http_requests_total{status=~"5.."}[5m]))
      /
    sum(rate(http_requests_total[5m]))
    ) / 0.01                



---------------------------------------------------------------------------------------

=> Fast burn rate 
    
    -> is the system breaking right now 
    
    -> Short windo (5 min)
    
    -> Detect sudden spike / outages

=> SLow burn 
   
   -> is the system slowly degrading over time 
   
   -> long window (1 hour)
   
   -> Detect persistent issue



=> Example 
  
  SLO = 99 percent  , error budget = 1%
  
  Case 1 , fast burn
      
      error rate = 10 % percent for last 5 minutes 
      burn rate  = 10/1  => 10x system is failing 
  
  
  Case 2 , slow burn 
     
     error rate  = 1.5% for last 1 hour
     
     Burn rate = 1.5 / 1 = 1.5x
     
     
     Not crashing, but slowly draining budget           
"""