"""  
=> Multi-label 
    
    -> Group more than one label at the same time 

-----------------------------------------------------------------------------------------------------------

-> sum(rate(http_request_total{status = "500}[5m])) by (endpoint , status) 
     
     which server endpoint is failing


-> sum(rate(http_request_total[5m])) by (service , endpoint)
    
    traffic per service + endpoint 

-> sum(rate(http_requests_total[5m])) by (status , endpoint)

---------------------------------------------------------------------------------------------------------

=> TopK
   -> Return the top k highest value 


-> topK(5 , sum(rate(http_requests_total[5m])) by endpoint))
    
    top 5 busiest api

-> topK(3 , cpu_usage) 
    
    which machine are overload
 
-> topk(5, sum(rate(http_requests_total{status="500"}[5m])) by (endpoint))
        
        top error-producing endpoints                        


=> bottomk()
    
    -> reverse of this topk        
"""