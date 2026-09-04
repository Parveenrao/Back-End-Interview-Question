""" 

=> Why do we Need indexes 
 
     -> DynamoDB is designed to retrieve data using primary key 

     -> Primary key = UserId

     -> But what if you want 

         1. Find user by email 
         2. Find all user from india 
         3. Find user aged 24

     DynamoDB cannot efficiently query these attributes because they are not part of the 

     primary key 

     without an index , you would have to perform a Scan

=> What is Index 

    -> An index is another data structure that organize the same data using different keys

    -> DynamoDB has two indexes


       1. Local secondary index 
       2. Global Secondary index 


"""