"""  
=> Stored procedure 
     
     -> Stored procedure is a set of sql statement saved  in the database inside your database that you can call anytime
     
     -> Instead of writing same queries again and again , store them once and resue
     
     
     DELIMITER //

     CREATE PROCEDURE get_users()
    BEGIN
      SELECT * FROM users;
    END //

DELIMITER ;


call get_user()


-> with input

            DELIMITER //

CREATE PROCEDURE get_user_by_id(IN userId INT)
BEGIN
    SELECT * FROM users WHERE id = userId;
END //

DELIMITER ;

call get_user_by_id(1)


-----------------------------------------------------------------------------------------------------

=> Recursive Procedure Call 
     
     -> A recursive stored procedure call is a stored procedure that call itself uitla condition is met
     
     
     Base condition = when to stop
     Recursive call = calls itself
     
     
     DELIMETER //
     
     create PROCEDURE count countdown(n , int)
     BEGIN 
          
          # base condition
          if n <= 0 THEN 
              Select 'DONE'
              
          else:
              select n;
              
              call countdown(n-1);
           
           end if;
    
     END;
   
   DELIMETER //            
              
                  

"""