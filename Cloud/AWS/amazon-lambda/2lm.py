""" 
=> ServerLess computing 

    -> Serverless computing is a cloud computing model where we write and deploye code 

       without managing servers.

    -> cloud providers automatically provisions , scales , patches and manages the 
       infrastructure for you.

    -> Despite the name "Serverless" , server still exist. The difference is that we don't
       have to manage them

    -> Common serverless service in AWS is AWS lambda

=> Traditional Server

   1. We create server 
   2. We install OS 
   3. We configure scaling 
   4. We pay even when idle 
   5. We patch server 

=> Serverless

    1. AWS creates servers automatically 
    2. AWS manages OS 
    3. AWS scale automatically 
    4. Pay only when code runs 
    5. AWS patch server 


=> How Serverless Work 

   User Reques ---> API Gateway --> AWS Lambda function ---> Business logic --> DyanmoDB --> Response


   1. User click Place Order 

   2. API Recieve request 

   3. Lambda starts automatically 

   4. Lambda writes order to the database 

   5. Response Returned 

   6. Lambda stop 

  No server stays running after the request finish


=> Characteristics Of Serverless

   1. No Server Management 

      -> We never install 

         1. Install linux 
         2. Configure Nginx
         3. Patch OS
         4. Upgrade hardware 
         5. Replaced failed servers

     AWS handle everything


   2. Automatic Scaling 

       1 User -> 1 function runs 

       100 User -> 100 function run 

       1 million user arrive -> AWS automatically scale


       No manual scaling is required

   3. Pay per use

       1. Traditional VM

           Server VM
           24 hours

           Cost = Pay 24 hours 

       2. Serverless

          Function Runs:

            200 ms

          cost = Pay for 200ms

    4. Event driven

       -> Serverless function run only when an event occur

       -> Event include 

          1. HTTP request 
          2. File upload 
          3. Database change 
          4. Queue message 
          5. Scheduled job 
          6. IoT event

=>             User
                │
                ▼
         API Gateway
                │
                ▼
        Lambda Function
          /     |      \
         /      |       \
        ▼       ▼        ▼
 DynamoDB     S3      SNS/SQS     


=> Example Workflow 


User uploads image
        │
        ▼
S3 Bucket
        │
(Image Uploaded Event)
        │
        ▼
Lambda Triggered
        │
Resize Image
        │
Store Thumbnail
        │
Update DynamoDB
        │
Send Notification


-> No server is running continuously. The function executes only when the image is uploaded


=> Advantage 

    1. No server management 
    2. Automatic scaling 
    3. High availability 
    4. Pay only for execution time 
    5. Faster development 
    6. Built-in-Fault tolerance 

    7. Easy integration with AWS services

=> Disadvantage 

   1. Cold starts (slightly delay if a function has not been used recently)
   2. Maximum execution time limit

   3. Less control over underlying infrastructure 

   4. Can become complex with many interconnected functions 

   5. Vendor lock-in if heavily tied to a specific cloud provider


=> Is serverless really serverless?
    -> No. Servers still exist, but they are fully managed by the cloud provider, 
       so developers do not need to provision or maintain them.   




"""