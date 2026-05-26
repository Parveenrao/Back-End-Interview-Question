"""   
=> Logstash 
    
    -> Data processing pipeline tool that collects , transform ,  and send data (mostly logs) to another system like ES
    
    Logstash = Log Collector + cleaner + transporter 
    
    
----------------------------------------------------------------------------------------------------------------------------

=> Why we need logstash 
     
     -> logs come from apps, server , database , API 
     -> Each log format is differnt , CSV , JSON , TEXT 
     -> Logs are messy and unstructured 
     
   -> Logs are hard to search , hard to analyze , different format , no central place
   
   
   -> Logstash solves this by:

           Collecting logs from everywhere
           Cleaning & structuring them
           Sending them to a centralized system    


-------------------------------------------------------------------------------------------------------------------

=> Working of Logstash 
    
    -> Logstash working in 3 stage 
    
  1. INPUT  --->  Where data comes from
      
      -> Logstash collect data from 
           Files(logs.txt) , Database , kafka , System logs
      
             input {
                  file {
                path => "/var/log/app.log"
                }
                  }     
        
        
    2. FILTER --->  Transform data / Process data 
    
          -> Parse logs , Extract fields , Remove useless data 
   
    3. OUTPUT --->  Where data goes     
         
         -> Send processes data to monitoring tool ,Database , file      
"""