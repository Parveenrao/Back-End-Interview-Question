"""   
=> Back-Pressure 
    
    -> System is recieving data faster than it can process 
        
        Producer speed > Consumer speed
        
        Consumer lag increases
        Memory/CPU overload
        System becomes unstable

-----------------------------------------------------------------------------

=> Where BackPressure happens  
    
    -> Back-Pressure hapoen at 
       
       1. Consumer side 
       2. Broker side 
       3. Downstream side 

-------------------------------------------------------------------------------

=> Real life example 
   
   Producer sends  10,000 msg/sec
   Consumer processes  2,000 msg/sec 
   
   Remaining 8,000 msg/sec  = backlog
 
 -> This consumer lag  building up
 
--------------------------------------------------------------------------------
 
 =>  Types of BackPressure 
 
1. Processing Bottleneck

    -> Slow Db calls 
    -> heavy computations
    -> External API delays 

2. Fetch Overload 
   
   -> Consumer fetching too much data 
   -> can not process fast enough

3. Resource Limit 
   
   -> CPU High
   -> Memory high
   -> Thread blocking

--------------------------------------------------------------------------------------------------

=> What Happens If You Ignore It
    Rebalancing increases
    Duplicate processing
    OutOfMemory errors
    System crash

This is why real systems fail          
 
 
-----------------------------------------------------------------------------------------------------

1. Handling Consumer Speed
   
   -> max.poll.recors = 100
      
      limits how many message you can process per poll

2. Pause And Resume 
   
3. Increase Consumer Scaling 
  
  -> Add more consumer in group
  -> Increse partitions

4. Batch Processing           
      








"""