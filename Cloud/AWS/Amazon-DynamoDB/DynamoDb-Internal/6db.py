""" 

=> Sort-Key Internals 

   -> A sort key is the second part of a composite parimary key

      Primary key = Partition key + Sort key 

      Partition key = UserId 

      Sort key = OrderId

      All orders of U101 stay together


=> Step 1 

   -> Partition key Decide Storage

      DynamoDB hashes the partition key

      hash(user)  -> Partition A

      all records of User1 go into the same physical partition

=> Step 2

   -> Inside the partition DynamoDB keeps items ordered by the Sort key 

      Partition A

       User 1 -> Order 1
                 Order 2
                 Order 3
                 Order 4
                 Order 5

            Not random , always sorted


=> Sort Key Data Types

   1. Sort key can be

       String 

       A101

       A002 

       A003

       Sorted lexicographically 

   2. Number 

      1
      2
      3
      4
      5

      Sorted Numerically 

   3. binary

      -> Sorted by binary value


=> why does DynamoDB have a Sort Key?

     -> The Partition Key determines which physical partition stores the item.
     -> The Sort Key determines the order of items within that partition.
     -> This enables efficient range queries (BETWEEN, <, >, begins_with) without scanning all items.
     -> It also supports modeling related data (orders, events, time-series, hierarchies) 
        under the same Partition Key.    


=> Range Queries 

    1. Give me all items whose Sort Key lie between a start value and an end value 

    2. What happen internally

        1. DynamoDb hash the partition key

        2. only one partition is searched

    3. Find the start

        -> Inside that partition

        -> Since data is sorted, DynamoDB quickly locates the first matching Sort key 

    4. Reads Sequentially

       -> It reads and stop immediately after it find end 

       -> this is why it is called range query


       -> DynamoDB jumps to the first matching key and reads until the end of the range.

          Time -> O(log n + K)

          log n -> find the first matching item 

          k -> Number of item actually returned        



"""