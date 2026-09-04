""" 


=> AWS Service Integration

   -> Normally the flow is 

       Client -> API gateway -> Lambda -> AWS Service

       client -> API gateway -> lambda -> SQS


       the lambda simple receive the request and call SQS

       lambda does not contain any business logic - it only forward request

       AWS asked ,

          Why run a lambda just to call another AWS service

          So AWS introduced AWS service integration


    -> Architecture 

       Client -> API Gateway -> AWS service

    -> benefit 

        1. Lower latency 

        2. Lower cost 

        3. Fewer component

        4. no lambda cold start 

        5. simpler architecture


=> Request Lifecycle

    Client -> API gateway -> Authentication -> validation -> IAM authorization -> AWS service 

    -> response -> Client

    instead of invoking lambda


    api gateway directly calls the aws api

=> How does it work 

  API gateway -> Assume IAM role -> Calls aws service


=> SQS integration 

   client -> api gateway -> SQS

=> SNS integration 

   client -> APi gateway -> SNS topic -> Email / sqs / lambda / sqs


=> Advantage 

   1. lower cost

      -> No lambda execution change

   2. lower latency

   3. simpler architecture

   4. no cold start

=> AWS Service Integrations allow API Gateway to invoke supported AWS services 
   directly without using a Lambda function. API Gateway assumes an IAM role with 
   the required permissions and calls AWS APIs such as SendMessage for SQS, Publish for 
   SNS, StartExecution for Step Functions, PutEvents for EventBridge, or PutItem for 
   DynamoDB. This reduces latency, eliminates Lambda cold starts and execution costs,
   and simplifies the architecture. However, when custom business logic or multi-step 
   processing is required, a Lambda function is still the preferred integration choice.      


"""