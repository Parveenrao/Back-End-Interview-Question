""" 

=> Visibility Timeout Internals

   
   -> Why do we need Visibility Timeout

           1. Imagine we have one message

              Queue

              -------------------

                 Order #101

              -------------------

           2. A consumer recieve it

           3. Now consumer start processing

              Consumer -> Process Payment -> Update inventory -> Send email

              suppose processing take 20 seconds

              Now another consumer polls the queue after 2 second

           4. without visibility timeout 


               consumer 1 -> Processing 


               consumer 2 -> Processing    

               Recieve same message

               Both consumer process same order

           5. Result 

              1. Pyament charge twice 

              2. Duplicate email 

              3. inventory update twice   

        -> This is what exactly visibility timeout prevents.

=> Message states

   ->  A message move between these states 


            Send
             │
             ▼
           Visible
             │
      ReceiveMessage()
             │
             ▼
           Invisible
            (Locked)
             │
      ┌──────┴─────────┐
      │                │
    DeleteMessage     Timeout
      │                │
      ▼                ▼
   Deleted         Visible Again

   Message is never removed when received

   It only become visible

   
=> Internal Architecture


    -> Suppose queue contains

         Queuee

       ------------------------------

         Message A 

         Message B 

         Message C

       --------------------------------

       Consumer Request -> RecieveMessage()

       Internally -> 


       Storage Node -> Locate visible message -> Mark invisible -> Set expiration time -> Return message

       -> Aws store metadata like 

          1. Message 
          2. ID 
          3. Visibility Expiration 
          4. Recieve count 
          5. Reciept handle


=> What happend during polling

   -> Suppose another worker ask for message , ReceiveMessage()

   -> Storage node check

       Message A -> visible -> No -> Skip

       Message b -> visible -> yes -> Return


       Invisble message are skipped

=> Consumer Successfully Reads

    Consumer sends -> DeleteMessage(reciept handle)


    -> Internally 

       1. Find replica 

       2. Delete message 

       3. Replicate Delete 

       4. Done

    -> Message disapper permanently


=>  Why doesn't SQS delete a message immediately after ReceiveMessage()?

    -> Because the consumer may fail during processing. SQS waits for an 
       explicit DeleteMessage() to ensure reliable delivery.       

=> What happens if the visibility timeout expires?

    -> The message becomes visible again and can be delivered to another consumer.

=> Why is idempotent processing important?

    Because Standard queues provide at-least-once delivery, 
    duplicate deliveries are possible. Idempotent consumers ensure 
    repeated processing doesn't cause incorrect results.           

"""