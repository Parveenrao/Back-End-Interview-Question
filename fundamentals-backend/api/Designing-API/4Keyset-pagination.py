""" 

=> Keyset Pagination 

    -> Keyset is a pagination technique where , isntead of saying Skip first N rows ,
       give me rows after this specific record


    -> why do we need cursor pagination 


       select * from user 
       order by id 
       limit 10 offset 9999990;

       -> db has to

           1. Read almost 1000000 rows 
           2. throw them away 
           3. finally return only 10 row


=> Cursor pagination idea

  
     -> Instead of saying , skipping 999000 rows 

     -> give me record after id 9999999


        select * from users

        where id > 99990000
        order by id 
        limit 10

        now db jump directly to the correct place using index 

        no  scanning , no skipping , very fast 


=> Important Point 

   
    1. Cursor is not always ID

    2. It can be 

        -> created at ,
        -> updated at ,

        -> email , id 

        -> score , id



"""