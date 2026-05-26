""" 
=> Quantile 
     
     -> We have latency like that 
        
        100ms , 120ms, 200ms , 300ms , 2s, 3s
        
        -> how bad it for users , avergae wont telll
    
    -> we Need 
       p90 = normal user
       p95 = slow user 
       p99 = wrost user


------------------------------------------------------------------------------------

=> Example 
   
   -> Suppose my bucket 
       
       le = "0.1" -> 20
       le = "0.5" -> 70
       le = "1.0" -> 90
       
       le = "+inf" -> 100 
       
       total 100 request
    
    1. 95% of 100 = 95th request
    2. Find where 95 lies  , <+inf
    
    3. so p95 is between 1.0 and +inf              


"""