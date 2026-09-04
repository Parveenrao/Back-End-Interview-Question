""" 

=> What is GSI 

    -> A GSI is a secondary index that allows querying a DynanoDB table using 

       different parition key and optional sort key then the base table .

    -> It is stored separately from the base table and is updated 

       async , making it eventual consistency


=> Can a table have multiple GSI

   -> Yes , a table can have multiple GSI , each supporting a different access pattern


=> Does GSI share same partition with base table 

    -> No.

    -> Base

       hash(UserId) -> Partition 5 

    -> GSI 

      Hash(city)  -> Partition 18

      They are independent

=> Can GSI become Hotspot

    -> Yes 

      
      city = "Delhi"

      Millions of users

      every write hashes to the same partition key


=> What GSI store internally 

   -> A GSI does not always store the complete item from base table

   -> It stores 

       1. GSI partition key(required)

       2. GSI Sort key (if defined)

       3. Base Table primary key (so DynamoDB knows which base table item the index entry refers to)

       4. Project attributes (depending on the projection type)

    -> Create GSI 

           Partition Key = City
           Sort Key = Name
           Projection = INCLUDE (Age)   

    -> What stored in gsi 

               City      =   Delhi          ← GSI Partition Key
               Name      =   John           ← GSI Sort Key
               UserId    =   101            ← Base table primary key
               Age       =   25             ← Projected attribute      


         what if projection = all

         GSI stores

           City 
           Name 
           UserId
           Age 
           Salary

        Everything is copied into the index

        Projection = keys_only

        only keys are stored

           City      ← GSI PK
           Name      ← GSI SK
           UserId    ← Base Table PK      

        projection = include

            Projection = INCLUDE

             Name
             Age       

         GSI stores 

                City
                UserId
                Name
                Age    

"""