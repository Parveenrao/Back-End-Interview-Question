""" 
=> View
   
   -> View = saved sql query that behave like a table 
   
   -> View is a virutal table based on the result of  of SQL query ,where query is stored but the data is not stored 
   
   
   CREATE VIEW user_orders AS
   SELECT u.name, o.id
   FROM users u
   JOIN orders o ON u.id = o.user_id;
 
 
-----------------------------------------------------------------------------------------------------

-> Update View 
    
   1. A view can be updated  if it is
      
      1. Based on ONe table 
      2. No group by 
      3. NO distinct 
      4. NO aggregation function
      
      CREATE VIEW user_view AS
      SELECT id, name
      FROM users; 
      
      UPDATE user_view
      SET name = 'Parveen'
      WHERE id = 1; 
   
   2. View cannot be updated when 
       
       1. Joins
       2. aggregation
       3. complex joins
   

-> View does not have indexex 


------------------------------------------------------------------------------------------------------

-> Working 
  
  1 Case Merge (Fast way)
    
    -> select * from user_view where id = 1;
    -> mysql convert it internally , SELECT * FROM users WHERE id = 1;
    
  
  2. Case 2 TEMPTable 
     
     1. RUn underlying query 
     2. store data in temp table
     3. apply filter
     
     4. if view has join , aggregation , mysql use temptable            

"""