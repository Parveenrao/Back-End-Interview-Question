"""

=> Common Non-Functional Requirements 
 
    1. Scalability 

        -> Scalability is the ability of system to handle increasing workload  without 

          significant degradation in performance

        -> As the number of user , request , data grows , system shoudl continue functionality
           efficiently 


        -> Example

            1. Suppose a website has 

                 Today = 1000 users 

                 Next Year = 10 million users


        -> Vertical scaling or Horizontal scaling 


    2. Availability 

       -> Availability is the percentage of time the system is operational and accessible to users

       -> Common Levels
            Availability	Downtime per Year
                99%	          ~3.65 days
                99.9%	      ~8.8 hours
                99.99%	      ~52 minutes
                99.999%	      ~5 minutes      

       -> Improve Availability


            1. Multipler servers 
            2. Load balancers 
            3. Health checks 
            4. Db Replication 
            5. Multi-region deployment 


   3. Relability 

       -> System should continuously perform the correct operation without failure or incorrect result 

       -> A reliable banking system always produce correct result  


       -> Relability Vs. Availability 

           A website can be availabe , but cannot be reliable 

           Amazon open successfully , but payment failed every time 

       -> Improving Relability 

           1. Retry mechanism 

           2.  Transaction 
           3.  Data validation 
           4.  Monitoring 
           5.  Idempotent APIs 


    4. Performance

         -> Peformance measure how quickly and efficiently the system process request 

         -> Performance include 

             1. Response time 
             2. Latency 
             3. Througput


        -> Improving performance 

            1. caching 
            2. CDN
            3. Async processing

    5. Fault Tolerance 

       -> Fault tolerance is the ability of the system to continue working when component fails 

       -> Server crash , 

          Another server process request

   8. Durability 

      -> Durability ensure that once data is successfully written , it is not lost - even server crash or power is

      -> Achieved using 

          1. Disk storage 
          2. Replication 
          3. WAL
          4. Backups

    9. Security 

       -> Security protect the sytstem from unauthorized access and attack

       -> include 

          1. authenication 
          2. Authorization 
          3. What are you allowed to do

   10. Consistency 

      -> Consistency ensure use see valid and expected data according to the system
         consistency model

   11. Maintainability

      -> Maitainablility is how easy it is to understand the fix  and improve the system over time 

   12. Extensible

      -> Extensiability is the ease with which new feature can be addded without major 
         change to existing code 

   13. Observability

       -> Ability to understand what is happening inside a system by collecting and 
          analyzig telemetry                                                                                                    



















"""