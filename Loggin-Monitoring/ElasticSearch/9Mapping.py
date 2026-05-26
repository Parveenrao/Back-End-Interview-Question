"""
=> Mapping 
   
   -> Mapping Control 
      
      1. How data is stored 
      2. how data is indexed 
      3. how data is searched 
      4. how data is aggregated
      
      -> if mapping is wrong , whole search ssytem become slow 

---------------------------------------------------------------------------------------------

1. Fields Type 
   
   A. Text 
       
       -> Analyzed (broken into tokens)
       -> used for search 
   
   b. keyword  
       
       -> Not analyzed
       -> stored as is
       -> used for filtering , sorting, aggregation

2. Numeric Types 
    
    Integer 
    long 
    float 
    double 
    
    -> used for range queries , sorting , aggregations

3. Object 

   "user"  :{
       "name" : "parveen",
       :age" : 22
   }
   
   flat structure 

4. Nested Object 
    
    -> Array of objects 
    
    "reviews": [
  { "user": "A", "rating": 5 },
  { "user": "B", "rating": 1 }
]                       
"""


from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

mapping = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "name": {
                "type": "text",
                "fields": {
                    "keyword": {"type": "keyword"}
                }
            },
            "price": {"type": "integer"},
            "category": {"type": "keyword"},
            "description": {"type": "text"}
        }
    }
}

# Safe create (avoid error if exists)
if not es.indices.exists(index="products"):
    es.indices.create(index="products", body=mapping)
    
    
from elasticsearch import helpers

actions = [
    {
        "_index": "products",
        "_id": 1,
        "_source": {
            "name": "iPhone 14 Pro",
            "price": 120000,
            "category": "mobile",
            "description": "Apple smartphone with A16 chip"
        }
    },
    {
        "_index": "products",
        "_id": 2,
        "_source": {
            "name": "Samsung Galaxy S23",
            "price": 90000,
            "category": "mobile",
            "description": "Android flagship phone"
        }
    },
    {
        "_index": "products",
        "_id": 3,
        "_source": {
            "name": "OnePlus 11",
            "price": 65000,
            "category": "mobile",
            "description": "Fast and smooth Android phone"
        }
    }
]

helpers.bulk(es, actions)

mapping = es.indices.get_mapping(index="products")
print(mapping)    