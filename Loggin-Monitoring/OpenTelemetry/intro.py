""" 
=> OpenTelemetry 
    
    -> It is tracing system inside your app
    
------------------------------------------------------------------------------------------------------------

-> Working 
      
      1. user send request 
      2. that request goes through mltiple service (API-DB-Cache)
      3. OpenTEl record what happend each step 


-----------------------------------------------------------------------------------------------------------

-> Optel does three things
     
     1. Metrics
        
        -> Number over time 
           ex = cpu usage , request count
           
           how many request per second
     
     2. Logs
        
        -> Something failed here
     
     3. Traces 
         
         -> Trace a request across service 
    
    -> Example 
    
        Request Start
           ├── FastAPI (200ms)
           ├── DB Query (1200ms) ❌ slow
           └── Redis (50ms)                    
        
        DB is bottleneck

"""