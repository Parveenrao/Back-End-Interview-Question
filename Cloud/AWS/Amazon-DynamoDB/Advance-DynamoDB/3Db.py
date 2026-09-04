""" 

=> Optimistic Locking 

   -> Is a concurrency control technique that prevent lost update when multiple 
      client try to modify the same item at same time

   -> Prevent lost update problem 

   -> with optimistic locking

       Every item contains a version number

       when updating , client says -> update only if version is still 5

       this is done using conditional expression


=> Conditional Expression 

                       UpdateItem(
                           Key={"AccountId": "A1"},
                           UpdateExpression="SET Balance = :b, Version = :newVersion",
                           ConditionExpression="Version = :oldVersion",
                           ExpressionAttributeValues={
                               ":b":1200,
                               ":oldVersion":5,
                                ":newVersion":6
                            }
                         )


=> Advantages
    
      -> Prevents lost updates without locking.
      -> High concurrency because readers and writers are not blocked.
      -> Atomic version check and update.
      -> Scales well in distributed systems like DynamoDB.
      -> Works naturally with conditional writes.                         

=> Limitations
     -> Under heavy write contention, many updates may fail and require retries.
     -> Clients must handle ConditionalCheckFailedException.
     -> Requires maintaining a version attribute (or another value used for conditional checks).

=> 2. Is optimistic locking atomic?

       -> Yes. The condition check and the write are executed as a single atomic 
          operation on the leader replica.    


=> Why doesn't DynamoDB use pessimistic locking?

     -> Because distributed locks reduce scalability and increase latency. 
        Optimistic locking allows concurrent access and only rejects conflicting updates.                 

"""