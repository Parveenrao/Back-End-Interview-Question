""" 

=> What is Topic

   -> A topic is a logical communication channel is SNS where publisher send message and 
      subscriber receive them

    -> think of broadcast channel , not queue

                     Publisher
                         |
                         |
                         V
               +----------------------+
               |   Order Topic        |
               +----------------------+
                   |     |      |
                   |     |      |
                 Email  SQS   Lambda  

    -> publisher never send message directly to lambda , SQS , or email . It send them to the 
       topic and SNS distribute them




=> WHy does SNS need topic

   -> Imagine an e-commerce application

      order service 
         |-> email service 
         |-> inventory service 
         |-> billing service 
         |-> analytics service
         
    order service must know

       1. where email lives
       2. where inventory lives 
       3. where billing lives 
       4. where analytics lives

     this create tight coupling

     if new service is added (fraud detection ) , the order service must be modified



     -> with sns

        order service only knows one thing

           publish to the order topic

        sns handle the rest


        create loose coupling , making system easier to extend and maintain


=> What inside a topic

    1. Topic ARN
    2. subscriber 
    3. access policy
    4. encryption setting 
    5. deliver policies
    6. tags 
    7. metadata


  what is not there 

     1. no permanent message storage (sns is not queue)

     2. no long - term db of msg 

     3. no consumer offsets



=> 1 Topic ARN 

   -> Every topic has an unique identifier called an Amazon Resource Name (ARN)  

              arn:aws:sns:us-east-1:123456789012:OrderTopic

              arn 
               |-> aws
               |-> sns
               |-> us-east-1
               |-> account ID
               |-> topic name

         when publishing , we use topic ARN

         sns.publish(
         
            TopicArn , 
            message)

    -> does topic store messsage

        no , a topic receives a message and immediately attempts to deliver it to all subscriber

        sns is optimized for routing , not storage

    -> can a topic has multiple publisher

       payment service 

       inventory service 

       mobile app 

         |

      order topic

     many publisher can send message to the same topic , provided IAM and topic 
     policies allow it 

    -> can a topic have multiple subscriber

         SNS -> Email / sqs/lambda

         each subscriber receives its own copy of the message


    -> topic types 

       sns provide two types of topic 

       1. standard topic

          -> very high throughtput

          -> best - offer ordering 

          -> at-least-once delivery

          -> possible duplicate deliveries

         suitable for 

           1. Notification 
           2. monitoring 
           3. analytics 
           4. event broadcasting

       2. FIFO topic

          -> Preserve message order

          -> support dedup

          -> work with fifo sqs queues

          -> lower throughput than standard topics                              



"""