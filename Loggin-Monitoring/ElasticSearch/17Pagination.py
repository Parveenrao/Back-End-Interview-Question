"""  
=> Pagination 

     -> Fetching result in chunks instead of all at once
     
     Total pdoducts = 100000
     You show = 10 per page






--------------------------------------------------------------------------------------------------

1. Basic (from/size)

      {
       
       "from" : 0
       "size: " 10       # Page 1 
     }     



->          {
      "from": 10,
       "size": 10       # Page 2
           }


-> Stil slow at scale 
      
      from 1000 , size 10 
      
      scan first 1000 documents , then returns 10 last
      
      limit =  max_result_window = 10000

-------------------------------------------------------------------------------------------------
2. Method 2 (search_after)
       
       -> instead of skip 1000 records
       
       give me result after this record
       
       {
           "size": 2,
          "sort": [
           { "price": "asc" },
             { "_id": "asc" }
              ],
          "search_after": [40000, "abc123"]
            }

----------------------------------------------------------------------------------------------------

-> Note

"sort": [
  { "price": "asc" },
  { "_id": "asc" }
]

always use sort 

add _id for tiebreaker                             
"""