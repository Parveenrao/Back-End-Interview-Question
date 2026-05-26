"""  
=> Cache 
    
    -> Elastic-Search cache is about avoiding repeated work at shard level

----------------------------------------------------------------------------------------

1. Query cache 
   
   -> Query cache store filter query result as bitsets per segment per shard 
   
   -> When you run a filter like 
   
   {
       "term" : {"category" : "mobile"}
   }    
   
   1. Scan document
   2. Finds matching docs
   3. Store result 
   
   -> Next time same query runs 
      
      1. It does not scan again 
      2. It reused stored result 
  
  -> What exactly stored 
       
       1. Not document
       2. Not full response 
       
          -> A bitset (bitmap)
  
  ->  DocID:     1   2   3   4   5   6
      category:  M   L   M   M   L   M        
      
      filter = category 
      [1, 0, 1, 1, 0, 1]
      
      1  -> match 
      0  -> not match
      
      Bit operational are extremely 
      Combining filter  = AND/OR operation on bisect
   
   
   -> Where  Query cache 
      
      1. Per shard 
      2. per segment 
    
    -> Segment
        
        each shard has multiple segments
        
        shard 1: 
        Segment A
        Segment B
        Segment C         

       cache is stored per segment
    
    -> Why cache matters 
    
       When new data comes 
       
       New segment is created 
       old segment remains 
       cache is not resused for every segments
       
       so cache is partially invalidated
    
    -> Cache lifestyle 
       
       1. Scan segment 
       2. build bisect 
       3. store in cache 
       
      2nd query 
        
        check cache 
        resue bisect 
        skip computation
    
    
    -> After index update 
        
        1. New segment created 
        2. cache miss  for new segment 
        3. partial recompute
    
    -> When query cache is used 
    
      1. Filter context
      2. Not used in query context
   
   -> Conditions for Cache Hit

        ✔ Same query structure
        ✔ Same field + value
        ✔ Segment unchanged
        ✔ Filter context          
   
   -> Cache miss 
          
          Cache Miss Happens When
          Query changes slightly
          New documents indexed
          Different filters used
          High cardinality fields       
    
    -> High cardanilty problems 
        
        1. Low cardnality      
             
             category = ["mobile" , "laptop" , "tablet"]
             
             only 3 values , good for caching  , fast filters
             
             many people search this 
        
        2.  User_id 
             
             [1, 2, 3 , -------------, million]
             
             almost every query in unique
             
             only one person use
 
 
 ->  Reduce Refresh Frequency

           Frequent refresh → cache invalidation            
 
 -> use low cardnality fields
 
 
 -> Query cache stored in heap 
    limited size          
"""