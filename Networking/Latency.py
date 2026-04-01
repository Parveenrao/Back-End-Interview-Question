"""  => Latency 
    
           -> Time taken for data to travel from source to destination 
           
           Example  -> Clinet -- server -- response 
               
                       if the request take 120 ms , the latency is 120ms 
           
           =>  Latency  -> time delay between request and resposne 
           
    
    => Example of latency in web request 
    
       -> suppose u open a request 
          
          Browser --> API server  -> database  --> API server -> browser 
          
          Network travel: 40 ms
          Server processing: 20 ms
          Database query: 30 ms
          Response travel: 40 ms       
          
          Total latency --> 130 ms


   => Total latency formula  = Latency =
                                       Propagation delay
                                       + Transmission delay
                                       + Processing delay
                                       + Queueing delay






"""