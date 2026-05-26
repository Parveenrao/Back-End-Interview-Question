""" 
=> Nested - Parent Relationship
      
      
      -> ElasticSearch store data as flat json documents
      
           {
          "user": "parveen",
          "orders": [
          {"product": "iphone", "price": 1000},
          {"product": "shirt", "price": 50}
          ]
          
          }


-----------------------------------------------------------------------------------------------------

1. Nested Type 
     
   -> it store each object  as a separate  hidden document , preserving relation
   
   {
  "mappings": {
    "properties": {
      "orders": {
        "type": "nested"
      }
     }
      }
       
       }



-> Query 

              {
  "query": {
    "nested": {
      "path": "orders",
      "query": {
        "bool": {
          "must": [
            {"term": {"orders.item": "laptop"}},
            {"term": {"orders.price": 50}}
          ]
             }
               }
             }
            }
        }
        
-> When to use Nested 
    
   1. You need relation inside same document 
    
      orders -> Items 
      users -> Address
      Product -> Reviews
  
  2. Data is small to medium 
        Nested is expensive


--------------------------------------------------------------------------------------------------

2. Parent-Child Relationship 
    
    -> Link documents across different docs using join 
    
    
    Parent -> Product 
    Child  -> Review
    
                {
          "mappings": {
          "properties": {
          "relation": {
          "type": "join",
          "relations": {
          "product": "review"
         }
       }
     }
   }
  }  
  
  
  -> When to use parent-child 
  
    1. Very large data 
    
    2. One to many large relation 
           
           products -> millions of review
           Blog    -> Comments       
  
           
"""