"""" 
=> HEAP (MEMORY) TABLE 
    
    -> A table stored enitrely in RAM  , not on disk 
    
    
    CREATE TABLE cache_data (
     id INT PRIMARY KEY,
     value VARCHAR(100)
    ) ENGINE = MEMORY;
    
    1. Super fast 
       
       data in memory , no disk i/o
       Read / write are very fast
    
    2. Not persistent 
         
         -> Server restart = Data gone 
         It's temporary storage   
       
"""