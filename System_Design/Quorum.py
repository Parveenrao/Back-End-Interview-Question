""" 
=> Quorum 
     
     -> Minimum no. of nodes that must agree for something to be accepted
     
     -> In distributed System 
           
           1. Node can fail 
           2. network can break 
           3. Data can be consistent
           
          if we trust everyone , system slow , 
          
          if we trust too few , unsafe system
        
        
        so we choose in between , middle => Majority
    
    
    -> Majority Rules 
        
        For N Nodes 
           
           Quorum = Floor(N/2) + 1
          
           3 Nodes = quorum = 2
           
           5 Nodes = 3 
           
           7 Nodes = 4
           
         This is called majority quorum

---------------------------------------------------------------------------------------------------------------
=> Quorum Write
    
    -> A write is considered successful only when it is stored on enough node so that it cannot be lost or contradict
        
        later
    
    1. Client send write 
         
         put(key = x , value = 10)
       
       
    2. Co-ordinator / Leader recieve it
    
        -> In leader system , leader handle it 
        -> In leaderless  system (like cassandra) -> any node can coordinate
    
    3. Send write to replicas
        
        -> Co-ordinator send write to multiple node
           
           Node 1 , Node 2 , Node 3 , Node 4 , Node 5
    
    4. Wait for ACk
       
       -> As soons as 3 node confirm                             
                   
          System return success to client
        
        what about other node
        
          may get update later 
          
          may be temporary outdated
          
          Eventual consistency
          
  
  
  -> Why Quorum Write Powerful
      
      1. Fault tolerance 
         
         majority confirm write , Node 1  Node 2 Node 3 , so data is in thses nodes
         
         if node 4 node 5 crash , data is present / safe
      
      
      2. No single point of failure
          
          No dependency on one node
   
   
   -> Concurrent Writes 



=> Quorum Read 
     
     -> We read from enough node , so that we can trust the result is latest committed value
        
        Node = 5 
        
        Quorum  =3 
     
     -> Flow 
       
       1. CLient send Read 
       
       
       2. Co-ordinate queries mulitple node 
           
           Node 1 , Node 2 , Node 3 , Node 4  , Node 5
           
           but it only need 3 response
       
       3. Collect response 
           
           Node 1 -> 10 
           Node 2 -> 10
           Node 3 -> 20                               
           
           
           Now we have conflict
       
       4. Resolve 
           
           System pick latest versioning 
           
           .Timestamp 
           
           vector clock
           
           c = 20 is newer 
           
           retrun x = 20
         
         
         -> Critical part Read Repair
           
           After detecting mismatch
             
             System update stale node
             
             Node 1 , Node 2 ->  updated to 20
   
   
   -> Why we dont use one quorum read 
       
       because ,one node may be slow , or outdated 
       
       we got stale data
    
    
    -> Higher latency , More network calls                   

"""