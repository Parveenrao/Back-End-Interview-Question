""" 
=> Long Polling Internals

    -> Problem Before Long Polling

        Imagine a queue with no message


           Queue
        ---------------------

           #no message
        ---------------------

        Consumer continuously ask SQS: ReceiveMessage

        SQS replies -> No message

        One second later SQS: RecieveMessage

        again -> No message

        This conitnue thousand of times

        Consumer -> Receive -> No -> Receieve -> Agina this many times

        This is called short polling

    -> Why this is bad

        Suppose 10,000 consumers
        each poll every second
        queue is empty

        That result in

            10000 request/sec

        Most request return

             No message

        Problems 

           1. Wasted CPU
           2. Wasted network bandwidth
           3. Higher aws request cost 
           4. Increase API load


=> AWS Long Polling

    -> Instead of immediately returning : No message

       SQS waits


          RecieveMessage(
          WaitTimeSecond = 20)

      Now the request stays open for upto 20 seconds


=> Internal Flow

    Consumer -> RecieveMessage() -> SQSfrontend -> Checkqueue -> Message?

    if message exist -> yes, Return immediately 

    if not No -> keep connection open


=> Internal Waiting mechanism

    1. Suppose queue is empty

       Queue(empty)

    2. Consumer calls

        RecieveMessage(20)

    3. Internally 


        Storage Node -> No visible message -> Register waiting consumer -> Sleep until

                                                                             1. New message arrives 
                                                                             2. Timeout expires

        Consumer is waiting , not repeatedly asking

    4. When a message arive

         Storage Node -> find waiting consumer -> Deliver message -> Close request 


    5. If no message arrives

       -> Suppose 20 seconds pass


       Consumer -> wait-> 20 seconds -> No message -> empty response

       only one request was made 

       without long polling  , 20 separate requests


=> Multiple Waiting consumer

    1. Suppose 

        Consumer A 

        Consumer B

        Consumer C

        ALl are waiting

        Queue(waiting)


        Producer send -> message 1

    2. Internally 


        Storage node -> assign message -> wake consumer B

        Consumer B receive the message

        A and C are waiting


=> What if multiple message arrive

    Producer -> 100 message

    Storage Node 

       Message 1 -> Consumer 1 
       Message 2 -> Consumer 2 
       Message 3 -> Consumer 3

    Consumer wake immediately 


=> Best Practice 

    -> Enable long polling whenever possible


            ReceiveMessage(
                 WaitTimeSeconds=20,
                 MaxNumberOfMessages=10
                )



"""