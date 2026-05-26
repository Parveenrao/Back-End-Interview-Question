""" 
=> Joins in Mysql
    
    -> A join is a clause used to combine row from two or more column from two or more tables

----------------------------------------------------------------------------------------------------

1. Inner Join
    
    -> Return only matching rows from both tables 
    
       select u.name , u.id from users u 
       from user u
       inner join orders o 
       on u.id = o.user_id

2. Left join 
    
    -> Return all rows from left table
    -> Matching from right 
    -> Non matching = NULL

3. Right join
    
    -> Opposite of left join

4. Full join 
    
    -> Not directly in Mysql 
     
     select  users u 
     left join orders o 
     on u.id = o.user_id   
     
     union
     
     select from user u 
     right join orders o 
     on u.id = o.user_id

5. Cross join 
   
   every row * every row
   

6. Self join 
    
    join a table with itself
    
    SELECT e.name, m.name AS manager
    FROM employees e
    JOIN employees m
    ON e.manager_id = m.id;   
                        


"""