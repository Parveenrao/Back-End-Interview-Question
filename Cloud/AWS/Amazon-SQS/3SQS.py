""" 


=> SQS Message Lifecycle 

    -> What happen to a message from the moment it is sent until it is deleted"

=> Complete Message Lifecycle 

                                 Application
                                     │
                                     ▼
                                SendMessage()
                                     │
                                     ▼
                               Validate Request
                                     │
                                     ▼
                              Authenticate (IAM)
                                     │
                                     ▼
                             Queue Metadata Lookup
                                     │
                                     ▼
                            Choose Storage Partition
                                     │
                                     ▼
                             Replicate Across AZs
                                     │
                                     ▼
                                Message Stored
                                     │
                           ────────────────────────────
                                     │
                                ReceiveMessage()
                                     │
                                     ▼
                            Visibility Timeout Starts
                                     │
                                     ▼
                             Consumer Processing
                                     │
                                     ▼
                               DeleteMessage()
                                     │
                                     ▼
                              Delete Replicas
                                     │
                                     ▼
                               Lifecycle Complete


=> Phase 1 Producer Create A Message

      -> Suppose an order receive message

      -> AWS SDK convert it into an HTTPS request

      Producer -> AWS SDK -> HTTS Request

=> Phase 2  API Validation      


     -> SQS front-end recieve the request 

     -> Queue url is correct 

     -> Message size is withint limits 

     -> Required permissions exist 

     -> FIFO requirments

     Incoming -> Validation -> Accepted

     if validation fails -> 400 Bad Request , No message is stored

     
=> Phase 3 Authentication

    SQS check IAM

     Producer -> IAM Policy -> Allow ?

     if denied , 403 access denied

     nothing reaches storage

=> Phase 4 Metadata Lookup

    -> Internally SQS retrieves queue metadata

                Queue Name

                 Visibility Timeout = 30 sec

                 Retention = 4 Days

                 Encryption = Enabled

                 Queue Type = Standard

        configuration determines how the message will be handled


=> Phase 5 Partition Selection 

   -> A routing mechanism choose a partition

   -> Now only Partition 3 store message


=> Phase 6 Replication

   -> Suppose the choosen partition exist in three Availability zones

      AZ-1

      AZ-2

      AZ-3

      Write Message

      Replica A 

      Replica B

      Replica C

      Only after sufficient replicas ack the writes does SQS return the success

      Producer -> 200 Ok

      Now the producer knows message is durable

=> Phase 7 Waiting state 

   -> Message is now stored

   
           Queue 
           | -> Message A 
           |->  Message B
           |->  Message C

           its state is-> visible

        Any consumer can read it


 => Phase 8  Consumer Polls

    -> Consumer calls

        Recieve message()


        Consumer

           ↓

        SQS Front-End

           ↓

       Partition

          ↓

   Find Visible Message

          ↓

     Return Message          

     
     The message still exist 

     It is not removed


=> Phase 9 Visbility Timeout

    -> Immediateltly after delivery


        Visible -> Invisible

        Message is hidden

        Other consumer cannot recieve a during visibility timeout

=> Why Does not sqs Delete immediately

    consumer -> Recieve message -> Server crash


    if sqs had already deleted the message -> lost forever 


    Instead 

    Recieve -> Hide -> Wait -> Delete only after success


=> Phase 10  Consumer Processing

    -> Consumer perform works


    Recieve order -> charge -> update db -> Send email -> Generate invoice


=> Scenario 1 Success

   -> Everything works 

   -> Consumer sends , Delete Message()


   Delete Request -> Locate Replicas -> Delete Message -> Ack

   message lifecycle ends


=> Secenario 2 Consumer crash

    Recieve -> crash

    consumer never deletes

    visibility timeout expire

    Invisible -> Visible again


    now another worker can recieve it 

    this provide at-least-once delivery


=> Message Retention

   -> Suppose no consumer is running

   -> the messsge waits

     1 minute -> 10 minutes -> 2 hours -> 3 days 


     eventually , Retention expires

     SQS remove it automatically 

     Retention period is configurable( 1 minute up to 14 days)

=> Message Attribute


Message

├── Message ID

├── Body

├── Attributes

├── Timestamp

├── Receive Count

├── Visibility Timeout

├── Receipt Handle


-> Receipt handle 

   1. when the consumer recieve the message 

      Recieve Message()

      sqs return something like

      Reciept handle 

      AQEB&F9

      to delete the message , the consumer must send that receipt handle ,not just the message ID.


      this ensure , SQS deletes the exact message delivery instance

"""