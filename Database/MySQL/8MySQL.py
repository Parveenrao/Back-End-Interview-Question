"""
---------------------------------------------------------------------------------------------------------
  
1. Where Clause
   
   -> Applied before grouping
   -> filter row directly 
   -> cannot use , sum , count 

2. Having 
    
    -> used with group by clause
    -> WOrk with aggregation
       
--------------------------------------------------------------------------------------------------------

3. Union 
    
    -> Union combine both queries
    -> Remove duplicates from both queries
    
    -> Union is slow compared to union all 
    
    
    -> TO remove duplicate
        
        1. mysql store data in temporary structure
        2. Then either , sort + compare or using hashing , both are expensive operation
        3. need extra memory , uses cpu  for sorting, comparsion
        3. create temporary tables

4. Union all 
     
     -> Union all keep everything from both queries
     
     
     SELECT name FROM users
     UNION ALL
     SELECT name FROM customers;           

"""