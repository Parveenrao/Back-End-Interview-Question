"""  
=> Schema Design 
   
   -> ElasticSearch is not a relation database 
   
   -> In ElasticSearch 
       
       1. You denormalized data 
       2. You optimized for search , speedd  not storage
       3. Design schema based on how you search, not how you store.


--------------------------------------------------------------------------------------------------------

1. Index (Database)
    
    -> Example = products , orders , users

2. Document (Row)
       
       -> Json object 

3. Field Column 
     
     Each field has a type 

-------------------------------------------------------------------------------------------------------------

=> Fiedl Type 
        
        1. Text (Full Text Search)
        
           Gets analyzed 
           used for searching 
       
        2. Keyword (Exact match)
              
              Not analyzed
              used for filtering, sorting  , aggregration 
        
        3. Numeric 
             
             used for calculations , sorting , range queries
        
        4. Date
            
            -> used for time-based queries  , logs analytics                  

----------------------------------------------------------------------------------------------------------------

PUT products
{
  "mappings": {
    "properties": {
      "name": {
        "type": "text",
        "fields": {
          "keyword": { "type": "keyword" }
        }
      },
      "category": { "type": "keyword" },
      "price": { "type": "integer" },
      "rating": { "type": "float" },
      "in_stock": { "type": "boolean" },
      "created_at": { "type": "date" },
      "reviews": {
        "type": "nested",
        "properties": {
          "user": { "type": "keyword" },
          "rating": { "type": "integer" },
          "comment": { "type": "text" }
        }
      }
    }
  }
}                         
           
       


"""