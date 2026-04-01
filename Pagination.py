"""    => Pagination 

           -> Pagination means breaking large data into smaller chunks (pages) insted of returing everthing at once
           
         Example  -> Suppose a table has 1M rows
         
                        -> Instead of returing all rows , we return 10- 20 rows per request
                              
                              GET /users?page=1&limit=10
                        
                        Page 1 → rows 1-10
                        Page 2 → rows 11-20
                        Page 3 → rows 21-30   
                        
            -> Reduce DB load 
            -> Improve API response time 
            -> Save netork bandwidth
          
          Without pagination --> all 1M records returns -> slow api
-----------------------------------------------------------------------------------------------------------------------------


1. Offset Pagination 
   
    -> Skip some rows and  return the next set of rows
    
       uses limit + offset in sql 
       
        SELECT * FROM users   -> skip first 20 rows and return next 10 rows 
        LIMIT 10 OFFSET 20;       
        
        
        
        def get_users(page, limit):

         offset = (page - 1) * limit
         return db.execute(query, (limit, offset))        
         
    
    -> Offset is not good for large tables 
    
       like  select * from user limit 10 , offset = 10000 
       
       DB scan row 1, 2, 3, ---- 10000   very expensive for large tables 
    
    
    -> When offset Pagination is good 
    
       When database have record less than < 10k
       static data
---------------------------------------------------------------------------------------------------------------------

2. Cursor based pagination  

    -> Instead of asking page number , client sends a cursor (a pointer to last item recieved) 
    
    -> The server returns the next set of records after that cursor.       
    
     Give me the next 10 records after this record.
                          
     
     SELECT * FROM posts
     WHERE id > 5
     ORDER BY id
     LIMIT 5;      
     
     
     -> Why cursor based pagination is fast 
         beacuse db direct jump using index
    
         
    def get_posts(cursor: Optional[int] = None, limit: int = 5, db: Session = Depends(get_db)):

    query = db.query(Post).order_by(Post.id)

    if cursor:
        query = query.filter(Post.id > cursor)

    posts = query.limit(limit).all()

    next_cursor = posts[-1].id if posts else None

    return {
        "data": posts,
        "next_cursor": next_cursor
    }                    

    
    in real system cursor pagiation does use column  , it is encoded by some value 
    
    
-----------------------------------------------------------------------------------------------------------------------

3. Keyset Pagination  

   -> key set pagination return result by using last seenkey like (id ,created_at)
   
   
        SELECT *
        FROM users
        WHERE id > 1000
        ORDER BY id
        LIMIT 10;    
        
        
        The database jumps directly using an index, which is much faster.
        
        
        def get_users(last_id=None, limit=5):

    if last_id:
        query = 
        SELECT *
        FROM users
        WHERE id > {last_id}
        ORDER BY id
        LIMIT {limit}
        
    else:
        query = f
        SELECT *
        FROM users
        ORDER BY id
        LIMIT {limit}
        

    users = db.execute(query)

    next_key = users[-1]["id"] if users else None

    return {
        "data": users,
        "next_key": next_key
    }


-------------------------------------------------------------------------------------------------

=> Problem with Normal key Pagination 

   simple key use one column  
   
     created_at < last_timestamp 
     
     
   sometim created-at dataa timestamo are not not unique   
   
   
   id	created_at
101	     10:00
102	     10:00
103	     10:00
104	     09:59
105      09:58  


imagine 

i run a query select * from users order by created_at limit 2

data = 101 , 102 

last timestamp = 10:00

now 

WHERE created_at < '10:00'

103 is lost 


-> so that solution is use compoist key
       
       SELECT *
FROM posts
WHERE (created_at, id) < ('10:00', 103)
ORDER BY created_at DESC, id DESC
LIMIT 3;

this will give correct ordering 


"""