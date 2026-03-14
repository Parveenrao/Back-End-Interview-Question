""" 

3. Write Around Pattern 

     -> Write around means 
        
        data is directly written in db and cache not updated 
        Cache is only udpated when data is read later
        
    -> Why Write - Around 
    
       This patter avoid cache pollution 
       
       
       THis is used in Write Heavy system
       
       -> User will see old data
       -> Consistency is not guranteed
       

4. Write behind Caching

   -> Application writes only to cache first , and the cache updates  the database later async
       
       database write are delayed
       
    -> Working 
        
        1. Client send an update request 
        2. Application write in cache 
        3. Background worker later flush to db 
    
    -> Example 
    
        Social media like 
        
        1. Millions or user liking the post 
        
            Redis handle writer operation 
            Background worker later flush like to db 
            
            so 1000 writes in cache and one write in db 
            
        
        -> Used in extremely write operation 
           Redis can handle 1m request
           db cannot 
    
       -> Risk of data loss 
          
          Redis write success 
          and db fails 
          
          data loss 
       
       -> Not strong eventual consisteny 
       
            redis like = 5000
            db  like = 4500          
                              


















































"""