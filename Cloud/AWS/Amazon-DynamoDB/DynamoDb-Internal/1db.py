""" 

=> DynamoDb Internal Architecture 

     -> Dynamo db is not one big database server 

     -> dynamodb is distributed. Data is automatically spread across many servers 


=> DynamoDB Architecture 

                Client
                   │
                   ▼
          DynamoDB Service
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
   Partition 1  Partition 2  Partition 3
        │          │          │
     Server A   Server B   Server C


  -> Instead of one server 

     1. Data is split into paritions

     2. Each partitions is stored on different AWS-managed servers 

     3. AWS automatically manages these servers -> we never see or manage them 


=> Partition

   -> A partition is a physical storage unit where Dynamodb stores part of yours table's data 

   -> imagine we have 10 million users 

   -> instead of storing them all on one machine , dynamo distribute them

       Paetition 1 -> user 1 , 5 ,20 ,.....
       Partition 2 -> user 2 , 7 ,10 .....

       each partition is stored on different AWS infrastructure 


   -> How does decide where data goes 

      1. This is where partition key become important 

      2. Is user_id is the partition key , DynamoDb 

         -> Take the partition key value 
         -> Applies a hash function 
         -> Use the hash to decide which partition store the item


         UserId -> hashfun -> hashvalue -> Partition 2     

         UserId -> hashfun -> hashvalue -> Partition 5

         we do not choose the partition -> DyanoDb does 


      3. If there is no hash

          -> every new user stored in one partition
          -> Partition become overload

          -> hashing spread data more evenly 

      4. This allows reads and writes to happen in parallel across multiple partitions

=> Automatic Scaling 

   -> Suppose my application grows

      Day 1 -> 100 users 

      Day 2 -> 1 million users 

      Day 3 -> 100 million users 


      as the amount of data and traffic increase , Dynanodb automatically creates additional partitions

      we do not need to manually add server or rebalance data 


=> Replication For High availability 

   -> Each partition is not stored on just one machine 

   -> AWS replicate it across multiple server in different AZs


                  Partition 1

                     Copy A
                       │
                ├──────────────┐
                ▼              ▼
          Availability      Availability
             Zone A            Zone B

       if one server or even an entire Availability zone fails , another replica can contiue
       serving request 

       This is the one reason Dyanmo DB provides high availability


=> Request FLow 

   1. When your application request an item


      Application -> DynamoDB API -> Hash '101' -> find partition -> Read item -> return result

      application never needs to know which partition holds the data 


   2. Why this Architecture is so fast 

       Partition 1 -> Read 

       Partition 2 -> Read 

       Partition 3 -> Read 

       Partition 4 -> Read 

       Partition 5 -> Read

    Many request can be processed at the same time , instead of all competing for one db server 

=> Key Takeways 


      DynamoDB is a distributed NoSQL database. 
      Data is divided into partitions.
      The partition key determines where data is stored using a hash function.
      AWS automatically manages partition creation and scaling.
      Each partition is replicated across multiple Availability Zones for durability and availability.
      Applications never interact with partitions directly—they only read and write using keys.


"""