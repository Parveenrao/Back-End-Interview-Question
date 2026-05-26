"""  
=> Multi-Field 
    
    -> Storing the same field in multi ways  for different purpose
     
    -> You take one field and index it in multiple format
  
  
  -> A multi-field allows a single field to be indexed both as text (for search) and keyword 
            (for exact match, sorting, aggregation).
  
  
  
  "name": {
  "type": "text",
  "fields": {
    "keyword": { "type": "keyword" }
     }
        }

-------------------------------------------------------------------------------------------------------------------------

=> Match query 
    
    {"query" : {"match" : {"name" : "iphone"}}}      


=> Exact match 
                
                
  { "query":   "term": {"name.keyword": "Apple iPhone 14" } }     }       

=> Sorting 
 
      {"sort": [  { "name.keyword": "asc" }]}
      
      
      
    
-------------------------------------------------------------------------------------------

=> 

    "name": {
    "type": "text",
    "fields": {
    "keyword": { "type": "keyword" },
    "lowercase": {
      "type": "text",
      "analyzer": "lowercase"
    }
    }
       }
"""