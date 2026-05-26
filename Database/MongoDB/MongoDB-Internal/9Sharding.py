"""
=> Sharding 
    
    -> Split data across multiple machine to scale horizontally
    
    -> why sharding 
        
        Single machine / server has limits
          
          RAM 
          DISK 
          CPU
        
        Vertical scaling hit ceiling

-------------------------------------------------------------------------------------------------

=> Sharded Cluster Architecture 
    
    A mongoDb sharded cluster has 3 main components
    
    1. Shards 
        
        -> Store acutal data
        
        -> Each shard = replica set 
   
    
    2. Config Server 
        
        -> Store meta data
        
        -> Know where data lives 
    
   3. Router (Mongos)
   
       -> Entry point for queries 
       -> Routes Request to correct shard 

---------------------------------------------------------------------------------------------

=> How data is distributed 

    -> Shard Key
        
        Field used to decide where data goes
        
    -> mongodb use shard key to 
          split data
          routes queries

-------------------------------------------------------------------------------------------------

=> Sharding Methods
       
       1. Range Base Sharding 
          
          A-M -> Shard 1
          N-Z -> Shard 2 
          
        
        hotspot problem (one shard overload)
     
     
     2. hash-based sharding 
         
         hash(user_id) → distribute evenly
         
         balanced distribution 
         
         poor range queries 
     
     3. Chunnks 
          
          -> data is split into chunks 
          
             chunk 1 -> shard A
             
             chunk 2 -> shard B
             
             chunk size = 64 Mb    
          
          -> Balancer 
              
              mongodb automatically move chunks between shards


---------------------------------------------------------------------------------------

=> Query Routing 
    
    db.find({user_id : 1})   
    
     mongos send to one shard , fast 
     
     
    db.find({"age" : 22})
    
      mongos send to all shards , scatter-gather problem , slow and expensive

=> Good shard key 
   
    1. High Cardanility 
    2. Even distribution 
    3. Used in queries


=> Bad Shard key 
    
    1. Low cardinality (gender)
    2. cause hotspot 
    3. Not used in queries                       
                                
           
         
                              


"""
