""" 
=> Elastic Search 
   -> index is built on top of APache lucene Engine 
   
   
=> Structure 

Index
 ├── Shards
 │     ├── Segments
 │     │     ├── Inverted Index
 │     │     ├── Stored Fields
 │     │     └── Doc Values   
 
 
--------------------------------------------------------------------------------------------

1. Shards 
   
   -> AN index is split into multiple shards
   
   why 
   
   -> Scale horizontally 
   -> parallel search 
   -> distribute load 
 
products index
 ├── shard 1
 ├── shard 2
 ├── shard 3


=>  Each shard is actually a search engine internally 
      -> Each shard has its own inverted index 
      -> Each shard can independently search data 
   
   -> So instead of 1 big index -> ES splits into smaller pieces 

----------------------------------------------------------------------------------

=> How Document Go To Shard 
     
     shard_number = hash(document_id) % number_of_primary_shard 
     
   -> Example 
   
      number of primary_shard = 4 
      
      Document ID = "user_123
      
    1. hash("User_123) -> Some number (say = 982734)
    2. 982734 % 4 = 2
    3. Document shard 2 
    
    
    Same document_id -> Same shard
----------------------------------------------------------------------------------

=> What happen to internally 
    
    1. Client send request 
        POST/users/_doc1
    
    2.Request hit any node - called cordination node 
    
    3. That node 
        
        -> Calculate shard using hash 
        -> Find which node holds that shard 
    
    4. Send request to primary shard 
    
    5. Primary shard 
        -> stored document 
        -> update inverted index 
    
    6. Then forward to 
         
         -> Replica shard
  
  
  Client → Coordinating Node → Primary Shard → Replica Shards
  
=> Replica 
   
   -> copy of shard 
   
   -> Handle read query
   -> failover

--------------------------------------------------------------------------
Index: users
Primary Shards: 2
Replicas: 1

Total shards = 2 primary + 2 replica = 4 shards   

---------------------------------------------------------------------------

=> How Shards Are Distributed Across Nodes

       2 nodes
       2 primary shards
       1 replica

        -> Distribution:
         Node 1	Node 2
            P0	P1
            R1	R0



               Replica is NEVER on same node as primary   

-----------------------------------------------------------------------------------------------

=> What happen during seach query 
    
    -> When you run a query 
    
    1. Co-ordinate send query to 
         
         -> ALl relevant shard (primary or replica)
    
    2. Each shard 
        
        -> Runs search locally 
    
    3. Co-ordination node
        
        -> merge result 
        
        -> Return final response                                                        
"""