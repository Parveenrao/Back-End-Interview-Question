"""" 
=> Request Cache 
   
   -> Request cache store the final response  of search request at shard level
      
      NOt partial 
      NOt filter 
      Entire result
      
     Client Request
             ↓
   Query Execution (filters, scoring, aggregations)
             ↓
          Shard Result
             ↓
🔥   Request Cache (stores this)
             ↓
     Merged Response → User 

-----------------------------------------------------------------------------------------------

-> What exactly cache 
   
   1. Aggregations 
   2. Total hits 
   3. Sometime hit 


-> Not ideal for 
    
    1. Random query 
    2. personalized result 
    3. constantly chagning data 

----------------------------------------------------------------------------------------------------

-> Key concept 
    
    1. Each shard maintains its own cache 
           Shard 1 → cache
           Shard 2 → cache
           Shard 3 → cache    
      
      
      -> Queries are computed per shard level 
      -> Result are merge later 

------------------------------------------------------------------------------------------------------

   {
    "size": 0,
    "aggs": {
    "category_count": {
      "terms": {
        "field": "category.keyword"
       }
       }
       }
     }                   
     
-> When cache is cleared
    
    1. New document is inserted 
    2. refersh happens
    3. Sgment changes 
    
    
    refersh_interval = 30s 
    
     cache live longer == better performance


-------------------------------------------------------------------------------------------------------------------

-> Request cache is used when the same query is executed again AND the data hasn’t changed  

-> Query must be identical 

-> data hasn't be changed 


-> Enalbe for cache (size = 0)

-> Off for normal search 


---------------------------------------------------------------------------------------------------------------------

=> If data changes → cache becomes invalid → query is recomputed

=>  Cache Key = Query + Segment State        

"""