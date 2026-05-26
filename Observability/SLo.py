"""   
=> Service Layer Objective 
    
    SLO => Internal target for service relability 
    
    -> we aim to keep system this reliable
    
    SLA -> Promise to users
    SLO -> goal for engineers


-----------------------------------------------------------------------------------------

=> You buil an api 
    
    You decide SLO => 99% of request should succeed over 30 days   


---------------------------------------------------------------------------------------------

=> SLO  is based on SLI 
     
     -> SLI success rate 
     
                sum(rate(http_requests_total{status!~"5.."}[5m]))
                / 
                sum(rate(http_requests_total[5m]))     
        
        This gives % of successful requests
    
    -> Build SLO from sli 
       
       SLO : success rate > 99


-------------------------------------------------------------------------------------------------

=> 1. Availability SLO 
        
        99% uptime 
   
   2. Latency SLO 
         
         95% of request are < 200ms
   
   3. Error rate SLO   
        
        < 1% errors                              


"""