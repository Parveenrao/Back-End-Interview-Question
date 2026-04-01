""" 

=> Rebalancing 
    
    -> Redistributing partitions among consumer in a group 
    
        Whenever system change , kafka says 
         
        Stop everything -> Reassign partitions -> resume 
        
---------------------------------------------------------------------------------------------------------

-> When Rebalancing happens 
    
    1. New consumer joins group 
      
      C1 -> C! , C2 
    
    2. Consumer Crash / leaves 
    
      C1 , C2 -> only C1
    
    3. Partition Change (topic scaled)
       
       3 Partition --> 5 Partition
    
    4. Consumer starts polling (TimeOut)
       
       max.poll.interval.ms exceeded     ---> kafka assume consumer is dead 


---------------------------------------------------------------------------------------------------------

=> Working  
  
 
  Topic -> 4 Partitions 
  Consumer -> C1 , C2 
  
  
  Before 
  
  C1  -> P0 , P1 
  C2 ->  P2 , P3 
         
            
-------------------------------------------------------------------------------------------------------------


-> Rebalance happens 

  1. Stop consumptions 
   
    All consumer pause
    
      -> No message processed ( thats why it is costly) 
      
  
  2. Group  Cordinator take control 
  
      kafka has a special broker   -> Group Cordinator
      
      IT  -> Track cosumers , Assign partitons 
  
  3. Rejoin Group 
     
     -> All consumer send , Hey , I , am alive 
  
  4. Leader Election 
  
     One consumer  become Group leader 
     
     -> It decide partitions assignment
  
  5. Partitions assignment 
     
     Example , new consumer join (C3)
     
     C1  -> P0
     C2 -> P1
     C3 -> P2, P3 
   
  6. Resume Consumptions 
     
     -> Consumers start reading again 


----------------------------------------------------------------------------------------------------------------------

=> Why Rebalances is problemmatic  

  1. Processing Stops 
     
     -> System is paused
  
  2. Duplicate Processing 
     
     -> If offset is not committed properly 
        
        message can be reprocessed                    
  
  3. Increase latency 
     
     -> Frequent rebalance --> slow system 
     
--------------------------------------------------------------------------------------------------------------------------

=> Types of Rebalancing 
   
   1. Eager Rebalancing (old way)
   
       -> All consumers stop 
       -> Revoke partitions 
       -> reassign from scratch 
     
     Heavy , Full pause 
   
   
   2. Cooperative Rebalancing (Modern Way)
   
      -> Only required Partitions movement 
          
          C0 -> P0
          C1 -> P1 
          
          only P2  moves to C3 
          
        Less disruption , Faster recovery 
--------------------------------------------------------------------------------------------------------------

=> Partitions Assignment Strategy 
   
   1. Range 
       
       Partitions: P0 P1 P2 P3
       Consumers: C1 C2

           C1 → P0 P1
           C2 → P2 P3            
   
   2. Round RObin 
   
        C1 → P0 P2
        C2 → P1 P3                         -> Better balance
   
    
    3. Sticky (Best)
    
       -> Keep previous assigment as much as possible      
                     
      
              
"""