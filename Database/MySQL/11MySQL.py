"""" 
=> Trigger in Mysql
    
    -> Trigger is a piece of code that automatically runs when something happens on a table
       
       whemever x happens -> automatically do y
       
       example 
       
       insert happens -> log it
    
    
    -> Type of Trigger
        1. INSERT 
        2. UPDATE
        3. DELETE 
        
    -> Combined TYPES 
        
        1. BEFORE INSERT
        2. AFTER INSERT
        3. BEFORE UPDATE
        4. AFTER UPDATE
        5. BEFORE UPDATE
        6. AFTER DELETE 
   
   
-------------------------------------------------------------------------------------------------------

-> Creata trigger log_user_update
   AFTER  UPDATE ON USER
   FOR EACH ROW
   
   BEGIN
      INSERT INTO user_log(user_id, action)
      values(NEW.id , 'UPDATED');
   END


->   CREATE TRIGGER backup_before_delete
        BEFORE DELETE ON users
        FOR EACH ROW
    BEGIN
      INSERT INTO users_backup(id, name, email)
      VALUES (OLD.id, OLD.name, OLD.email);
    END;                
"""