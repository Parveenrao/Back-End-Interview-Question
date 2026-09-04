""" 

=> Write Sharding 

   -> Is a technique used to spread write across multiple partition keys so that no 
      single partition become overload


=> Why do we need write sharding   


        Suppose you have a DynamoDB table:

           Partition Key	Sort Key
            Post999	         User1
            Post999	         User2
            Post999	         User3

        -> Partition key is Post999

        -> Now imagine a celebirty post something  , in one minute  1,00,000 users post something


        -> Every write looks like (PK = Post999 , SK = "User12345")

            hash(Post999) -> Partition A 

            Every one of those 1,00,000 goes to Partition A

            Create hot partition and throttling and higher latency

=> Solution , Write Sharding

    1. Instead of using single partition key , Post999

    2. Create multiple partition keys

       Post999#0
       Post999#1
       Post999#2
       Post999#3

    3. Partition A      100,000 writes/sec

       Partition B      100,000 writes/sec

       Partition C      100,000 writes/sec

       Partition D      100,000 writes/sec

       Instead of one partition handling all writes, several partitions share the load.   


=> Reading become harder

   1. Without sharding

      query(Pk= Post999)

      one query return all likes 


   2. with sharding 

       Query("Post999#0")

       Query("Post999#1")

       Query("Post999#2")

       ...

       Query("Post999#9")   


    Application merge the result

=> What is Write Sharding?

     -> Write sharding is a data-modeling technique where a single logical partition key 
        is divided into multiple partition keys by adding a shard suffix (for example, Post999#0 to Post999#9). 
        This distributes write traffic across multiple physical partitions, preventing hot partitions 
        and improving write scalability. The trade-off is that reads become more complex because the 
        application must query multiple shards and combine the results.     



"""