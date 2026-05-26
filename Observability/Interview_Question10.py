""" 
=> Joins In Prometheus
    
    -> Combining two metrics based on matching labels
    
       Metric A -> Request rate
       Metric B -> instance metadata (region)

----------------------------------------------------------------------------------------

=> Vector Matching 
    
    -> We control using on
        
       1. on -> match only specific label
        
           match only on instance , ignore other label
        
            matric A * on(instance) metric B 
       
       2. ignoring -> ingnore specific label
           
           metric A *ignore(job) metric B  
           
           match everything except job


----------------------------------------------------------------------------------------------

=> Calculate error rate per region 
         
         
         rate(http_request_total{status=!"5..}[5m])
         /
         rate(http_request_total[5m])
         
         * on(instance)
         
         group left(region)
         instance_info                


"""