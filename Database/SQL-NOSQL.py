"""" 
=> COre difference between SQL AND NOSQL

----------------------------------------------------------------------------------------------------- 
=> SQL 
    
    1. Structure 
       
       -> Data stored in the form of table (rows and columns)
       -> Fixed schema (Define structure before inserting data)
    
    
    2. Schema 
       
       -> Strict Schema 
       
       -> Predefined structure
    
    3. Relationship 
        
        -> Strong relationship using joins 
        
        -> Support joins
    
    4. Scaling 
       
       -> Often use vertical scaling (RAM / CPU)
    
    5. Transaction 
    
       -> FULL ACID compliance 
       -> Relaiable for banking and finance 
    
    6. Uses 
       
       -> When Need strong consistency 
       -> Relationship matters
       -> Data is structured 

----------------------------------------------------------------------------------------------

=> NOSQL 
   
   1. Structure 
       
       -> Data stored as json documents 
       -> key-value 
       -> graphs 
     
     => NO fixed schema
    
   2. Schema
     
     -> Dynamic / flexible schema 
   
   3. Relationship 
      
      -> Usually no joins 
      -> Data is often embedded 
   
   4. Scaling 
       
       -> Horizontally scaling (add more cpu / ram)
   
   5. Transaction 
     
     -> Often eventual consistency 
     -> Faster but less strict 
   
   6. Uses
       
       -> Use when 
          
          1. Data is flexible 
          2. Huge scale 
          3. High speed required 
          
       Chat apps 
       Real - time analytics                                         
       
"""