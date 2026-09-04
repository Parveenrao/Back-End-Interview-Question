""" 

=> DAX Internal Architecture
             

              Application
                   │
          DAX Client SDK
                   │
                   ▼
        Request Router
                   │
         Hash Cache Key
                   │
                   ▼
          Cache Manager
          /          \
 Cache Hit        Cache Miss
     │                │
     ▼                ▼
 Return         DynamoDB
                     │
                     ▼
            Cache Population
                     │
                     ▼
                Return Result


=> Step 1 Application send request

         table.get_item(
            Key={
             "UserId": "USER#100"
          }
        )

    -> Normally this would go directly to dynamo db

    -> With DAX

        application -> DAX client SDK

=> Step 2 DAX client SDK

    -> The DAX SDK replace the normal DynamoDB client

       application -> DynamoDB

       instead , it become 

         Application ---> DAX cluster 

    -> SDK knows

       1. DAX endpoint 

       2. Cluster nodes 

       3. Authentication 

       4. Which node to contact

    It serializes the request and sends it over the network 


=> Step 3 Request Router

    -> Request reach a DAX node 

    -> Router decide 

        1. Which cache node owns this key 

        2. Whether to process locally 

        3. Whether to forward to another node 

     The router itself  doesn't know whether the item is cached -- it first determines where the lookup

     should happen

=> Step 4 Hash Cache Key 

   -> Now DAX converts key into hash

       hash(User#100) -> 9748943

       The hash is not the partition key from DyanmoDB. It is an internal value used by DAX to 

       locate cached entries efficiently 

    -> Why hash

       1. Imagine 100 million cache items

          without hashing 

           User#1
           User#2
           User#3


           User#10000000000000

           finding one item by scanning would be very slow

         with hashing 

            Hash(User#123)  -> bucket 25

            cache can jump directly to bucket

         this is why DAX returns data in microsecond

=> Step 5 Cache Manager

    -> Cache manager owns the in-memory cache.

                      Memory

                      Bucket 1
                      Bucket 2
                      Bucket 3
                      Bucket 4
                      Bucket 5
                      ...
                     Bucket N

             each bucket contains cached items

       example 

                        Bucket 25

                           ↓

                         USER#100

                       {
                         Name : Parveen
                         Age : 23
                         City : Delhi
                        }    

           cache manager checks:

            Does USER#100 exist 

               yes / no

               now there are two possibilites

    -> cache Hit

        -> Suppose the item already exist 

        -> cache manager immediately returns it

           application -> DAX -> RAM -> Return item

          no request goes to dynanmodb

    -> cache miss

       -> suppose this is the first request

       -> not found 

       -> cache manager says:

          need to fetch from dynamoDB

=> Step 6 Cache population 

   -> Loading data into the cache after it is fetched from original database (dynamoDB)

      it happen on cache miss

   -> before sending data back to application , DAX store it in its memory

   -> stroing process is called cache population   



"""