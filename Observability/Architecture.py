""" 
=> Target 
     
     Any service that  expose metrics for scrape
     
     -> Prometheus is behave like a clinet
         
         send request 
         read metrices 
         store them 
  
  
  -> How prometheus find target 
     
     1. static target 
     
     you tell promethus directly in yaml file 
     
     2. Service Discovery 
        
        -> Kubernetes 
        
        -> Docker find running container
        
        -> Aws EC2

----------------------------------------------------------------------------------------------------

2. Exporter 

   An exporter is a small service that expose metrcies  in Prometheus format
   
   It translates system/app data → /metrics endpoint
   

 -> Why exporter
    
    Most system (linux, Mysql ,Redis)  dont speak prometheus format
    
    exporter like a translator 
    
    System (CPU, DB) → Exporter → /metrics → Prometheus

--------------------------------------------------------------------------------------------------  
  1. Node Exporter  
     
     CPU usuage 
     Memory 
     Disk 
     Network
                        
---------------------------------------------------------------------------------------------------

=> Types of Exporter 

   
   1. System Exporter  
   
       Node exporter = os metrices 
       cAdvisor =  container metrics
   
   2. Databse Exporter 
      
      Mysql Exporter 
      Redis Exporter 
   
   3. Custom exporter                                



Exporter → exposes metrics  
Service Discovery → finds exporter  
Prometheus → scrapes exporter

-----------------------------------------------------------------------------------------------------------

3. Prometheus server
  
  -> Brain of the system 
 
   1. Scrape metrics (pulls metrics )
   2. Stores data 
   3. Run queries (PrompQl)
   4. Trigger alerts 
   
  
  -> Scrap Manager 
     
     1. Reading ymal file 
     2. Find target 
     3. Sending HTTP Request
    
   GET http://localhost:8000/metrics
   
   
   Runs after few second 
   
   scrape_interval: 15s
  
  -> TSDB (Time Series Data)
      
      this is where data is stored
      
      metric + labels + timestamp + value
      
      metric + labels + timestamp + value
   
   -> Query Engine (PrompQL)
   
       Analuze data 
       
       rate(http_requests_total[1m])
   
   -> Rule Engine 
   
       IF error_rate > 5% → trigger alert
   
   -> Alert flow 
       
       Prometheus does not notify directly
         
         promethes -> Alert manager -> Slack
    
Exporter → Target → Scrape Manager → TSDB → PromQL → Alert → Alertmanager



-----------------------------------------------------------------------------------------------------------------

-> Limitations 

Why Prometheus alone is NOT enough

Prometheus is great, but:

❌ Single node
❌ Limited storage (local disk)
❌ No easy horizontal scaling
❌ Data loss risk    
                        
-----------------------------------------------------------------------------------------------------------------------

=> Full flow 


 Step 1: Your App / Exporter generates metrics

        -> Example (Python app):

        -> http_requests_total 10

        -> Exposed at:

            /metrics

           This is your data source

Step 2: Target is defined

          In prometheus.yml:

         scrape_configs:
             - job_name: "my_app"
              static_configs:
               - targets: ["localhost:8000"]
        
         Now Prometheus knows:

        “I need to monitor this service”

Step 3: Prometheus scrapes data

             Every few seconds:

            GET http://localhost:8000/metrics

            This is pull model
             If this fails → no data collected


Step 4: Data stored in TSDB

             Stored as:

             metric + labels + timestamp + value

             Example:

             http_requests_total{method="GET"} 10 @ 10:00

             Time-series = data over time

Step 5: Query using PromQL

          Example:

          rate(http_requests_total[1m])
         
          Answers:

         Requests per second
         Trends
         Patterns

          Used by:

          You (debugging)
          Grafana dashboards

Step 6: Alert rules evaluated

            Example rule:

            IF error_rate > 5%

             Prometheus continuously checks this

Step 7: Alert sent to Alertmanager
          Prometheus → Alertmanager
          Prometheus doesn’t notify directly

Step 8: Notification sent

            Alertmanager sends to:

             Slack
             Email
             PagerDuty

             Example:

              High error rate in payment service
              Full Flow (compress this in your brain)
                 
                 
                 App/Exporter → /metrics → Prometheus scrape → TSDB → PromQL → Alert → Alertmanager → Slack                        
   
"""