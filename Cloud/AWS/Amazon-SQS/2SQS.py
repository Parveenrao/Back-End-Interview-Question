""" 

=> SQS Internal Architecture  


                  Producer
                      │
             HTTPS (AWS SDK)
                      │
                      ▼
              SQS Front-End API
                      │
          Authentication (IAM)
                      │
          Rate Limiting / Validation
                      │
                      ▼
             Queue Metadata Service
                      │
          Find Queue Partition
                      │
                      ▼
          Distributed Storage Nodes
          ┌────────┬────────┬────────┐
          │Node A  │Node B  │Node C  │
          └────────┴────────┴────────┘
                      │
             Multi-AZ Replication
                      │
                      ▼
               Consumer Polling

               
    -> An SQS queue is not a single server. It is a distributed system spread across multiple machine 
       and Availability zones

=> Core Component

    1. Front-End API Layer

        -> Public Endpoint our application calls.

        -> example 

           sqs.send_message(...)


        -> internally 

             Producer -> HTTPS Request -> SQS API Gateway

        -> Responsibility 

            1. Authenticate using IAM 
            2. Validate request parameters

            3. check permissions 

            4. Apply request throttling 

            5. Route the request

    2. Queue Metadata Service 

        -> Every queue has a metadata such as.

           1. Queue name 
           2. Queue URL 
           3. Queue type (Standard/FIFO)
           4. Visibility timeout 
           5. Retention period 
           6. Delay configuration 
           7. Dead Letter Queue configuration

    3. Partition Manager 

        -> Large queues cannot live on one machine 

        -> Suppose 100 million message

             One server would become bottleneck

        -> SO 

                    Queue 
                      |-> Partition 1
                      |-> Partition 2
                      |-> Partition 3
                      |-> Partition 4
                      |-> Partition 5

        -> Benefit 

           1. Horizontal scaling 
           2. Higher thorughput 
           3. Parallel processing

    4. Distributed Storage Layer

        -> This is where messgage lives


                                    Queue

                                 Partition 1

                                  /   |   \

                                  AZ1 AZ2 AZ3       

            AWS replicate message across multiple Availability zones

            if one server dies.  -> Replica server

            if one AZ fails 
               -> Another AZ serves the message


=> Message Write Flow 

     -> Suppose the producer sends

        
         {
         
           "orderID":123
         
         }

    => Step 1 Producer sends HTTPS request 

        Producer -> SQS API

    => Step 2 Authentication

        IAM -> Allowed ?

    => Step 3 Find Queue

        -> Queue metadata

    => Step 4 Find partition

        orderid() -> hash() -> Partition 6

    => Step 5 Write message 

        Partition -> Replica A , Replica B , Replica C


     Only after the required replicas ack the write does SQS return success to the partition


=> Conusmer Read Flow

   Consumer -> SQS API -> Locate Queue -> Locate Partition -> Find Available Message -> Return message

   message is not deleted yet


=> Visibility Timeout

   -> suppose Message A

   -> Consumer receive it

   -> Internally


   Visible -> Invisible -> Processing -> delete

   Other consumer cannot see it during visibility timeout

   if processing fails 

   Timeout expire -> Visible again

   Another consumer can retry it 

=> Delete Flow

   -> After processing

   Consumer -> DeleteMessage -> Remove replicas -> ACk

   if the consumer forget to delete the message

    visibility timeout -> Visible again


   This is why Standard queues provide at least once delivery 

"""