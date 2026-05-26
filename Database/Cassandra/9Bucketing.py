""" 
=> Partition Size 
    
    A partition = all rows sharing same partition key
    
    Ideal (10-50mb)
    
    acceptable (upto 100mb)
    
    danger zone (100mb - 1gb)
    
    very bad(> 1gb)
    
  
  -> WHy large partition is a problem 
     
     1. Read latency explode
        
        when we query a parition , cassandra may scan large sstable
        more disk i/o , slower query
     
     2. Compaction expensive 
         
         cassandra compaction in background
          
          large partition => expensive compaction 
          
          CPU spike , Disk pressure , latency issue
     
     3. Memory pressure
        
        -> index + metadata loaded in memory 
        -> bigger partition  -> more memory used

--------------------------------------------------------------------------------------------------

-> Control 
    
    
    1. Time-based bucketing
    
    PRIMARY KEY ((chat_id, day), message_id)
    
    split data over time

-> Random bucketing 

         PRIMARY KEY ((chat_id, day, bucket), message_id)            
                    

"""