"""  
=> Numeric data type
      
      -> They are used to store numbers , but not all no. are same
      
      1.Smallint 
          -> 2 bytes 
          -> 32k range 
          
      2. int 
         
         -> 4 bytes 
         -> 2 billion
      
      3. bigint 
          
          -> 8 bytes 
          -> very large
          
--------------------------------------------------------------------------------------------

=> Serial Autoincrement

    id Serial
    id bigserial       


=> Decimal 
   
   -> Exact precision
   -> Used for money 

=> Floating Point 
    
    -> Float 
    -> Real 
    -> Double Precision
    
   Fast but not exact 
   Used in 
   scientif calculations
 
--------------------------------------------------------------------------------------------------------

=> String Data types 
    
    1. TEXT 
       
       name TEXT;
       description TEXT;
      
      -> unlimited depth 
    
    2. VARCHAR 
      
      -> variable length  with limit
      -> Thorw error if exceed
    
    3. char 
      
      -> always store fixed length 
      -> pads with space
      
      
      CREATE TABLE users (
      id BIGSERIAL PRIMARY KEY,
      name TEXT,
      email VARCHAR(255),
      bio TEXT
    );


----------------------------------------------------------------------------------------

=> Date Type Data type 
  
  1. DATE 
     
     brith_date DATE;
  
  2. TIME 
  
     start_time  TIME;
  
  3. TIMESTAMP 
     
      created at timestamp ('2026-04-20 14:30:00')
  
  4. TIMESTAMPZ
      
      created_at TIMESTAMPZ ( '2026-04-20 14:30:00+05:30' )          
         
          
                     
       



"""