"""" 
=> Fan-out-write
     
     -> write once , copy to many timelines
     
     
     -> When a user create content  , the system  immedaitely distribute (pushes) that content to all follower feed
     
     -> Instead of computing feed later , we pre-compute them at write time

-----------------------------------------------------------------------------------------------------------------------

-> Working / Flow 
    
    Let say user post something
    
    User A  posts -> sytem find followers -> push post to each follower feed 
    
    
    1. user A create post
    2. save post in main DB
    3. Fetch followers of A
    4. For each followers
          
          insert post into their feed table / cache
          
          
          
                User A
                  ↓
                New Post
                  ↓
            ┌───────────────┐
            │ Fan-out Logic │
            └───────────────┘
               ↓     ↓     ↓
             User B User C User D
             Feed    Feed   Feed    
    
    
    -> We do heavy work , before user open app 
    
    -> instant loading 
    
    -> no lag 
    -> smooth scrolling

-------------------------------------------------------------------------------------

-> We do not do synchronously
    
    is user has 1M follower then it will systme
 
 
-> Real implementaton
    
    1. Background jobs
    
    2. queus 
    
    3. async workers 
    
 
  User post 
     |
  Save post
     |
  Send event to queue
     |
  worker consume event 
     |
  Worker fan-out-followers
  
  
  
-------------------------------------------------------------------------------------------------

-> Where to store feed
    
    1. Database
       
       feed(user_id , post_id) 
       
       can become huge
    
    
       -> Lets suppose user has 1 M followers
           
          1. Biggest problem write explosion 
             
             we do 1M insert 
             
             lock resource 
             choke on write throughput
          
          
          2. Hot partition / hot rows
             
             -> if many users follow popular content
             
             -> same shard / partition get hammered
             
             -> uneven load , degraded performance
          
          
          3. Expensive index 
              
              -> To keep reads fast , we index on (user_id , created_at)
              
              -> but , every write / insert update index
              
              -> index size grow
              
              write become slower
           
           4. Storage cost 
               
               -> You are duplicating data 
                  
                  same post stored in millions of feeds
                  
                  huge storage overhead

-------------------------------------------------------------------------------------------

=> What to do in Real life 
     
     cache + hybird db
     
     hot data stored in cache 
     
     cold data store in mysql                           
                   
                                   


"""