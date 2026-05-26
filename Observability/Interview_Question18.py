""" 
=> Design SLO / SLI 
 
    
    -> Typical Dimension 
       
       Latency
       Availability
       Error rate
       
    
    These become your SLIs(Servie Level Indicator)

-------------------------------------------------------------------------------------------------------

-> Define SLI (What you measure)
    
    1. Availability 
         
         -> Percentage of successfull request
         
           availability = successfull request / total request 
    
    
    2. Percentage of Request under threshold (< 200ms)
        
        latency = request below threshold / total request
    
    3. Error  Rate SLI
        
        -> Percentage of failed request 
           
           error rate = error request / total request


-> Define SLO
     
     Convert SLI into goals
      
      Availability , 99.9% over 30 days
      
      latency 95% < 200ms
      
      Error rate < 0.1% 
      
      -> These are busniess commitment . not technical guess

----------------------------------------------------------------------------------------------

=> Error budget 
    
    If SLO = 99.9%  
    
    Error budget = 1-SLO
    
    99.9% SLo -> 0.1% allowed failure


=> Burn Rate 
   
   -> How fast we are consuming error budget 
      
      
      BURN RATE = current error rate / alloed burn rate         
                
                           


"""