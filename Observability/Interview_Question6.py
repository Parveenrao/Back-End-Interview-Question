"""
=> Scrape Configuration
       
       -> Scrape configuration tells prometheus 
            what to scrape , where to scrape , and how often to scrape 
            
        -> It lives inside prometheus.ymal file and define how prometheus collects metrics from target 

----------------------------------------------------------------------------------------------------------------

=> A scrape configuration is a set of rules that tells prometheus which target to monitor and how collect thier metrics
          
          scrape_configs:
              - job_name: "my-app"
                 scrape_interval: 15s
                   metrics_path: /metrics
                    static_configs:
                       - targets: ["localhost:8080"]    
        
        
        1. job_name 
             
             -> Logical group of targets
             -> used a label in metrics
        
        2. targets 
            -> List of endpoint Prometheus will scrape
        
        3. scrape interval 
               
               -> How often collect metrics
               -> default 15s
            
            too high = stale data
            too low = high load
        
        4. metrics path
            
            -> endpoint path

------------------------------------------------------------------------------------------------------------

=> What happen during Scrape 
     
     1. Scheduler trigger the scrape 
         
         -> based on scrape_interval (e.g every 15s)
         -> Prometheus pick a target from  its config / service discovery
     
     2. HTTP Request is sent
            
            GET http://target:port/metrics
            
            Uses timeout (scrape_timeout)
            Adds headers if configured                                                       
            
            If this fails → scrape is marked failed
     
     
     3. Target return metrics 
                 
                 http_requests_total{method="GET"} 1024
                 cpu_usage 0.65       
           
           This is the Prometheus exposition format
     
     4. Parsing and Validation 
          
          -> Parse metrics , labels , values 
          -> validate formats 
          
          -> Reject invalid lines
     
     
     5. Labelling and Relabelling 
         
         Prometheus add label like 
          
          job
          instance
          
          Then apply labelling rules like 
          
          1. Add / remove lables
          2. Rewrite rules
          3. Drop unwanted rules
     
     6. Sample creation 
         
         -> Each metric become a sample 
         
           (metric_name + labels )  -> value + timestamp
           
           http_requests_total{method="GET", instance="10.0.0.1"} → 1024 @ t
     
     
     7. WAL (Write ahead logging)
     
        -> Before storing 
        
        Data is wriiten to WAL
        
        for crash discovery , Durability
        
        prometheus crash -> WaL help recover recent data 
     
     
     8. Stored in TSDB
        
        -> Data goes into memory chunks 
        -> Later persisted to disk block
     
     9. Alert evaluation 
         
         -> After ingestion 
            
            alert rules are evaluated                              









"""