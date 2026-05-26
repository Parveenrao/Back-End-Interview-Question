""" 
=> Leader Election 
    
    -> In distributed system , many nodes are running at same time , If all of them try to 
       
       1. Write to database 
       2. coordinate task
       3. manage shared resources 
       
       things can coflict  , duplicate or break 
       
       -> So one node become the leader 
       
       -> other become follower

--------------------------------------------------------------------------------------------------

=> What does leader of 
    
    -> Leader is responsible for 
       
       1. handling write 
       2. Coordinating task 
       3. manitaing consistency
       4. making decision
    
    
    -> Followers listen to leaders 
    
    -> Execute task 
    
    -> Take over if leader fails

---------------------------------------------------------------------------------------------------

=> How Leader election works
   
   1. All node start equal 
   2. They communicate with each other 
   3. One node get selected based on some rule 
        
        1. Highest ID 
        2. Fastest response 
        3. Voting majority 
   
   4. Other accept it leader 


=========================================================================================================

1. Bully Algorithm 
    
    1. The node with highest ID become the leader 
    2. If a node detect the leader is down  - it start an election 
    3. Node with higher ID bully lower one and take over 
   
  => Assumptions 
      
      1. Each node have unique ID 
      2. Node know IDs of other nodes
      3. System is synchronous 
      4. Failure are detectable
    
    if assumptions fail break -> Bully fails(not used in modern system)


=> Working 

   -> Let say we have 5 nodes 
   
   IDs : 1, 2, 3 ,4 ,5 
   
   current leader = 5
   
   
   -> Case , leader (5) fails 
      
      Node 2 notice , leader is not responding 
   
   -> Election process
      
      Node 2 start election 
      
      send election message to higher ids
        3 ,4 ,5
   
   -> Response 
       
       node 3 -> i am alive 
       
       node 4 -> i am alive 
       
       node 5 -> no response(dead)
       
       node 2 back of , 
       higher node take over
                                             
    
    -> Node 4 start election 
       
       send election message 
       
       node 5 (no response)
          
          node 4 wins
    
    -> node 4 become leader 
         
         -> send co-ordinator message to all 
            
            i am the leader now


==========================================================================================================

=>  RAFT
     
     -> Raft is a consensus algorithm used in distributed system to make multiple machine agree on same data 
         
         even some fail
      
      -> we have 5 servers , Once must act as a leader  and other follow it
      
      -> Everyone must agree on the same sequence of operation(logs)
    
    
    -> Core Idea 
        
        Raft divide problem in three part
        
        1. Leader Election 
        
        2. Log Replication
        
        3. Safety consistency
   
   
   1. Leader Election
       
       -> Each node can be in three states 
          
          Leader ,Follower ,candidate
        
          1. Initially -> all are followers                         
          2. If no leader heartbeat - node become candidate 
          
          3. Candidate ask other -> vote for me 
          
          4. If majority votes -> become leader 
          
              Only one leader at a time
   
   
   2. Log Replication   
      
       -> Leader handle all  Client  request      
            
            CLient -> Leader -> follower
           
           1. Client send request to leader 
           
           2. Leader add it its log 
           
           3. leader send log to followers
           
           4. Once majority confirms  , if it is committed
           
           
           This ensure consistency across nodes
   
   3. Safety (Consistency Rules)
      
      Raft Gurantees 
      
      1. No conflicting logs
      
      2. Same order of operation
      
      3. Majority agreement before commit
   
   
   4. Heatbeat 
       
       -> Leader continuously send 
           
           "I am alive"
           
           If followers don’t receive heartbeat → start election.        

------------------------------------------------------------------------------------------------------------

=> Real Internal 
    
   1. Terms
         
         -> version of leader
         -> start from 0 = increase over time
         
         -> every election = new term
      
      
        if node sees higher term , step down 
      
        only one leader per term
      
        this prevent old leader messy up
   
   2. Leader Election 
        
        Step 1. Timeout (150-300ms)
            
            Each follower wait random time
            
            why random -> to avoid become node candidate at once
        
        Step 2. Become Candidate
             
             Increment Term 
             
             Vote for itself
             
             Send RequestVOte RPC
       
       
       Step 3. Voting Rules
            
            A node give vote if 
            
            Candidate term >= its term
            
            candidate logs is at least up-to-date
      
      Step 4 . Win Election
                   
                   
                   Must get majority vote
                   
                 5 nodes -> 3 vote
      
      Step 5. Heartbeat
          
          -> Leader send
             
             AppendEntries RPC (empty)
             
             This is heartbeat
   
   
   3.Log  Replication
       
       -> Structure of log
           
           Each entry (term , command)   
           
           
        -> Flow
           
           1. CLient -> Leader
           
           2. Leader append its log
           
           3. Send AppendEntries to its followers
           
           4. Follower check
                
                previous term 
                previou log term
            
            if match -> accept 
            
            if not -> reject 
   
   
   4. Log consistency 
         
         -> if two logs have same index + term  = everything before is identical
         
         coflict handling
         
         if follower has wrong log
         
           leader force overwrite
             
             Leader:   A B C D
             Follower: A B X Y

             → Follower becomes: A B C D         
                          
   5. Commit ANd APply
       
       Leader commit when , 
         
         entry is replicated to majority
         
         
         Once committed → applied to state machine
  
  
  => Failure scenario
    
    Case 1. Leader Crash
       
       -> Follower stop getting heatbeat
       
       -> Election start 
       
       -> New leader electied
       
       
       old uncommitted log may be lost
    
    
    Case 2. Split Vote
         
         4 node -> 2 vote A , 2 vote B 
            
            no majority , retry election with new term
    
    
    Case 3. Network Partition 
        
        Group 1(3 node) -> majority , continue 
        
        Group 2 (2 node)  -> cannot elect leadere
        
        Prevent split brain
    
    Case 4.  Old leader return 
       
       It sees higher term
       
       step down automatically                                                            
                                          
                    
                

""" 