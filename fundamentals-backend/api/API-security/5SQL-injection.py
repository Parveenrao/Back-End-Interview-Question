""" 

=> SQL Injection 

    -> SQL injection is a vulnerability where an attacker injects malicious SQL code 
       into a db query

     -> SQL Injection is an attack that manipulates SQL queries by injecting malicious input, 
        allowing unauthorized access to a database.  


=> WHy Does SQL Injection Happen 

   1. User Enter 

       Username : Parveen 
       Password : 12345

  2. Backend code 

      query = select * from users where username = {username}
                                  and   password = {password}


  3. Attackers enter 
               Username:
               ' OR '1'='1

              Password: anything 


   SQL becomes 
                       SELECT *
                        FROM users
                        WHERE username=''
                        OR '1'='1'                              '1'='1' = always true
                        AND password='anything'                                                    
  

=> Types Of SQL injection 

   1. Authentication Bypass

       -> Login without password 

           " OR "1" = 1


  2. Error based SQL injection 

     -> Attacker intentionally cause SQL errors to reveal

        1. Table name 
        2. Columns names 
        3. Database version 
        4. Query structure          

"""