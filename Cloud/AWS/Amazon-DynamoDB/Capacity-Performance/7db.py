""" 

=> Why can a table with high total capacity still experience throttling?

   -> A DynamoDB table can still experience throttling because throughput limit 
      are enforced at the partition level not just at the table level.

    -> if one partition recieve too much traffic (hot partition), it 
       can be throttled even though the table has plenty of unused capacity overall


   -> Suppose table has

       Total provisioned capacity = 10,00 WCUs

       DynamoDB has split the table into 10 physical partitions


       Partition 1 -> 1,000 WCUs

       Partition 2 -> 1,000 WCUs

       Partition 3 -> 1,000 WCUs 

       Partition 10 -> 1,000 WCUs

    Although table total is 10,000 WCUs , each partition has its own throughput limit


=> Why does not DynamoDB use the unused capacity

   -> Because data is distributed by partitioned key

   -> A request for specific partition key must go to the partition that store that key.

      DynamoDB cannot simply redirect those request to another partition becuse data is not store 

      there 


=> A DynamoDB table can have plenty of total capacity and still 
   experience throttling because throughput is enforced at the physical  
   partition level. If many requests target the same partition key, they 
   all go to the same partition, creating a hot partition. That partition 
   can reach its throughput limit and throttle requests even while other 
   partitions have unused capacity. Good partition key design is essential 
   to avoid this.          

"""