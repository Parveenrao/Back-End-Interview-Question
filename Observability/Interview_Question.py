""" 
=> What is Prometheus 
     
     -> Prometheus is an open source monitoring and alerting system tool
     
     -> It is a tool that collects , stores and analyze metrics(number over time) from your system and applications


-------------------------------------------------------------------------------------------------------------------------

=> Why prometheus
   
   
   1. Monitoring system health 
       
       -> Prometheus continuously gather metrics 
       -> Is server overloaded 
       -> is your app slower 
       -> are error increasing
   
   
   2. Powerful Query language 
       
       -> It used its own query language (Prompql)
       
       -> Analyze trends
       -> Aggregate data
       -> Find anomalies
   
   3. Alerting 
      
      -> IF error rate > 5% for 2 minutes  , send alert 
      
      -> integrate with tool
         
         Alertmanager , slack , PagerDuty
   
   4. Time - Series database
      
      -> Prometheus store data as time-series
            timestamp → metric value
            
            10:00 → CPU 40%
            10:01 → CPU 55%
            10:02 → CPU 80%           
   
   5. Pull based model 
       
       -> Prometheus pulls data from services via HTTP endpoints(/metrics), which
  
  
  
  
  
  
  Prometheus is used to monitor systems and applications in real time, detect issues early, and trigger alerts when something goes wrong.                      



"""