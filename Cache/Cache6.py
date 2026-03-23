"""  
   => Cache Penetration 
   
       -> Cache penetration happens when request ask for data that does not exist in database 
       
          beause the data not exist 
           
           1. It is not in cache 
           2. It is not database
           
        So every request to goes to db 
        
        If attackers send many request , all goes to db   -> DB overload
    
    
    -> Suppose valid user are 1 - 1000000
    
        some send -1 , this is not exist in db 
        
        Result  --  Because the data doesn't exist, cache never stores it, so the next request repeats the same process.
                     Infinite DB hits
    
    
    -> Solution 
    
      1. Cache NUll 
      
         if db return no data 
           cache null 
           Next request --> null
           No db query 
           
     2.  Bloom filter
        
         -> Large system use Bloom filters 
            A bloom filter quickly check whether a key exist or not 
            so no db query 
     
     3. Input validation 
        
        -> Validata request parameters 
           
           User id must be between 1 to 100000 
           if not return 400
     
     4. Rate limiting 
     
        Block abusive client 
        
        if too many invalid request
        IP blocked                                            



"""