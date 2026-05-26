""" 
=> In 
   
   -> Is this value  present in a list or subquery
   
   
   -> user with orders 
      
      
      select * from users where id in (select user_id from orders)
      
      subquery run first 
      create a set / list 
      outere query check membership
      
      
   -> Problem with IN
       
       when subquery has null , then iin behave differently 
          
          SELECT * FROM users WHERE id NOT IN (1, 2, NULL);

----------------------------------------------------------------------------------------------------------------------

=> Exist 
   
   -> Exist check does at least one matching row exist 
   
         SELECT *FROM users u WHERE EXISTS (SELECT * FROM orders o WHERE o.user_id = u.id);     
         
         SELECT *FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);  
         
         
         used for large dataset , fast 
         
         
         work for null also
          
          exist does not care about , null ,it care about does row exist    

"""