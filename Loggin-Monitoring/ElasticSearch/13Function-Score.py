""" 
=> Function Score in Elastic Search 
   
   -> By default , ElasticSearch use BM25 , scoring algorithm to rank documents
   
   -> WHy function score 
      
      1. Boost expensive products
      2. Boost recent documents
      3. Boost popular items (like , views)
      4. Demote outdated items

   
   
   -> Core Idea  
   
     1. Elasticsearch find documents using must , term 
     2. Then fuction score modify their score

--------------------------------------------------------------------------------------------

1. Base Query    
    
    "query" : {
        "match" : {
            "description" : "apple"
        }
    }
    
  -> This gets initial BM25 score    
  
2. Function (Heart) 
    
    -> Each function modify score
    
    {
  "filter": { "term": { "category": "mobile" } },
  "weight": 2
    }
    
    if document is mobile , score * 2
    
     
3. Score mode
     
     -> When multiple function exist 
      
      1. add       = add score
      2. multiply  = multiply 
      3. average   = average 
      4. max       = take max       

4. Boost mode 
    
    -> How function score combine with  original score 
    
        1. multiply = default 
        2. sum = add 
        3. replace  = ignore original score
   
   
              
""" 

from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

print(es.info())

index = "products"


# create index 
    
mapping = {
          
          "mappings" : {
              
              "properites" : {
                  
                  "name" : {"type" : "text"},
                  "description" : {"type" : "text"},
                  "category" : {"type" , "keyword"},
                  "price" : {"type", "float"},
                  "rating" : {"type" , "float"}
              }
            }
           
    }

if es.indices.exists(index=index):
    es.indices.delete(index=index)
    

es.indices.create(index=index , body = mapping)

# Insert docs
docs = [
    {"name": "iPhone 14", "description": "Apple smartphone", "category": "mobile", "price": 1000, "rating": 4.8},
    {"name": "Samsung Galaxy", "description": "Android phone", "category": "mobile", "price": 800, "rating": 4.5},
    {"name": "Apple MacBook", "description": "Apple laptop", "category": "laptop", "price": 2000, "rating": 4.9},
]

for i , doc in enumerate(docs):
    es.index(index=index , id= i+ 1, document=doc)

es.indices.refresh(index=index)    
        
        
query = {
    "query": {
        "function_score": {
            "query": {
                "match": {
                    "description": "apple"
                }
            },
            "functions": [
                {
                    "field_value_factor": {
                        "field": "rating",
                        "factor": 1.5,
                        "modifier": "sqrt",
                        "missing": 1
                    }
                }
            ],
            "boost_mode": "multiply"
        }
    }
}

res = es.search(index=index, body=query)

for hit in res["hits"]["hits"]:
    print(hit["_source"], hit["_score"])
    

""" 
-> Important function u should know 
   
1. Weight  
    
    {"wieght = 2}

2. field_value_factor 
       
       {
  "field_value_factor": {
    "field": "rating",
    "factor": 1.2,
    "modifier": "log1p",
    "missing": 1
        }
        }


3. Decay function 
      
      1. Used for time decay 
      2. Distance deacy


4. Script score 

           {
  "script_score": {
    "script": {
      "source": "doc['rating'].value * 2"
    }
  }
}      



"""    