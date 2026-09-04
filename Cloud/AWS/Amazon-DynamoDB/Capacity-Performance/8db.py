""" 

=> Throttling 

   -> DynamoDb temporarily reject or delays request because the requested read / write rate
      exceeds the capacity that DynamoDB can currently save 

    -> The request is not permanently failed. DynamoDB ask the client to retry later 

      usualy with exponential backoffs

    -> Example 

       Suppose table has 

      ->   Provisioned capacity = 100 WCU

      ->   Application send = 150 writes/sec

      ->   DynamoDB can process only 100 writes /sec

      -> The remaining 50 writes/sec are throttled


     ->          Application
                     |
              150 Write Requests
                     |
                     v
              +------------------+
              | DynamoDB         |
              | Capacity = 100   |
              +------------------+
                     |
                     +--> 100 Accepted 
                     |
                    
                     +--> 50 Throttled 


=> Why does throttling happen

  1. Exceeding Provisioned Capacity 

  2. Hot partition 
     
      1. Table total capacity = 10,000 WCUs

      2. Traffic 

          Partition 1 -> 7000 writes 

          Partition 2 -> 200

          Partition 3 -> 100


     3. Even though the table has enough total capacity 

         unused capacity = yes

        Partition 1 exceed its limit

        Result -> throttling 

     4. Sudden traffic spike

          1. Suppose traffic is 100 req/sec

          2. suddenly  500 req/sec

          3. In provision mode, auto scaling need some time to increase capacity

          4. During that time , some request throttled

     5. Exceeding On-Demand Scaling  Ability

         1. Many think on demand never throttles

         2. This is not true


         3. If the increase is too large or concentrated on one partition , DynamoDb can still
            throttle request

     6. Service quotas 

        -> Every AWS account has service limits

        -> Example , Maximum table throughput   Exceed

        -> Result throttling

=> What happen during throttling 

    -> application shoudl retry (Throttling Exception)




"""