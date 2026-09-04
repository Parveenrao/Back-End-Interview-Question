""" 

=> API - Gateway Caching

    -> It reduce latency and decrease the number of request reaching backend by serving frequently
       requested response directly from API Gateway

    -> Normally , every request goes to the backend

       client -> API Gateway -> Lambda -> Db


       if 10,000 users request the same product detail , lambda execute 10,000 times

    -> with caching


        first request

        client -> API Gateway cache(miss) -> Lambda -> db -> store response in cache

        second request

        client -> API gateway cache (hit) -> Returned cache response

=> WHy do we need caching

   -> Suppose product catalog rarely change

      without cache

       1000 -> request -> 1000 lambda invocation -> 1000 db reads

    -> with cache

      1000 request -> 1 lambda invocation -> 999 cache hit


    -> lower latency , lower lambda cost , reduce db load , better scalibility

=> Cache TTL

   -> cache data expire after a configured TTL

     TTL = 300 second

     ttl control how long cached data remains valid

=> cache key

   -> API gateway needs a unique key to identify cached responses


   -> cache key can aslo include

      1. Path parameters 
      2. Query string parameters
      3. Headers


=> what can be cached.

   1. Product catalog
   2. user profile 
   3. country list 
   4. configuration 
   5. Read only data

=> What should not be cached 

    1. Login resposne 
    2. OTp generation 
    3. Payment request 
    4. order creation
    5. banking txn 

    6. Frequently changing data


=> cache invalidation

   -> some data changes before the ttl expires


      product price -> 100 

      updated = 120

      but cache still contains 100


=> cache capacity

   -> API gateway provision a dedicated cache cluster

   -> example , 0.5 Gb  1.6 gb 6.1 gb 13.5 gb


   large cache

     1. store cache 
     2. improve hit rates 
     3. cost more



"""