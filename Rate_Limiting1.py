"""        1. Fixed window Rate Limiting Algorithm    
         
           -> System allow a fixed no of request in a fixed time interval 
           
           
           => Example   
           
                ->  5 requests per minute
                
                    Request Arrives 
                    
                    
                    12:00:01 → request1 → allowed
                    12:00:05 → request2 → allowed
                    12:00:10 → request3 → allowed
                    12:00:15 → request4 → allowed
                    12:00:20 → request5 → allowed
                    12:00:30 → request6 → rejected

            AT ->  12:01:00
            
            counter reset
        
        
        => Problem   
           
            -> Brust Traffic problem  
            
               limit = 100 req/min 
               
               12:00:59 -> 100 request
               12:00:01 -> 100 request 
               
               2 -> second 200 request     




"""      