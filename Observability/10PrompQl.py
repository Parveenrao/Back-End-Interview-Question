""" 
=> Eror rate queries

   1. Basic error rate query 
        
        sum(rate(http_request_total{status = ~"5.."}[5m]))
        /
        sum(rate(http_request_total[5m]))
     
     -> This gives you 0.02 
    
    2. Convert to percentage 
             
        (sum(rate(http_request_total{status = ~"5.."}[5m]))
            /
        sum(rate(http_request_total[5m]))
        ) *100
    
    3. Trigger Alert if error rate > 5 % 
        
         (sum(rate(http_request_total{status = ~"5.."}[5m]))
            /
        sum(rate(http_request_total[5m]))
        ) > 0.05
    
    5. Error rate by service     
        
         (sum(rate(http_request_total{status = ~"5.."}[5m])) by (service)
            /
        sum(rate(http_request_total[5m])) by (service)
        ) > 0.05
            
    
    6. SRE style 
                   
                   (
          sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
          /
         sum(rate(http_requests_total[5m])) by (service)
         ) > 0.05
         AND
        sum(rate(http_requests_total[5m])) by (service) > 10    
        
        Alert if service 
        
        1. has more than 5% percent errors
        2. And recevingin more than 1-re/sec     


"""