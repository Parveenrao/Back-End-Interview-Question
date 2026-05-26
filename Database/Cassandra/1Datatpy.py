""" 

=> String Data type 
    
    1. Text 
        
        -> Support all unicode (english , hindi , emoji ,everthing)
        -> No length limit
        
        name TEXT , bio TEXT , city TEXT
     
     
     2. VARCHAR = TEXT
        -> Same as TEXT
     
     3. ACII
        
        -> only basic english character
        -> No emoji , no hindi , no special symbol
     
     
     
        CREATE TABLE users (
        user_id UUID PRIMARY KEY,
        name TEXT,
        email TEXT,
        city TEXT
        );         
  
-------------------------------------------------------------------------------------------------------

   2. Integer Data type 
       
       1. INT 
          
          -> used for normal values
          -> age , count , small nubers
          
          Range = - 2 bn to +2 bn
      
       
      2. BIGINT 
          
          -> timestamp 
          -> counters 
          -> IDS
      
      3. SMALLINT / TINYINT
          
          TINYINT -> 128 to 127
          SMALLINT -> 32K
      
--------------------------------------------------------------------------------------
   
   3. Decimal / Floating Type
       
       1. Float
           
           -> Approximate values(less price)
       
       2. DOUBLE
          
          -> More precise than float 
       
       3. Decimal 
          
          -> Exact precision (no rounding issue)
          
          -> used for , price  , finnanical calculations
          
          price Decimal

----------------------------------------------------------------------------------------------------------
    
    4. Counter data type 
        
        -> Only for like , view , followers
        
        CREATE TABLE post_likes (
          post_id UUID PRIMARY KEY,
          likes COUNTER
         );
          
                 
                 
"""