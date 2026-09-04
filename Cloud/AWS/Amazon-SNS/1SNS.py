""" 

=> Amazon SNS

    -> Simple Notification Service

    -> Is a fully managed publish/subscribe (pub/sub) model / messaging service that enables 
       microservices and serverless component to communicate async


    -> Key concept 

       1. TOpic -> A communication channel where message are published
       2. Publisher -> the application or service that sends message to topic 
       3. Subscriber -> the endpoint that receives message from the topic


    -> Features

      1. pub/sub messaginig
      2. Fan-out -> (send one message to multiple subscriber)

      3. Message filtering -> deliver message only to interested subscriber

      4. High availability and scalability

      5. Serverless -> No infra management


    -> Supported subscriber

       1. amazon-sql 
       2. lambda 
       3. email 
       4. sms 
       5. http/https endpoints
       6. mobile push notification

     -> common use case 

        1. sending order confirmation emails / sms

        2. trigger multiple microservices  after an event 

        3. fan out architecture 

        4. alerting and monitoring 

        5. mobile push notifications

     -> example 

       Suppose an e-commerce application receives a new order

       1. order service publish a message to the order topic

       2.sns sends the same message to

           1. email service -> send confirmation email 

           2. inventory service (lambda) -> update stock

           3. billing service -> process payment 

           4. analytics service -> record order statistics


=> SNS vs SQS
                 SNS	                                      SQS
              Push-based	                              Pull-based
              One-to-many messaging	                     One-to-one messaging
              Publishes to multiple subscribers	         Messages consumed by one consumer
              No message storage (except retry window)	Stores messages until consumed
         Used for notifications and event broadcasting	Used for decoupling and buffering workloads




"""