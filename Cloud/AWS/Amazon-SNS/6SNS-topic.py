"""" 
=> Standard Topic

   -> Standard topic is a default sns topic type that provide

      1. very high throughput (designed to scale horizontal)

      2. At least once delivery 

      3. best effort ordering 

      4. low latency 

      5. fan out to millions of subscribers

    when we create an sns topic without specifying fifo , aws create a standard topic


=> Why does standard topic exist 

   1. Imagine amazon receives 1 million order per minute

      each order must notify

      -> billing 
      -> inventory
      -> shipping 
      -> fraud detection
      -> email 
      -> sms


      -> without sns

        order service -> billing service -> inventory service -> shipping service -> fraud detection

        -> email service -> sms service



        order service has to make many calls , increasing latency and coupling

      -> with sns

          1. Order service publish one message , sns handle fan out


=> Internal architecture 

 
     1. SNS frontend

         -> this is the api endpoint that receives publish request 

         sns.publish(topicarn , message = )

         frontent:

           -> authenticat the caller 
           -> validate the request 
           -> checks IAM and topic policies
           -> sends request to backend

    2. Routing layer

       -> locate the topic metadata

       -> tell sns 

          1. who should receive the message 
          2. which protocol to use 
          3. any filter policies
          4. delivery setting

    3. Delivery engine

       -> Suppose ther are 4 subscriber

          Topic -> billing queue / inventory queue / analytics queue / email / webhook

          delivery engine creates separate delivery task for each

          these task can execute in parallel

    4. worker pool

        -> sns does not use one thread per subscriber

        -> aws maintain a large distributed worker pool


        delivery queue -> worker 1 / worker 2 / worker 3/ worker 4 / worker N


        each worker deliver messsage independently

        if one endpoint is slow , others continue processing


=> why it is called Standard 

   1. Maximum scalability
   2. lowest latency 
   3. high availability

   it does not prioritize strict ordering or exact-once delivery

   Those guraantees require additional coordination , which would reduce throughput


=> Best effort ordering

    -> Consider two message

        Message A 
        Messge B

        we might exepect , every subscribr always receive
         
        A -> B

        with standard topic , that is not guraanteed


        a subscriber might recieve 

        B -> A

        this can happen because deliveries occur in parallel and network condition differ


        if strict ordering is business requirement , use an SNS FIFO topic with compatible
        subscriber

=> At least once delivery

   1. suppose sns send a message to an HTTP endpoint

       sns -> HTTP server 

       if the server timeout

       sns -> timeout


       sns cannot determine whether the server processed the request before the timeout

       to avoid losing the message  SNS retires

       possible outcome 

       the subscriber may recieve same message twice


       this is why standard topic can produce duplicate deliveries


=> WHy SNS does not gurantees exactly once

    1. sns optimized for 

       1. speed 
       2. availability
       3. massive scale

    instead for waiting for perfect confirmation fromm every subscriber , it retires when necessary

    this improves reliability but allows duplicate 

    consumer should therefor be idempotent

=> Throughput

   -> A standard topic is designed for extremely high throughput


      publisher a / b / c/ d -> sns standard topic -> millions of deliveries



=> Limitations 

    1. No strict ordering 
    2. possible duplicate deliveries
    3. not a persistent message store 
    4. require idempotent consumers




"""