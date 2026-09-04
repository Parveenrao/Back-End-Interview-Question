""" 

=> Single Table vs Multiple Table Design 

    -> Should i use single table or multi table

    -> It depends on access patterns

       1. DynamoDB encourages single-table design , but multi table design is still
          appropriate for some application


=> Single Table Design

   -> Means  storing multiple entity types in one DynamoDB table 


                          Application

                              │

                              ▼

                +------------------------------------+
                |          Ecommerce Table           |
                +------------------------------------+

                              PK              SK
                -----------------------------------------
                           USER#101        PROFILE
                           USER#101        ORDER#1001
                           USER#101        ORDER#1002

                           ORDER#1001      PAYMENT

                           PRODUCT#501     DETAILS

                           CATEGORY#Laptop PRODUCT#501

         -> Everything lives in one table

=> Advantage of single table design


    1. Fewer db calls

       -> Instead of 


          Users Table -> order table -> Payment table 

        -> we do 

          Query(User#101)

    2. Better performance 

       -> Related data is retrieved together , less latency 

    3. Lower cost 

       -> One query consumer fewer reads operation then several separate request            

  



"""