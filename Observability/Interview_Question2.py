""" 
=> How prometheus collect metrics 
   
   1. Target expose metrics
   
      -> Your application  or system expose an HTTP endpoint
          http://app:8080/metrics
   
   2. Prometheus configuration define target 
     
      -> In prometheus.yml, you define where to scrape from:
                            
                            scrape_configs:
                             - job_name: "my-app"
                                 static_configs:
                                   - targets: ["app:8080"]     
                        
                        This tells Prometheus:
                         “Go to this endpoint and collect metrics”    
   
   3. Service Discovery 
          
          -> Instead of static config , Prometheus can auto-discover
             
             kuberneted pods 
             EC2 instance 
             Containers
          This is critical in microservices—targets keep changing.
   
   4. Scraping 
       -> At a fixed interval (default 15 seconds)
       
       Prometheus 
       
       1. Send HTTP request GET request -> /metrics
       2. Recieve metrics text 
       3. Parse it 
       4. Adds timestamp
       5. Store it
       
       This process is called scrapping
   
   5. Storage in TSDB
         
         -> After scraping , data is stored like
         
         metric_name{label="value"} → timestamp → value
         
         http_requests_total{method="GET"} → 1713950400 → 1200
   
   6. Exporter 
       
       -> Not all system support /metrics
       
       so we can use exporters 
       
       1. Node exporters = system metrics
       2. Mysql Exporter = database
       3. Blackbox  Exporter -> uptime
    
   7. Pull vs Push Model
       
       -> Proemtheus is a pull model
       
       -> push model  , Apps sends data to server                                                       


"""