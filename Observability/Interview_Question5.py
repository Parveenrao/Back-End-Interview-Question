""" 
=> Exporter 
     
     -> An exporter is a bridge that convert metrics from a system into Prometheus - readable  format and expose them via
        a /metrics endpoint
        
        
        Exporter = translator → system data → Prometheus metrics
     
------------------------------------------------------------------------------------------------------------------------------

=> Why exporter 
   
   Not every system natively support prometheus
   
   -> Linux doesnot expose metrics
   
   -> Mysql does not expose prometheus format
   
   -> network service doesnot expose


-----------------------------------------------------------------------------------------------------------------------------

=> Flow 
    
    1. Exporter read data from system (OS , DB)
    2. Convert it into prometheus format 
    3. expose metrics /endpoint 
    4. Prometheus scrap it

---------------------------------------------------------------------------------------------------------------------------

=> Common Exporter 
   
   1. Node exporter 
       
       -> CPU , memory  disk , network 
       -> used for server
   
   2. Mysql exporter 
      
      -> queries  , connections , replication sets 
   
   3. Blackbox exporter 
              HTTP, DNS, ping checks
              Used for uptime monitoring              
         

"""