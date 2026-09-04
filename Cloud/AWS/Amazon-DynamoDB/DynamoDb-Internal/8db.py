""" 

=> What is Adaptive Capacity 

   -> Is a feature that allows DynamoDB to automatically give more throughput to busy 

      partition when possible


    -> One partition is busier than others . Instead of throttling immediately , DynamoDB

      borrows unused capacity from less busy partitions


    -> It improve performance without requiring you to provision more capacity manually 


=> Wihtout Adaptive Capacity 

       Table

+-------------+
| Partition A |
|  200 WCU    |
+-------------+

+-------------+
| Partition B |
|  200 WCU    |
+-------------+

+-------------+
| Partition C |
|  200 WCU    |
+-------------+

+-------------+
| Partition D |
|  200 WCU    |
+-------------+

-> Total = 800 WCU

-> Now traffic become

   Partition A -> 700 writes/sec

   Partition B -> 30 

   Partition C -> 40 

   Partition D -> 30


  Partition A needs 700 WCU , but has 200 WCU

  Result throttled


=>  With Adaptive Threshold

     -> DynamoDB notice

          Partition A -> Needs more throughput

          Partition B -> unused 

          Partition c -> unused 

          Partition d -> unused 

      -> It automatically  shifts unused thorughput

         total still is 800 WCU

         Nothing new was created 

         it was simply redistributed


=> Important 

   1. Adaptive capacity does not create more throughput 

   2. It reallocates unused throughput 

=>  If one partition becomes hot, will DynamoDB split it?

     -> First, DynamoDB uses Adaptive Capacity to allocate more throughput to the busy partition 
        if unused capacity is available elsewhere.

     -> If the workload is caused by many different partition keys, DynamoDB can scale the 
        table by adding more physical partitions over time.

     -> However, if one partition key (for example, User1) receives nearly all requests, 
        neither Adaptive Capacity nor adding partitions can fully solve the problem. 
        The correct solution is to redesign the data model, such as using write sharding or 
        selecting a better partition key.




"""