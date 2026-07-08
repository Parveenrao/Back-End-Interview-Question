""" 

=> AWS Lambda Invocation

   -> An invocation is the process of executing a lambda function

   -> when an event or request reaches lambda , AWS starts  your function by calling the handler


       Invocation = One execution of lambda function


=> What can invoke a lambda function 

    -> Many aws service can trigger lambda

      
       s3 file upload 

       API Gateway request 

       SQS message 

       SNS notification

       eventbridge schedule

       cloudwatch alarm 

       dynamodb stream

       kinesis record 


=> Types of Lambda Invocation


    1. Synchronous Invocation

        The caller wait  until lambda finishes executing

        Client -> API gateway -> Lambda -> Execute -> Return Response -> Client Receive Response


        the client does not continue unitl lambda return a result or an error


        -> Characteristics

            1. Caller waits 
            2. Immediate response 
            3. Errors are returned to the caller 
            4. Suitable for APIs and user-facing applications

    2. Asynchronous Invocation

       -> Caller does not wait 

       -> lmabda accept the event , queues it internally and process it later 


       s3 upload -> lambda queue -> lambda execute later 

       -> The source service gets an acknowledgment that the event was accepted; 
          it does not wait for function completion.   


       -> characteristics 

          1. Caller does not wait 

          2. event is queued 

          3. lambda retries on many asyn failure 

          4. good for background processing


    3. Poll based Invocation (Event source mapping)

       -> Lmabda polls  another service for new records

       -> The source service does not push event directly 

       -> the source service does not push event directly 


    SQS queue -> Lambda poller -> Reads message -> Invoke  lmabda 



=> WHen to use each

    1. Synchronous 

        -> Use when caller needs an immediate answer

        -> example 

           Login 

           Payment 

           Search API 

           order creation

   2. Async

     -> use when the work can happen in background

     -> example 

        1. send email 
        2. generate reports 

        3. Resize images 

        4. Process upload files

    3. Poll based 

       -> use when consuming message or streams 

       1. sqs order processing 

       2. kinesis analytics 

       3. dynamodb streams



=> flow 

  Customer

      │
      ▼
API Gateway
      │
      ▼
Lambda (Sync)
Create Order
      │
      ▼
Save to DynamoDB
      │
      ▼
Publish to SNS
      │
      ▼
Lambda (Async)
Send Email

      │
      ▼
Push Order to SQS
      │
      ▼
Lambda Poller
      │
      ▼
Generate Invoice


"""