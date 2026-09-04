""" 

=> SNS FIFO TOPIC

   -> FIFO topic is to provide ordered , deduplicated event distribution across
      subscribers that support FIFO semantics


=> what is FIFO Topic

    1. First in first out 

       -> Ordered message delivery (within in message group)

       -> dedup support 

       -> at-least-once delivery 

       -> fan-out-to-fifo


=> FIFO Topic Architecture

                                 Publisher
                                    │
                                    ▼
                            +-------------------+
                            | SNS FIFO Topic    |
                            +-------------------+
                                    │
                                    ▼
                              Ordering Engine
                                    │
                                    ▼
                           Deduplication Engine
                                    │
                                    ▼
                            Message Groups
                                    │
                                    ▼
                               Subscribers

    -> FIFO has two extra component 

        1. Ordering engine 
        2. Deduplication engine



=> Publisher send message 

    -> it must provide 
       
        1. Message body 
        2. Message groupID
        3. DeduplicationID

                    {
               "Message": "Order Created",

               "MessageGroupId": "Order-101",

               "MessageDeduplicationId": "abc123"
              }

              without messagegroupId

              sns reject request

=> What is message group

   -> think of message group as
     
        1. a separate ordered queue inside the topic

        2. example 

             orders 
               order101
               order102
               order103

               inside mixing all message

               sns creates independent streams

        3.  group a 
              -> message 1       
              -> message 2
              -> message 3

            group b

              -> message 1 
              -> message 2
              -> message 3





              SNS FIFO Topic

             +-------------+
             | Topic       |
             +-------------+

             /     |      \

     Group-A  Group-B  Group-C

     M1       M1       M1
     M2       M2
     M3       M3

     ordering exist 

     only inside 

     each group

=> Deduplication

     -> sns also prevent duplicates

     -> network timeout 

     -> publisher retries


     -> messagededuplicationID

         1. publisher send 12345

         2. sns store 12345 temporarily

         3. if another message arrive

            12345 sns ignore it 


=> Deduplication window

    -> sns window deduplication id for about 5 mintues

=> Ordering engine

   -> each message group has
      
        next expected message


        -> imagine 

           m1
           m2
           m3

           sns deliver

           m1 -> wait -> m2 -> wait -> m3

           even if m3 arrive first due to retry

           delivery wait until the correct sequence is maintained
"""