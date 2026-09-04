""" 

=> RDS Proxy 

   -> Amazon RDS Proxy is a fully managed database proxy that sits between your application 
      and your RDS database 

    -> Its main job is to manage database connection pooling efficiently by using connnection
       pooling

=> Why do we Need RDS Proxy 

    1. Imagine application directly connects to RDS

       User -> Application -> Amazon RDS

       Every user request may create a new database connection 


       User 1 -> New connection 

       User 2 -> New connection 

       User 3 -> New connection 

       User 10,000 -> 10,000 connections 

    But database have a limit on how many concurrent connection  they can handle 

    if the limit is exceed 

       New connection are rejected 

       User see error like Too many connections

       Database perform degrades

    -> Solution = RDS proxy


    -> Instead of handling directly to RDS , application connect to the proxy 

             User -> Application -> RDS proxy -> Amazon RDS

         proxy keep pool of resuable database connection 


=> Why it is important 

   -> Opening a database connection is expensive 

   -> Involve 

       1. Authentication 
       2. Network communication 
       3. memory allocation 
       4. Session setup

     if this happens for every request , application become slower

   -> With RDS proxy 

      1. Existing connection are reused 
      2. Response time  improve 
      3. database handle more load efficiently    


=> Example , Without RDS proxy 

     user login -> Backend -> create connection -> Run query -> Close connection 


     with RDS proxy 


     user login -> backend -> RDS proxy -> use existing connection -> Run query -> return to connection pool


=> High Availability 

   -> RDS proxy work with Multi A-Z deployments 

   -> if primary db fails , standby become primary 

   -> RDS proxy reconnects automatically 

=> Security 

  -> RDS proxy integrates with 

     1. IAM authentication 
     2. AWS Secret manager for securely storing database credentials 

     3. TLS encryption for secure communication 



"""