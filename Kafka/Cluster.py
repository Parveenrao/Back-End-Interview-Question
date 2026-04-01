"""  
=> Cluster === Group of multiple broker 


               Instead of one borker , you run mutiple broker 
               Broker 1
               Broker 2
               Broker 3 
               
         All together = Kafka CLuster 

-----------------------------------------------------------------------------------

=> Why multiple broker 
    
    -> If we use only one broker 
       
       1. No fault tolerance 
       2. Limited scalabilty 
       3. Risk of data loss
 
1. Scalability  ->  Handle millions of message by adding more brokers 
2. Fault tolerance -> If one broker dies, system still works
3. High Availability ->  Consumer and producer dont stop 


-------------------------------------------------------------------------------------------

=> Core Component of cluster 

   1. Broker 
      -> Actual servers
      -> Store partitions
   
   2. Topic 
      
      -> Logical  Grouping of data
   
   3. Partitions 
      
      -> Physical storage of units
   
   4. Leader 
      
      -> Handle read and write 
      
    5 . Followers 
    
        -> Replicate data 

---------------------------------------------------------------------------------------------

=> Controller 
  
  One broker become controller
   
   1. Leader election 
   2. Detect broker failure
   3. Mange cluster metadata                          
               
"""