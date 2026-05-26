"""        1. Fixed window Rate Limiting Algorithm    
         
           -> System allow a fixed no of request in a fixed time interval 
           
           
           => Example   
           
                ->  5 requests per minute
                
                    Request Arrives 
                    
                    
                    12:00:01 → request1 → allowed
                    12:00:05 → request2 → allowed
                    12:00:10 → request3 → allowed
                    12:00:15 → request4 → allowed
                    12:00:20 → request5 → allowed
                    12:00:30 → request6 → rejected

            AT ->  12:01:00
            
            counter reset
        
        
        => Problem   
           
            -> Brust Traffic problem  
            
               limit = 100 req/min 
               
               12:00:59 -> 100 request
               12:00:01 -> 100 request 
               
               2 -> second 200 request    


========================================================================================================================

=> Sliding Window 
     
     -> Instead of dividing into fixed time chunks(fixed window)
     
     -> Sliding window look at last N second from now  = continuously
     
     
  -> At any moment , count how many request happened in last X second
  
  
  -> Working 
      
      1. Store timestamp of request 
      2. ON new request 
           
           Remove old timestamp
           count remaining request 
           
           if count < limit -> allow
           
           else -> reject 
   
   
   Limit = 3 request / 10 
       
       t = 1 -> allow
       t = 2 -> allow 
       t = 3 -> allow
       t= 4 -> reject (already 3 in last 10 sec)
       
       t= 12 -> expired (t = 1  , expired)
       
         it slides , not reject     


=> Disadvantge 
      
      1. Store every request 
      2. Memory heavy 
      3. Not scalable


=> When it breaks 
    
    1. Million of users 
    
    This approach is expensive 

==========================================================================================================

=> Sliding window Counter 
    
    -> Instead of storing every request timestamp
    
    -> we store only counts of two windows
        
        1. current window
        2. Previous window
        
     
     estimated _count  = current_count + prev_cout * (remaining_time/window)   
     
     curr_count = request in current window
     prev_count = request in previous window
     
     remaining_time = how much of previous window still overlap
   
   
   -> Example 
      
      Limit = 10 request / 10 sec
      
      
      Previous window = 10 request
      Current window = 3 request 
      
      we are 4 seconds into current window
      
    Remaining overlap = 6 sec 
    
               count=3+10×(6/10)=3+6=9
        Allow request (since < 10)


==============================================================================================================

=> Token Bucket Algorithm 
     
     1. Imagine a bucket that hold token 
     2. Every request need 1 token 
     3. Token are added over time(refill)
     
     4. Bucket has max capacity
     
     5. If token availabel -> allow
     
     6. If empty -> reject
  
  -> Example 
     
     Bucket Capacity = 5 tokens 
     Refill = 1 token / sec
     
    Time 0 -> [5 tokens] -> user send 5 request -> all allowed
    
    Time 1 -> [1 token added] -> 1 request allowed
    
    Time 1 -> [1 token added] -> 1 request allowed
    



============================================================================================

=> Leaky Bucket 
   
   1. Imagine a bucket small hole at the bottom
   
   2. it leaks at constant rate 
   
   3. if too much water comes -> bucket overflow , request rejected 
   
   
   4. Output , rate is fised no matter how fast can be input 
 
 
 -> Example 
      
      Leak rate = 1 request / sec 
      capacity = 5 
      
      
      Time 0: 5 request -> bucket filled -> queued
      
      Time 1: 1 request  -> 4 left 
      
      Time 2: 1 processed -> 3 left 
      
      
      user send 3 more request 
      
      bucket overflow  -> reject extra       
                                                  
                             
               
                               




"""      