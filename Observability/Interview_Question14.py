""" 
=> Scaling And Production 
   
   
   1. Federation 
       
       -> Instead of one gaint prometheus handling everything you run multiple prometheus server , and then higher-level
          prometheus server collects data from them
          
        -> Prometheus A = scrape app/service
        -> Prometheus B = Scrape prometheus A (using federation)
     
     
     -> WOrking 
        
        1. Prometheus expose a special endpoint , /federate
        
        2. Parent Prometheus send a query like
                    /federate?match[]=up
                    
                    Give me only the metrics matching up
                    
                    Then it stores those metrics again in its own TSDB
      
      
      -> Types of Federation
         
         1. Hierarchical Federation 
             
             App -> Prometheus(regional) -> Prometheus(global)
             
             Lower-level prometheus , detailed data 
             Higher-level prometheus , aggregrate / imported data only
         
         
         2. Cross service federation 
            
            -> One prometheus pulls specific metric from another
            
            -> used when service are another
            
            scrape_configs:
                - job_name: 'federate'
                  scrape_interval: 15s
                  honor_labels: true
                  metrics_path: '/federate'
    
                  params:
                     'match[]':
                     - '{job="node-exporter"}'
    
                  static_configs:
                     - targets:
                     - 'prometheus-source:9090'   
       
       -> Federation helps 
       
           1. Reduce load 
           2. Avoid single point of failure
           3. handle large scale data 

====================================================================================================

=> Remote Read & Remote Write 
    
    1. Remote Write (Push Model)
        
        -> Prometheus send (pushes) its metrics to an external ssytem
        
        -> Instead of storing everything locally , prometheus stream data to system like 
            
            Thanos, Cortex 
            
            remote_write:
                - url: "http://remote-storage:9201/api/v1/write"      
        
        -> Why use it
               Long-term storage (Prometheus local TSDB is limited)
               Global aggregation across clusters
               Durability (data survives Prometheus crash)     
    
    
    2. Remote Read 
         
         -> Prometheus fetches (pulls) data from external storage when querying
          
         -> If data is not in local TSDB → it asks remote storage.
         
         remote_read:
            - url: "http://remote-storage:9201/api/v1/read"      
          
          -> Slower query 
          -> High latency                
                                        
               

"""