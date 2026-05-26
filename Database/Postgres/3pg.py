""" 
=> JOSN Data Type 
    
    -> Java-scripts object notation

----------------------------------------------------------------------------------------------------

1. JOSN 
   
   -> stored as string
   -> slower 
   -> no index benfit


2. JOSNB
   
   -> stored in binary format
   -> faster queries
   -> SUpport indexing (GIN index)
   
   -> Remove duplicate keys
   
   
   
   create table user(
       Id BIGSERIAL primary key ,
       profile JSOB
   )
   
   
   INSERT into user(profle)
   values('{"name" :"Parveen" , "age" : 21}')
   
   
   select profile ->> 'name' from users;
   
   
   UPDATE users
   SET profile = jsonb_set(profile, '{age}', '22');         



--------------------------------------------------------------------------------------------

=> ENUM Data Type 
   
   -> fixed set of allowed value
   
   -> create 
   
      CREATE TYPE user_status as ENUM('pending' , 'active' , 'blocked')
      
      
      CREATE TABLE users (
      id BIGSERIAL PRIMARY KEY,
      name TEXT,
      status user_status
     );    
         
         
         INSERT INTO users(name, status)
         VALUES ('Parveen', 'active');
         
         
         ALTER TYPE user_status ADD VALUE 'suspended';
    
    
    -> Real example 
              
              
              CREATE TYPE order_status AS ENUM (
                 'pending',
                  'paid',
                  'shipped',
                   'delivered',
                   'cancelled'
                    );

             CREATE TABLE orders (
               id BIGSERIAL PRIMARY KEY,
               status order_status,
                created_at TIMESTAMPTZ
              );     
        
        -> Instead of enum hard coded values , use TEXT + check
       
       CREATE table user (
           
           id BIGSERIAL primary key ,
           name TEXT ,
           status TEXT CHECK (status IN ('pending' , 'active' , 'blocked'))
       )       

"""