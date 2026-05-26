""" 
=> UUID Data Type 
    
    1. Random unique identifier
    2. No ordering
    3. No time info
    
    
    create table users (
        user_id uuid , primary key,
        name text
    )
   
     -> uniqueness only
     -> cannot sort by time
     -> cannot know when it was created 

-------------------------------------------------------------------------------------------

=> TIMEUUID 
    
    -> Unique ID + timestamp embedded
    -> Automatically sortable by time
    
    
        CREATE TABLE posts (
         user_id UUID,
         post_id TIMEUUID,
         content TEXT,
         PRIMARY KEY (user_id, post_id)
        );
        
        INSERT INTO posts (user_id, post_id, content)
         VALUES (uuid(), now(), 'Hello world');     
"""