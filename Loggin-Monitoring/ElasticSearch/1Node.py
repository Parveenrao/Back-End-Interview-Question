""" 
=> Node 
    
    -> One running instance of elasticsearch 
    
    -> One process , one machine , part of cluster 


-----------------------------------------------------------------------------------------

=> Function of Node 
    
    1. Store data (shards)
    2. handle queries 
    3. talks to other node 

-----------------------------------------------------------------------------------------

=> Types of Node 
     
     1. Master Node 
         
         -> Control the cluster 
         -> manages clusters state
         -> Decide shard allocation 
         -> handles node join/leave
     
     2. Data Node 
         
         -> Store actual data 
         -> Hold shards 
         -> run queries
         -> does indexing 
         
     3. Coodination Node
         
         -> Handle request
         -> Recieve search request 
         -> send to all nodes 
         -> merge result 
      
      -> Every node can act as this by default 
     
     4. Ingest Node
         
         -> Pre-process data before indexing 
          
         -> pipeline 
         
         -> transformation


---------------------------------------------------------------------------------------------

=> Cluster 
   
   -> A group of nodes working together as one system 
   
   -> share data , distribute load , provide fault tolerance


=> what does cluster do 
    
    1. Data Distribution 
       
       -> Split index into shards 
       -> spread shard across node 
    
    2. Load balancing
    
       -> Queries handling by multiple node 
       
       -> faster response 
    
    3. Fault tolerance 
        
        -> if one node dies = system still work                                       

"""