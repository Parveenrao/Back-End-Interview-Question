""" 

=> DynamoDB Partitions 

                     Users Table
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Partition A   Partition B   Partition C
        │             │             │
     Server 1      Server 2      Server 3


     One table is distributed across many partitions



     -> Partition is a physical storage unit where DynamoDB stores data

     -> Think of a partition as a storage box 


     -> Dynamodb internally  store it like 

        Partition 1

          U100
          U103 

        Partition2
          U101

        Partition 3

          U102 

    We never control which partition store which item

=> Partition Capacity 

   1. Each partition has a limit to how much traffic it can handle

   2. Like , each partition as having maximum throughput 

       Partition 1

        Reads 
        writes 

        capacity

      If every request goes to the same partition , it become a hot partition.


=> Hot Partition Problem 

    1. Imagine a food delivery application 

       Partition key -> ResturantId

       Suppose one resturant become extremely popular 

       ResturantID = R101 , hash -> parition 2 

       Every order is written with the same parition key


       millions of order hitting partition 2

       other partition remain idle

       this imbalance called hot partition

       Result can be

         1. Higher latency 
         2. Throttling 
         3. Reduced throughput

=> Good Partition Key 

   -> A good partition key shoudl distribute data evenly 

   -> Each user has unique id (user_id)

   -> bad parition_key = "india" , if most user are from india, hot partition problem

   -> another bad partition key = status (Pending , completed , Failed)


=> High Cardinality 

    -> Many unique values

       UserId 

       OrderID 

       TransactionId 

=> Low Cardinality 

   -> Few unique value 

      1. Status 
      2. Country 
      3. Gender 

"""