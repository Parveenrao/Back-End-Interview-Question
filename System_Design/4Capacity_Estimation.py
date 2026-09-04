""" 

=> Capacity Estimation 

    1. Capacity estimation is the process of calculating the expected 

       -> Number of user 
       -> Request per second 
       -> Read and Write traffic 
       -> Storage requirement 
       -> Network bandwidth 
       -> Cach size 
       -> Memory 
       -> CPU needs


=> WHy Capacity Estimation is Needed 

     -> Suppose we are designing instagram 

     -> without capacity estimation , we do not know 

        1. Should one server be enough 
        2. Do you need Redis 
        3. Do you need kafka
        4. SHould be use kafka or cassandra 

        5. Do we need sharding


=> Process of capacity Estimation 

    
    1. Understand the requirements -> identify what the system does 

       -> what is the product 
       -> who are the user 
       -> what operation are supported 
       -> Which operation are reads 
       -> Which operation are writes 
       -> Is it real-time

       -> is it global or regional


    2. Estimate users

        -> Estimate how many people use the system

        -> imp metrics 

            1. Total Registered users
            2. Montly active users
            3. Daily active users
            4. Concurrent users

        -> Example 

            Registered users = 100 million

            Montly active users = 30 million 

            Daily active users = 10 million

            concurrent users = 500000

        -> why concurrent user imp 
 
              server handle user who are online at the same time 


   3. Estimate Request per second 


       Average RPS = Total Request per day / 86400 

       -> Example 

          10 million user 

          each user send = 20 request per day 

          total = 10 M * 20 => 200 Million/day


          Average RPS = 200 Million / 86400 => 2315 RPS

      -> Peak RPS

          Traffic is not constant

          Assume peak traffic is 5 X of Average traffic 

          2315 * 5 => 11575


   4. Estimate Read and Write Ration 

      -> Every system has different traffic patterns 

        1. Youtube   -> Read = 99% , Write = 1%

        2. Instagram -> Read = 90% , Write = 10%


        3. Twitter  -> Read = 95% , Write = 5%

        4. Whatsapp -> Read = 50% , Write = 50%

        5. Banking -> Read = 60 % , Write = 40%


     -> Peak RPS 

        10000 RPS 

        9000 Read per second 

        1000 write per second


   5. Estimate Storage 

       -> Estimate how much data is stored 

          Storage = Number of Records * Record size

       -> Example 

          100 million users 

          Each profile = 2kb

          storag = 100 m * 2kb => 200 Gb


       -> include growth

          suppose -> 1 million new user/month

          each profile = 2kb

          monthly increase = 2gb

          yearly 24GB


   6. Estimate Bandwidth

       bandwidth = RPS * Response size 

                   3000 RPS = 100kb 

                   bandwidth  = 300mb/sec

   7. Estimat cache and memory

      -> Not all data needs to stay in RAM

        DB = 5Tb

        only 20% is frequently accessed


        20% * 5 Tb => 1 TB

   8. Estimate Number of servers

      -> suppose one application server can handle

         100 RPS

        Peak traffic , 10,000 RPS


        Servers = 10,000/1000 => 10 servers


   9. Plan for future growth

      current = 10 million users

      exepected = 50 million user

      Design should allow 

        1. Horizontal scaling 
        2. Db sharding 
        3. Load balancing
        4. caching 
        5. Auto scaling                                                                                                         


"""