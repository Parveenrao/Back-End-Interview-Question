""" 

=> DAX (DynamoDB Accelartor)

   -> DAX is a fully managed , in-memory cache for DynamoDB provided by aws.

   -> It is designed to reduce read latency from millisecond to microsecond without 

      requiring you to change application logic singnificantly

   -> without dax 

       application -> dynamodb(1-10ms)

   -> with dax 

      application -> dax(microsecond) -> cache miss -> dynamodb

=> Why DAX

    1. Imagine our application
    
       -> Instagram profile page 

       -> Amazon product page 

       -> Cricket score 

       -> Gaming leaderboard

     millions of user request same data repeatedly


   2. Without cache.

       -> 1 million request  => DynamoDb

          Read capacity increase 

          higher cost 

          Higher latency

   3. With DAX 

      1 Million request

         |

      DAX (server cache)
         |

         only few request

         go to dynamodb

=> What DAX store complete DyanmoDB items in RAM


=> DAX Cluster Architecture

                  Application
                      │
          DAX SDK (Client Library)
                      │
         --------------------------
         │                        │
         ▼                        ▼
     DAX Primary            DAX Replica
         │                        │
         ▼                        ▼
                 DynamoDB


      -> A DAX cluster continue

         1. One primary node 
         2. Multiple Replica node 

         Primary handles

            1. Writes 
            2. cache updates 

         Replicas handle 

           1. Reads 
           2. cache lookup


=> Read flow

   -> Suppose application ask  GETUSER(USER#500)

      Step 1 -> application send request

         application -> dax

      Step 2 DAX check cache

         cache -> USER#500 exist ?

      Step 3 Cache hit

         Ram -> User#500 found

         Return immediately 

          application

          latency

      Step 4 cache miss

       application -> DAX -> cache miss -> dynamodb -> return item -> store in cache -> return to client

       future request use cache

=> Write flow 

    -> DAX is write through 

    -> every write first reached dynamodb first 

    -> only aftere successfyll write , cache updated


    application -> DAX -> Dynamodb -> write successfull -> update cache -> Return success


=> Cache consistency 

   -> DAX maintain cache consistency for writes that go through DAX

   -> application writes through dax

      application -> dax -> dynamodb -> cache updated

=> What if someone writes directly to dynamodb

    -> Application A -> DAX -> dynamodb

    -> but another service 

       lambda -> dynamodb

     -> now dax cache , age = 25 

        dynamodb age = 26 

     -> cache become stale until 

        1. TTL expire 
        2. Item is evicted
        3. cache refereshed

=> TTL (Time to live)

   -> Every cacha item has expiration 

      TTL = 5 minutes


=> Query Caching 

    -> Dax also caches query result

       ex = PK User#100

       Result = 10 items

       Next same query = served from cache

=> Eventually consistent Reads

   -> Dax support eventual consistent reads


     User A updates item 

     Immediately 

     User B reads


     Depending on time

      1. DAX may return the latest value , if the write went through DAX

      2. stale if not go thorugh DAX

=> Transactions 

   -> DAX does not cache txn APIs


      TransactionWriteItems -> Bypass cache -> DynamoDb



"""