"""   =>  Throttling 

          -> Throttling means slowing down request instead of rejecting them 
          
          -> Throttling controls the rate of incoming requests by delaying or queuing them so the system is not overloaded.
          
          Example  -> Imagine a system has capacity 10 req / sec 
          
                      we have two option 
                      
                      we can accept 10 and reject 90 (429)
                      
                      or We can processed 10 req immediately and  90 req delayed / queueing

        => Queue based throttling 
        
           -> Request goes into the queue 
           
              kafka / rabbitmq







""" 