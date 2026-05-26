""" 
=> How to design Prometheus for 1M metrics

      
      1. First Principle .... Don't collect garbage
          
          -> At 1M metrics ., the biggest issue is cardinality
          
          -> Bad , user_id , request_id , (millions of user)
          
          -> Good , store aggregrate result , region , server , status 
      
      
      2. Horizontal Scaling
         
         1. Functional sharding (Split by service)
         
            Prometheus -1  -> Kubernetes Cluster A
            Prometheus -2  -> Kubernetes Cluster B
            Prometheus -3 -> Database
            Prometheus -3 -> Infra (node)
     
     
     3. Add global query layer
        
        -> Aggregrate multiplee prometheus instance 
        
        -> Provie global querying
        
        -> handle dedcuplication
     
     
     4. Remote storage 
        
        -> Prometheus local storage is not for 1M metrics
        
        use
        
        -> Object storage (s3)
     
     5. Recording Rules
         
         -> Raw queries on millons of series 
         
         -> SO you pre-compute
         
         rate(http_requests_total[5m])
         
         store as 
         
         job:http_requests_rate5m
         
         
         
         
         
         
            +------------------+
            |   Grafana        |
            +--------+---------+
                     |
              Query Layer
          (Thanos / Cortex / Mimir)
                     |
            +--------+------+--------+
            |        |               |
          Prom-1   Prom-2         Prom-3
            |        |               |
          Targets   Targets        Targets                  



"""