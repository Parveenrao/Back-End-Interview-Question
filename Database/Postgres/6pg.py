""" 
=> Trigger 

    -> Trigger is a function that runs automatically when an event happen on table
    
     Events:
       
       INSERT 
       UPDATE
       DELETE
       
    -> when something happen in table , run this logic automatically
    

-------------------------------------------------------------------------------------------------------------

-> First write trigger function 

            CREATE OR REPLACE FUNCTION log_user_update()
            RETURNS TRIGGER AS $$
       BEGIN
        INSERT INTO user_logs(user_id, action)
        VALUES (NEW.id, 'UPDATED');
    
        RETURN NEW;
       END; 
    $$ LANGUAGE plpgsql;   
    
    
    CREATE TRIGGER user_update_trigger
    AFTER UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION log_user_update();


"""