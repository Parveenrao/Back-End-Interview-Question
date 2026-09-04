""" 

=> Why does DynamoDB split Partition

   -> A physical Partition has limit

   -> Each physical partition has approximately 

       1. Storage : upto 10GB 
       2. Read throughput upto 3,000 RCUs

       3. Write throughput upto 1,000 WCUs

     if any of these limits are approached , DynamoDB may split data across additional partitions 
     to maintain performance and capacity  


"""