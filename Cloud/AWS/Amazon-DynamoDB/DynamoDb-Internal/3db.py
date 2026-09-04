""" 
=> DynamoDB Primary Keys

   1. Primay key

       -> A primary key is a field (combination of field) that uniquely identifies an item
          in a DynamoDB table 

        -> Like UserId , is a primary key , uniquely identify the item

    2. Types of primary keys 

         -> DynanoDB support two types of primary keys 

             1. Simple Primary key 
             2. Composite Primary key 


        1. Simple Primary key 

           -> A simple primary key consist of only one attribute , the partition key

              userid -> hash -> partition -> Find item


           -> When shoud we use simple primary key 

               when each item naturally has a unique identifier 

               userid , productid , employees , Books , orders


        2. Composite Primary key 

           -> Consist of 

              1. Primary key 
              2. Sort key 

           -> example 

               Primary key -> userid 

               Sort key -> orderid

               But in orders table , userid table repeats

               but the combination (userid , orderid) must be unique


            -> Internal storage 

               Partition key = userid 

               Sort key   = Orderid

               Dynamodb hash only partition key 


               Inside partition , items are stored in sorted order 


            -> Parition key decide , where data is stored 

            -> Sort key decide , how data is organized within that partition

        => Important Rule 

           -> Only primary key is hashed 

           -> sort key is not hashed

=> Why do we use a sort key?

     To store multiple related items under the same partition key and enable 
     efficient sorting and range queries within that partition.                                                       

     

=>  Can two items have the same partition key?
       Yes, if the table has a sort key and the sort key values are different.
       No, if the table uses only a simple primary key.     


"""