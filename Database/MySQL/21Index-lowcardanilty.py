""" 

=> Why Index On Low Cardanlity Not Usefull 

    1. what is cardanlity 

       -> Means approximately how many distinct values a column has 

       -> Imagine a user table with 10 million rows

            Gender columns has 2 unique values 

            Cardanlity = 2


        -> Gender is low-cardanlity column

    2. Why does it matter for an index 


       -> Purpose of an index is to help Mysql quickly reduce the number of rows it need 
          to examine

          10, 000 ,000

          Male   -> 5, 000, 000
          Female -> 5, 000, 000

          Create index idx_gender
          on employees(gender) 


       -> select * from users where
          gender = "Male"

          Index can quickly find  where 'Male' start 

          but thats not the real problem

          It find 5 million matching index entries

    3. WHy full table scan is better here

       -> Optimizer choose two plan 

       1. Plan A -> use idx_gender 

            Find Male in B+ Tree

            Read  5 million index entries 

            Reterieve 5 millions full rows

       2. Plan B full table scan

           Read table

           row 1 -> Male , yes

           row 2 -> male , no 

           row 3 -> male , yes

    6. Low cardanlity does not automatically mean , bad index 

        -> suppose we have

           status 

           Active           -> 9,990,000
           Suspended        -> 9000
           Delete           -> 1000

           status has only 3 distinct values

           so it has low cardanlity

           select * from users
           where status = "DELETED"


           only 1000 rows out of 1000000 match

           An index on status could be useful for this query because 'DELETED' 
           is highly selective, even though the column overall has low cardinality.

           The optimizer cares about cost and selectivity—how many rows the particular 
           predicate is expected to match.

    7. Composite indexes change the situation

        CREATE INDEX idx_city_gender
        ON users(city_id, gender);       




"""