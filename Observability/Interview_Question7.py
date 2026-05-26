""" 
=> What is time-series in prometheus 
    
    -> A sequence of data points (values) for a specific metric , recorded over time and identified by a unique set of lables 
    
    -> Example , we are tracking CPU usage 
        
        every 15 second , record its value 
        
        become time series
        
        10:00 -> 45%
        10:20 -> 50%
        10:30 -> 60%
        
        
        Time series is uniquely defined by metric_name + label 
        
        http_requests_total{method="GET", status="200"}
        
        This combination = one unique time series
        
        http_requests_total{method="GET"} 100
        http_requests_total{method="POST"} 50
        
        two time series , because labels are different

------------------------------------------------------------------------------------------------

=> Label in Prometheus 
   
   -> Label is a key-value pair attached to metrics that provide context and uniquely identify a time series
   
   -> Labels = metadata that tells you "what exactly the metrics is about
   
   
   http_requests_total{method="GET", status="200"} 1024
   
   http_request_total -> metric 
   
   methods = "GET" labels 
   status = 200    lables
   
   Together these labels describe metrics 

=> Why lables 
    
    1. Identify data precisely
    
        without lables , we dont know whiche endpoint , which method , which server 


----------------------------------------------------------------------------------------------------------------

=> Lable Cardanilty 
    
    -> No if unique label  combinations created for a metric 
    
    more unique label values -> more time series -> higher cardanilty
    
    
    http_requests_total{method="GET"}
    http_requests_total{method="POST"}         
    
    2 unique label sets = cardinality = 2
    
    
    -> A time series is defined by
       
       metric name + lable
   
   
   -> High cardinality labels
         http_requests_total{user_id="123"}
         http_requests_total{user_id="124"}
         
         
           1 million users -> 1 million time series
           
           called high cardinality
   
   -> Why high cardanlity is dangerous 
      
      1. Memory explosion
          
          -> Prometheus store each time series in memory 
          
          more series = more memory
          
      2. Slow queries 
         
         -> prom scan all series 
         
           high cardinality = slow dhashboard
      
      3. System instability 
          
          Crash prometheus 
          Cause OOM(out of memory)
                           
                           
                                     
--------------------------------------------------------------------------------------------------------------------

=> Sample In Prometheus 
    
    -> A sample is a smallest unit of data in prometheus 
        
        sample = (timestamp , value) for specific time series
        
        
        -> each time prometheus scraps , it records one data point
        
         that data point called  = sample

"""