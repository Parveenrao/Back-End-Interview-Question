""" 


=> One-Demand Mode 

   -> On Demand Node is a capacity mode where where AWS automatically scales the read and 

      write capacity based on your application's traffic.

   -> we do not need to estimate traffic or provision RCUs/WCUs\


   -> Instead of configuring capacity units, simply create the table in On-Demand mode.


                    Application
                        |
                        v
                 +--------------------+
                 | DynamoDB Table     |
                 | Capacity Mode      |
                 | On-Demand          |
                 +--------------------+
                          |
               AWS automatically allocates
                 read/write capacity   

        if traffic increase , DyanmoDB automatically scales up. If traffic decrease , it scales 

        down . You pay only for the request you actually made 

    -> Example 

       1. Suppose you have an e-commerce website 

          Normal days

          100 reads/sec 

          5 writes/sec


          during festival sale

          10,000 reads/sec

          5,000 writes/sec


          with on demand

          1. No manual scaling
          2. No capacity planning 
          3. No throttling due to under provisioning

          4. AWS handle the capcity change automatically


=> Billing 

   Charges for 

   1. Read request units consumed 
   2. Write request units consumed 
   3. Storage 
   4. Optional feature (backups , stream)
   
   we do not pay for  unused capacity

=> Can an On-Demand table still be throttled?

     -> Although On-Demand automatically scales, requests can still be throttled if:

     -> You exceed DynamoDB's service/account limits.
     -> A single partition becomes a hotspot due to poor partition key design.
     -> The workload exceeds what the table can immediately scale to.  

=> Can you switch between On-Demand and Provisioned?

    -> Yes. DynamoDB allows switching between the two capacity modes, 
       making it easy to optimize costs as your workload changes.      


=> Does On-Demand remove the need for a good partition key?

      -> No. A poor partition key can create a hot partition, 
         where one partition receives most of the traffic. 
         Even in On-Demand mode, uneven traffic distribution can lead 
         to throttling on that partition.  


=> Is On-Demand infinitely scalable?

     -> No. It scales automatically, but it is still subject to 
        partition-level limits and overall service quotas. Good data 
        modeling remains essential.              
"""