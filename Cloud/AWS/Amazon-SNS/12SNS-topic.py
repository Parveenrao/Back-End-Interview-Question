""" 


=> SNS Topic Lifecycle 

    Create -> Configure -> Add subscribe -> Publish Message -> Deliver message -> Monitor 

    -> Update -> Delete


=> Phase 1 Topic Creation 

   -> Everything starts with topic creation

       developer -> createTopicAPI -> SNS


=> Phase 2 Configure Topic

   -> A new topic has default settings

   -> in production , we usually configure

      1. Access policy 
      2. encryption 
      3. delivery policy 
      4. FIFO setting
      5. Tags

=> Phase 3 Add Subscriber 

    SNS topic -> no subscriber

=> Phase 4 Subscription Confirmation

=> Phase 5 Publish message

=> Phase 6 Message Processing


=> Phase 7 Fan-out

=> Phase 8 Delivery 

=> Phase 9 Retry

=> Phase 10 Monitoring

   -> SNS publish metrics to amazon-cloudwatch


=> Phase 11 Update Topic


=> Phase 12 Delete Topic


"""