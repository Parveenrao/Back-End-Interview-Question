""" 

=> Control place Vs. Data plane

    1. Control Plane

       -> Responsible for configuration

           create topic 
           delete topic 
           subscribe endpoint 
           remove subscribe
           set policy
           configure encryption

    2. Data plance

       -> Responsible for actual message delivery

       -> when we call , publish()

           sns switch to data plane

       -> data plane


          publisher -> topic metadata lookup -> find subscriber -> deliver message

           control plane is not involved in routing each message



=> Topic Metadata

   -> A topic contains much more than just its name


      Topic = {
      
               "TopicId" : "...",
               "TopicName" : "order_topic",
                "TopicType" : "Standard",

                "Subscriber" : [
                
                
                                 lambda , 
                                 queue ,
                                 email],
                "encryption" : {
                
                
                                    "Enabled" : True ,
                                    "Keys" : KMS},
                "Delivery Policy" : {...},
                "Access Policy" : {....},
                "Tags" : {...}                                     
                    }

=> Subscriber list  

   
    Topic 
     |-> Billing queue 
     |-> Inventory queue 
     |-> analytics lambda
     |-> email service

     
   internally sns maintains references to these subscriber


   when  a message arrive , sns walks thorugh list  and dilver to each endpoint


=> What happen during publish

   publish -> orderTopic -> order#123 created

   internally

   step 1 , locate topic metadata

   step 2 , load subscriber list 

   step 3 , for each subscriber , create delivery task

   step 4 dispatch

   this is why sns can support millions of subscriber


=> WHy SNS store message 

   1. One topic has

       5000 subscribers , 10000 msg/sec

       if sns stored every message permanently , storage requirements would explode

       sns is optimized for routing


=> Can topic contain data

   -> No

   -> Suppose publish , order created

       topic does not append it to log

   -> instead 

       Receieve -> read subscriber list -> send copies -> forgot message

       the message exist only as long as sns need it for delivery and retries


=> Topic Namespace

   -> Topic exist within an AWS account and region

     account -> region -> sns -> topic
                                   |-> order topic
                                   |-> payment topic
                                   |-> user topic
                                   |-> audit topic

    no two topics in the same account and region can share the same name


=> Topic Lifecycle

    create topic -> generate arn -> store metadata -> init subscriber list (empty) -> ready

    when add subscriber 

    subscriber -> validate endpoint-> create subscription -> add to topic metadata

=> Why topic scale so well

   -> Imagine topic with 1 million subscriber

   -> aws does not send message  one by one in single thread


     publisher -> topic -> delivery engine -> worker pool -> thousand of parallel worker

     -> millions of deliveries




"""