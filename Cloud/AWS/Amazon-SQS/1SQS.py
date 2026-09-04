""" 

=> Amazon SQS

   -> Amazon SQS is a fully managed message queue service that allows different applications or 
      services to communicate asynchronously.

   -> Instead of one service directly calling other , it send message to queue.

   -> Another service reads that message later 

                       Producer
                          |
                          | Send Message
                          ▼
                     +----------------+
                     |      SQS       |
                     |    Queue       |
                     +----------------+
                           |
                           | Receive Message
                           ▼
                        Consumer   

   -> Think of it like a post office 

       1. Someone drop letters
       2. letters wait safely 
       3. Receiver picks them whenever they're ready

=> Why do we need SQS

   1. Imagine a e-commerce website 

       user place order -> order service 

    Now after placing an order many things must happen

      Send email 

      update inventory 

      Generate invoice 

      Notify warehouse 

      Send sms

   2. Without SQS

      Order Service
         |-> Email service 
         |-> Inventory 
         |-> Invoice
         |-> Warehouse
         |-> SMS

       if Email service become slow 

       everything become slow

       the user wait

   3. With SQS

             +----------------+
             |  Order Service |
             +----------------+
                     |
          Put Messages in Queue
                     |
      --------------------------------
      |      |      |       |       |
      ▼      ▼      ▼       ▼       ▼
   Email   Invoice Inventory SMS Warehouse    

   Order service finished immediately 

   background service process work independently 

   This is called asynchronous communication

=> Main Components 

   1. Producer 

       -> The application sending message

          1. Website 
          2. backend APIs
          3. Lambda 
          4. EC2

   2. Queue

      -> Temporary storage for message

                 Queue

                 Message 1

                 Message 2

                 Message 3

                 Message 4    

        Message wait until processed

   3. Consumer Read message 



=> Message Lifecycle 

   Producer -> Send Message -> Stored in queue -> Consumer Reads -> Consumer Process -> Consumer Deletes 

   -> Finished


=> Benefit 


   1. Decoupling 

      
   2. Reliability 

      -> Message remain in queue until processed 

      -> no data loss

   3. Scalability 

       -> suppose today , 100 message/minute 

       -> tomorrow , 100000 message / minutes

       -> simply add more consumer 

            Queue -> worker 1 ,worker 2 ,worker 3 , worker 4 , worker 5

   4. fault tolerance 

       -> if consumer crashes

         queue -> consumer , crash

         message return to queue 

         another consumer processes it 


=> Types Of SQS Queues 

    1. Standard queues 

       -> Ordering is not guranteed 
       -> Duplicate can occur

    2. FIFO Queue

       -> First in First out

          order preserved

        -> useful when order is critical

=> Important Terms 

   1. Message

      -> A unit of data stored in the queue 

   2. Queu URl

      -> Each queue has a unique URl

      -> Application use this URL to send and receive messages

   3. MessageId

      -> Every message gets a unique identifier 


   4. Visibility Timeout

   5. Message Retention Period 

      -> how long SQS keep an unprocessed message

      -> default = 4 days 

      -> Configurable 

         1 minute / 14 days

   6. Delay queue

      -> delay delivery of new message 

      -> example , delay = 30 sec 

          message enter queue now 

          consumer sees it after 30 seconds

          usefull for retries or scheduled processing

   7. Long Polling

         -> without long polling   

         -> consumer repeatedly ask

            any message -> no

            any message -> no

            lots of unecessary request 


         -> with long polling

             consumer wait for a message 


   8. DLQ

      -> Suppose processing keep failing

      -> after the maximum receives 

      -> Move message to DLQ                                  

   


"""