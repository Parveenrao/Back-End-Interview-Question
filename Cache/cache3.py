"""   => Cache Strategy 

       
       1. Cache - Aside ( Lazy Loading)
         
          -> Application first check cache first , it data is not present , fetch from database and store in cache
          
              Client --> Application --> Cache -> Database
              
              1. Application first check cache
              2. If cache hit , return data
              3. If cache miss , fetch from db
              4. store the data in cache 
              5. return result
        
        def get_user(id):
        
        cache = redis.get(f"user : {id}")      
        
        if cache:
            return cache
        
        
        user = db.get_user(id)
        
        redis.set(f"user :{id}" , ex = 60)
        
        return user
        
        
        -> cache only store frequent data
        -> First request is always slow
    
    
    2. Write Through Cache     
    
      -> Whenever your application write or update   , it writes to cache and db at the same time 
      
          Client
            |
 
       Application              -> Both stay consistent 
            |
  
       Cache (Redis)
           |
                                      
        Database   


      => Flow 
         
         1. Client send update request 
         2. Application write data to cache 
         3. Redis writes the same data to databse
         4. Cache and DB remain sync.
         
         
         
         import redis
         import psycopg2

         r = redis.Redis()

         def update_user(user_id, name):

          # write to cache
           r.set(f"user:{user_id}", name)

          # write to database
           cursor.execute(
        "UPDATE users SET name=%s WHERE id=%s",
        (name, user_id)
         )
        conn.commit()
        
        
        
        -> Write latency increased write to cache and db same time
         
         -> cache m/m is high useless cache also written
         
         -> Unnecessary cache writes  -> even if data is rarely used still it go to cache
        
        -> used when strong consistency required
        -> Data is frequently read
        
      -> Problem in write through 
         
         redis writed success 
        db failss
        
        -> Solution 
           
           use retry 
           message queue   









"""