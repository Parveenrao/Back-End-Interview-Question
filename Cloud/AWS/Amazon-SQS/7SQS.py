""" 

=> Amazon SQS standard Queue Internals

   -> Why standard queue exist 

       Suppose amazon has 

         1. 50 million customer

         2. Millions of order every hour 

         3. Thousand of microservice 

      if every message had to maintain strict ordering , throughput would drop dramatically 

      instead , aws optimized standard queue for 

         1. Massive throughput 

         2. High availability 

         3. Low latency 

         4. Horizontal scaling


=> Internal Architecture 

                Producer
                    │
                    ▼
             SQS Frontend API
                    │
                    ▼
            Queue Metadata Service
                    │
                    ▼
             Partition Manager
                    │
          ┌─────────┼─────────┐
           ▼         ▼         ▼
       Partition1 Partition2 Partition3
           │         │         │
           ▼         ▼         ▼
       Storage A  Storage B  Storage C

    -> The queue is split into many partitions


=> Why Partition

    1. Imagine one queue storing

       100 billion message

       can one server handle this : No

    2. Problems

        1. Disk become full 

        2. CPU become overhead 

        3. Network saturates

      aws instead distributes data across many machines


=> How does aws choose partition

   -> internally a routing function determines where a message goes

   Message -> hash function -> Partition number

   producer does not need to know the partition , SQS handle it 


=> Replication 


   -> Each partition is replicated across multiple AZs

=> Standard queues only offer best-effor best effort ordering


=> Horizontal Scaling

     Traffic increasing from

     1000 msg/sec -> 1,00,000 message/sec

     aws does not upgrade one server 

     -> Instead 

       Partition 1

       Parition 2 

       Partition 3

       Partition 4 

       Partition 5


       more partition are added behind the seeen

       each partition contributes additional throughput





 -> Why does Standard Queue sometimes deliver duplicates?



Consumer

↓

Receive Message

↓

Process Successfully

↓

DeleteMessage()

Suppose the network fails after SQS receives the delete request but before the acknowledgment reaches the consumer.

The consumer doesn't know if the delete succeeded.

Or suppose the storage replicas briefly disagree about message state.

To avoid losing a message, SQS may make it visible again rather than risk dropping it.

The result:

Message delivered twice

This is intentional. SQS chooses durability over deduplication.        


=> Why "At-Least-Once" Delivery?

There are two possible strategies:

Strategy A

Never lose messages

↓

Occasional duplicates

Strategy B

Never send duplicates

↓

Risk losing messages

AWS chose Strategy A because duplicates can be handled by applications, while lost business events often cannot.



=> Storage Nodes 

    1. Each partition is backed by storage nodes

     
    
       Partition -> storage nodes


    2. Storage nodes is responsible for 


        1. Writing message 
        2. Reading message 

        3. Update visibility 

        4. Deleting message 

        5. Replicating data 

=> Front End layer 

                    Application

                        ↓

                     AWS SDK

                        ↓

                 SQS Frontend

                        ↓

                 Partition Manager

                        ↓

                  Storage Node


=> Queue Growth 

   -> Suppose consumer are slower than producer 

        incoming are more than consumers

      the queues grows

      SQS act as a buffer

      as you add more consumers

      pattern is called load leveling  



"""