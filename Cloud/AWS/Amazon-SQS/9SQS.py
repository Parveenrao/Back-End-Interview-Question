""" 


=> Failure Handling Internals


    -> Imagine aws has a storage cluster like this

       
                             Queue Partition

                                    │
                     ┌──────────────┼──────────────┐
                     ▼              ▼              ▼
                  Storage A      Storage B      Storage C
                   AZ-1            AZ-2            AZ-3

        every message is replicated across multiple AZ


=> Failure Scenario 1 

    Storage Node crash

    -> Nothing will happen 

    -> Frontend simply routes reads to healthy replica


    -> application never knows Storage failed

=> Failure Scenario 2

    Entire Availability Zone fails


    -> Because replica exist in AZ-2 and AZ-3 

       Producer continue writing 

       Consumer continue reading 

       Messge remain available 



=> Failure Scenario 3 

      Consumer crash

      -> Message was hidden , not deleted

      -> after the visibility timeout expire , visible again 

      -> Another consumer receive it 

      -> this is how sqs prevent messge loss due to consumer failiures


=> Failure Secanario 4

    Producer does not recieve ack 

    -> it think

        maybe sqs never stored the message

        so it retries

     1. standard queue

        -> msg may exist twice 

        -> application should be idempotent

     2. FIFO queue

        -> If the retry use the same Deduplication ID with dedup windo, sqs suppresss the duplicate 

=> Failure Secanario 5   

      Delete Request Lost 

      ->  Consumer process successfully 

      -> but the networks fails , before the delete response reach the consumer

      -> now consumer , unsure if delete succeed

      -> sqs may deliver again , rather than risk losing it

      -> again durability is prioritzed over avodinig duplicates 

=> Failure Secanario 6

     Storage Node fails during writes

     Producer -> Storage A -> crash


     if storage A were the only copy , message lost 


    -> instead


    Producer -> replica A , replica B , replica C

    enough replicas knowledge -> ack returned


    Replication before ack greatly reduce risk of message loss 

=> Failure Scenario 7 — One Replica Falls Behind

   Imagine Replica A , Replica B , Replica C


   -> Replica C experience temporary issue

   -> Replica c = experience recent updates

   -> when it come back , it must catch up with the current state from healthy replica before serving

      request 


=> Failure Scenario 8 Queue Backlog

   -> Suppose producer send
    
      10,0000 msg/sec

    -> consumer process

       10000 msg/sec

    -> Sqs does not drop , message , because of the brust , it buffers them until consumer catch up
       or the retention period expire

=> Failure Scenario 9 — Poison Messages

   -> Suppose every time a consumer process a message


      Receive -> Exception -> Retry -> Exception -> Retry -> Exception

      the same msg could be retried forever 

   -> instead   


                   main queue -> receive count -> Maxreceivecount -> DLQ

         the failing message is isloated , allowing normal message to continue flowing             




=>     



"""