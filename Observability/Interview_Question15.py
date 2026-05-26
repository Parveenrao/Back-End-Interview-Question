""" 
=> Recording Rules 
     
     -> Pre-compute and store the result of PrompQL query as a new time series

-----------------------------------------------------------------------------------------

=> Alerting 
    
    -> Alert rules are about taking action when something goes wrong
    
    -> Alerting rules = condition that trigger alert when a metric crosses a threshold
    
    
    
                        - alert: HighCPUUsage
                            expr: avg(rate(node_cpu_seconds_total[5m])) > 0.9
                            for: 2m
                             labels:
                               severity: warning
                            annotations:
                                   summary: "CPU usage is high"    
                                   
                            -> expr = condition(prompql) 
                            
                            -> for  = avoid false alert 

---------------------------------------------------------------------------------------------------

=>  AlertManager 
      
      -> Component that recieve alert from prometheus and decide
         
         who should be notified
         When
         how often
    
    
    -> Flow 
       
       1. Prometheus Fire An Alert 
            
            -> Condition become true , alert is send to alertmanager 
       
       2. Alert arrive with labels 
       
       3. Grouping 
           
           -> Instead of sending 100 alerts 
           
           Alertmanager groups them 
           
           group_by: ['alertname']
           
           “One notification: HighCPUUsage (100 instances affected)”
       
       4. Deduplication 
           
           -> if we run , 2 prometheus server 
           
           Both send same alert 
           
           alert manager send only one alert 
       
       5. Routing 
           
           -> based on labels        
                                       

"""