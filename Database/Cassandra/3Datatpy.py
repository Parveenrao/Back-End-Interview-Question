"""" 
=> Collection data type 
     
     1. LIST 
        
        -> Odered , allow duplicate
        
        skills LIST<TEXT>
        
        INSERT INTO users (user_id, skills)
        VALUES (uuid(), ['python', 'java', 'python']);
         
         
         -> When to use 
             
             1. Small data 
             2. avoid when data is large
             
             3. Because Cassandra rewrites collection internally → slow
     
     2. SET 
        
        -> No duplicate
        -> unodered
        
        
        tage<TEXT>
        
        INSERT INTO posts (post_id, tags)
        VALUES (uuid(), {'tech', 'ai', 'tech'});
    
     3. MAP 
        
        -> Key - value pair
        -> Like dictionary
        
        
        preferences MAP<TEXT, TEXT>    
     
                

"""