""" 

=> How SQS Message Are Physically stored

  
     -> Flow 


                      Producer
                         │
                         ▼
                   Frontend API
                         │
                         ▼
                  Partition Manager
                         │
                         ▼
                   Storage Node
                         │
                     ┌───┼────┐
                     ▼   ▼    ▼
               Replica Replica Replica
                 AZ1    AZ2    AZ3

                 
=> Message arrvies

   -> Suppose application sends

     {
     
     "orderId" : 101,
     "user" :    "john"
     
     }

     
    -> SQS receives the HTTPs request 


    application -> aws sdk -> HTTPS -> SQS API


=> Create Internal Message Object 

    -> SQS convert your payload into an internal structure 


                     Message

              -------------------------

                   Message ID

                   Queue ID

                   Body

                   Timestamp

                   Visibility Timeout

                   Retention

                   Receive Count

                   Receipt Handle

                   Checksum

                   Metadata

=> Assign Message ID

    -> SQS generate something like this

    -> ID is globally unique

=> Find storage partition


     -> Suppose queue has 20 partition

     -> a routing function decide where the message belongs

=> Write to storage nodes

   ->  partition are managed by storage nodes


   -> storage nodes are not just RAM

   -> SDD = data files

=> Replication 


=> Acknowledgment 

   -> Once enough replication succeeds aws respond

   application now knows the message is safely stored


=> What is actually stored



--------------------------------------------------

Message ID

Queue ID

Partition

Body

Attributes

Visibility Timeout

Retention Deadline

Receive Count

Receipt Handle

Creation Timestamp

Checksum

Replication Metadata

--------------------------------------------------

"""