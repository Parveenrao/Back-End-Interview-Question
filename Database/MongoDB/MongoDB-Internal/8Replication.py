""" 
=> Replication 
    
    -> Keeping multiple copies of data across server for high availability and fault tolerance

-----------------------------------------------------------------------------------------------------

=> Replica Set
     
     -> MongoDB Cluster Use ReplicaSet
     
     Primary    -> handle write
     Secondary  -> replicates data
     Arbiter    -> votes in election

-----------------------------------------------------------------------------------------------------      

=> Working 
   
   1. Write on Primary 
      
      db.users.insertOne({name : "Parveen"})
      
      goes through ->  write path -> journal -> acknowledgment
   
   2. Oplog (Operational Log)
        
        -> Primary records every write in , oplog(special capped collection)
        
               {
                 "op": "i",
                 "ns": "db.users",
                 "o": { "name": "Parveen" }
                }  
        
        -> Replication is Not copying full data 
         
         it replay operations from oplog 
   
   3. Secondary Sync
       
       -> continuously read oplog
       -> apply operation                   
              
              
              Primary → Oplog → Secondary → Apply changes
   
   4. Replication Lag 
       
       -> Difference between primary and secondary
       
       -> Cause:
           
           hevay write 
           slow network 
           slow secondary        

----------------------------------------------------------------------------------------------------------------

=> Read Preference  
    
    -> MongoDb allows reads from 
    
    1. Primary(default)
    
        stronger consistency
        Higher load 
    
    2. Secondary 
        
        load distribution
        stale data 
    
    3. Modes 
        
        parimary 
        secondary
        primarypreferred
        secondarypreferred

-----------------------------------------------------------------------------------------------------------

=> Failover 
    
    what happen if primary crash
    
    1. Election start 
        
        Replica set runs election using similar to RAFT
    
    2. New primary selected
        
        Node with latest data wins
        majority votes required 
    
    3. CLient redirect 
        
        Applications start writing to new primary
    
    4. Downtime 
        
        few seconds

------------------------------------------------------------------------------------------------------------

=> Consistency Model 
     
     MongoDb allows eventual consistency(default)
   
   
   -> for stronger consistency
                 
                 readConcern: "majority"
                 writeConcern: "majority"                              
                
    
                  
"""