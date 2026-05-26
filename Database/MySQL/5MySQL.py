""" 
=> Constraint IN MYSQL  

    -> Constraints are the rules applied to the columns to ensure data accuracy and relabiity
   
   
   1. Primary Key 
      
      -> Uniquely identifu each row 
      -> cannot be null
      -> ONly one per table
       
       
       Creata table users(
           id int primary key,
           name varchar(100)
       )
       
       INNOdb , this is called clustered index 
       data is physically stored based on  this
   
   2. Foreign Key 
       
       -> Link two table 
       -> Enforce refertial integrity
       
       -> Foreign is a column that link one table to another
       
       Cascade
       
        1. ON DELETE CASCADE
         -> if user is deleted , all their order are deleted 
        
        2. ON DELETE SET NULL 
            -> is user deleted = user_id = NULL
        
        3. ON DELETE RESTRICT
            
            -> Cannot delete parent if child exist
       
        CREATE TABLE users (
            id INT PRIMARY KEY
              );

          CREATE TABLE orders (
          id INT PRIMARY KEY,
          user_id INT,
          FOREIGN KEY (user_id)
          REFERENCES users(id)
           ON DELETE RESTRICT
           ON DELETE CASCADE
           ON DELETE SET NULL
           
               );  
    
    
    3. Unique 
        
        -> Ensure all values are unique 
        -> Multiple allowed per table
    
    4. NOt null
    
    5. CHeck 
         
         -> Enforce condition
    
        -> age int check (age > =18)    
    
    5. Default 
       
       -> Set default if none provided
         
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP     


-----------------------------------------------------------------------------------------------------------

=> ALias
   
   -> Alias is a temporary nickname we give to the table or columns in a query to make it shorter or readable                              
"""