""" 
=> Index-Design 
    
    1. How many indices
    2. How many shards
    3. how data is distributed
    4. how queries will perform at scale


--------------------------------------------------------------------------------------------

=>  First Principle 
    
    You design index based on query pattern + data size + Pattern
    

--------------------------------------------------------------------------------------------

1. Index(single / multiple)
    
    -> One single index (all data in one place)
    
   -> multiple index
   
      products_2024
      products_2025     
        
          Time based partitioning

2. Shard 
    
    -> Index in split into pieces  
    
    
    
       PUT products
        {
         "settings": {
        "number_of_shards": 3
        }
       }          

      -> Horizontal scaling , parallel processing , large data handling 

3. Replica 
         
    -> copy of shard 
     "number_of_replicas": 1
      
      
      Fault tolerance 
      High availability 
      Better read performance


--------------------------------------------------------------------------------------------------------------------

PUT products
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1,
    "refresh_interval": "1s"
  },
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
      "created_at": { "type": "date" }
    }
  }
}                 
      
"""