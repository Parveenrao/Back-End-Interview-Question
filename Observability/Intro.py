""" 
=> Observability 
    
    -> Observe != logs & dashboard

    -> It means 
       
       can you undertand whats happening inside your system just by looking at outputs
       
    -> If system breaks at 
       
       1. What failed 
       2. Where did it fail 
       3. Why did it fail 
       4. How bad is it 

--------------------------------------------------------------------------------------------------------

=> Pillars of observability 
    
    1. Logs(Events)
        
        -> Errors
        -> Request 
        -> Debug info 
    
    {
  "level": "ERROR",
  "message": "DB connection failed",
  "user_id": 123,
  "timestamp": "2026-04-06T10:00:00Z"
}


2. Metrics (Number over time )

    -> How system behaving 
    
    -> CPU usages
    -> Request Rate 
    -> Error latency
  
  api_requests_total = 1200
  error_rate = 2%
  latency_p95 = 300ms        
  
  
3. Traces (Request Journey)
   
   -> Where did it acutually slow 
   
   User → API → Auth Service → DB → Payment Service
   
   -> Each step latency  
       
       


"""