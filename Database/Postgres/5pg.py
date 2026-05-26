""" 
=> View in Postgres 

   -> View is virutal table in postgres 
   -> store only query 
   -> does not store any data 
   
   
--------------------------------------------------------------------------------------------------

=> why view
    
    1. Reusability 
       
       creat view  user_view as
       select o.id, u.name ,o.amount 
       from order join users u on o.user_id = u.id
       
       select * from user_view
    
    2. Hide sensitive columns 


---------------------------------------------------------------------------------------------------

-> Types 
   
   1. Simple view  
      -> based on one table 
      -> some time updateable
   
   2. complext view 
      
      -> joins / aggregations

--------------------------------------------------------------------------------------------------

-> Materlized view
   
   1. Normal view 
       
       -> runs query every time  , slow for heavy queries 
   
   2. Materizlized query 
       
       stored result physically
       
       CREATE MATERIALIZED VIEW sales_summary AS
      SELECT user_id, SUM(amount) FROM orders GROUP BY user_id;     
      
      REFRESH MATERIALIZED VIEW sales_summary;
      
      data is not auto refersh                   


"""