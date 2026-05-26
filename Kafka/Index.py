""""

=> Index 
    
      -> An index is used to quickly find where a message is stored inside a log file
      
      -> Kafak store message like this 
          
           Partition Log
           
           offset | Message
           
           0          "hello"
           1           "hi"
           2            "bye"
      
      -> Kafak does not search line by line
      
      -> That would be slow for millions of msg
      
      -> So kafka keep an index file 
           
            .index file
      
      -> acutal working 
          
           Kafka store 
           
           .log file    -> acutal message 
           .index file  -> maps offset  position in log file
           
           
           -> index file 
           
           0 ->   0 
           
           100 -> 2048       
           
           200 -> 5090
           
           
           consumer ask
           
           give me offset 200 
           
           
           kafka looks in index
           
           find index bytes position 5090
           
           jump directly there in log file



"""