""" 

=> Capacity and Performance in DynamoDB

    1. Read Capacity 

        -> Every Read operation consume Read Capacity unit(RCU)

        -> RCU depends on

            1. Item size 
            2. Strong vs Eventual consistency read 

           
        -> Strong consistency Read

            Return the latest committed value

            user balance = 500

            update balance = 600

            Read immediately 

            Result = 600

            Consumes 

            1RCU = 1 strongly consistent read

            for an item upto 4Kb

        -> eventually consistent Read

            Data may be slightly late(usually millisecond)

            so eventually consistency reads are twice as efficient

        -> Transactional Read 

           Used in Transaction 

           Gurantees acid

           consumes 2 RCUs


   2. Write capacity 

       -> Writes consumes WCUs

       1WCUs = 1 write upto 1kb


       -> Txn writes -> consumes 2wcus


   3. Capacity modes


     1. Provisioned Capacity

        -> We specify

          Read capacity -> 1000 RCUs

          Write capacity -> 500 WCUs


          DynamoDB reserve these resources 

          Good when -> traffic predictable

     2. On-Demand Capacity

        -> No capacity planning 

        -> AWS automatically allocates capacity 

        -> Good for 

           Sudden traffic 

           Unknows traffic

           No throttling 

           Cost more if traffic is consistent high

   4. Internal Partition Capacity 

       -> Easy physical partition has limits

       -> approximate limits 

          Read = 3000 RCUs

          Write = 1000 WCUs                                       





"""