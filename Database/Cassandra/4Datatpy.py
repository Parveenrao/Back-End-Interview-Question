""" 
=> Partition key & CLustering Key 

    
    -> IN Apache Cassandra 
       
       Primary key(A , B)
       
       Partition key = A
       
       CLustering Key = B
    
    
    
    1. Partition Key 
        
        -> Decide which store the data 
        -> Group rows into partition
        
        PRIMARY KEY (user_id, post_id)
        
        partition key = user_id
        
        
        internally  hash(user_id) = decide node
        
        -> Bad partition key 
           
           too many rows in one partition -> performance issue
           
           Hotspot problem -> same key used again and agina , one node overlaod 
        
        
        -> Good partiton key 
           
           1. High cardanality (many unique value)
           
           2. Even data distribution

--------------------------------------------------------------------------------------------------

   2. CLustering Key
       
       -> sort rows inside parition
            
            PRIMARY KEY (user_id, post_id)
            
            post_id -> clusterin key
            
       if post_id in timeuuid() , automatically sortd by time
       
       WITH CLUSTERING ORDER BY (post_id DESC);
       
       latest data come first 

-------------------------------------------------------------------------------------------------
   
   3. Composite Partition key 
         PRIMARY KEY ((user_id, category), post_id)
         
         Partition key = (user_id + category)
         Clustering key = post_id                              


-------------------------------------------------------------------------------------------------

    CREATE TABLE messages_by_chat (
    chat_id UUID,
    message_id TIMEUUID,
    sender_id UUID,
    text TEXT,
    PRIMARY KEY (chat_id, message_id)
    ) WITH CLUSTERING ORDER BY (message_id DESC);

"""