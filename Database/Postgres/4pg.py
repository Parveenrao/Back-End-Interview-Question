""" 
=> Array data type 
   
   -> array let u store multiple value in single column
   
     one user    - many tags 
     one product - many category
     
     
     CREATE TABLE posts (
     id BIGSERIAL PRIMARY KEY,
     title TEXT,
     tags TEXT[]
     );

     INSERT INTO posts(title, tags)
     VALUES ('PostgreSQL Guide', ARRAY['db', 'sql', 'backend']);
     
     # get full array 
     
     select tag from post
     
     # access element 
     
     select tag[1] from post , in postgres array are 1 based index 
     
     # search inside array 
        
        
        SELECT * FROM posts
         WHERE 'sql' = ANY(tags);
     
     # update array 
     
       
       UPDATE posts
      SET tags = array_append(tags, 'performance');    
"""