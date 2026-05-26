""" 
=> Full TeXt Query 
     
     full text = elastic search understand languauge , not just exact values
     
   
   -> internally what happens 
   
   
   GET products/_search
  {
  "query": {
    "match": {
      "description": "Apple iPhone 14"
    }
   }
   } 
   
   
   1. Input text 
         
         "Apple iphone 14"
         
   2. Ananlyer break it 
       
       ["apple" , "iphone" , "14"]
   
   3. Seach in inverted index 
       
       FIND DOCS CONTAINING THESE TOKENS 
   
   4. Scoring (BM25) 
   
     more match  = high score 
     important words = high score

------------------------------------------------------------------------------------

=> Or & And Behaviuor 
         
         "match": {
  "description": "apple iphone"
      }     
      
      
=> Force ANd



"match": {
  "description": {
    "query": "apple iphone",
    "operator": "and"
  }
}           

=> Minimum should match 

"match": {
  "description": {
    "query": "apple iphone 14 pro",
    "minimum_should_match": "75%"
  }
}

means 75 % should match 

useful in seach engine
type tolerance

=> Fuzziness 


"match": {
  "name": {
    "query": "iphnoe",
    "fuzziness": "AUTO"
  }
}

still matches  iphone


=> Match phrase (Order matters )

"match_phrase": {
  "description": "apple iphone"
}

math by apple iphone is great 

not by great apple iphone


=> Slope 


"match_phrase": {
  "description": {
    "query": "apple iphone",
    "slop": 2
  }
}

all some word gap

=> Multi_match 

"match_phrase": {
  "description": {
    "query": "apple iphone",
    "slop": 2
  }
}

search multile fields

=> Cross fields  

"multi_match": {
  "query": "iphone apple",
  "fields": ["brand", "name"],
  "type": "cross_fields"
}

treat field as one

          


"""

from elasticsearch import Elasticsearch 

es = Elasticsearch("http://localhost:9200")
print(es.info())

index_name = "products"

mapping =   {
             "mappings" : {
                 "properties" : {
                     
                     "name" : {"type" : "text"},
                     "description" : {"type" : "text"},
                     "category" : {"type" : "keyword"},
                     "price" : {"type" : "integer"}
                 }
             }
}

# delete index in  exist 

if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)
    
es.indices.create(index=index_name , body = mapping)

print("Index Created")    


docs = [
    {"id": 1, "name": "iPhone 14", "description": "Apple smartphone with A15 chip", "category": "mobile", "price": 80000},
    {"id": 2, "name": "iPhone 14 Pro", "description": "Apple premium smartphone with great camera", "category": "mobile", "price": 120000},
    {"id": 3, "name": "Samsung Galaxy S23", "description": "Samsung flagship phone", "category": "mobile", "price": 90000},
    {"id": 4, "name": "Dell Laptop", "description": "Powerful laptop for developers", "category": "laptop", "price": 70000},
    {"id": 5, "name": "Apple MacBook Air", "description": "Lightweight laptop with M1 chip", "category": "laptop", "price": 95000}
]

for doc in docs:
    es.index(index=index_name, id=doc["id"], document=doc)

es.indices.refresh(index=index_name)

print("Documents inserted")


# 1. Simple match query

query = {
    "query": {
        "match": {
            "description": "apple"
        }
    }
}

res = es.search(index=index_name, body=query)

for hit in res["hits"]["hits"]:
    print(hit["_source"])
    

# 2. match with ANd 




query2 = {
    "query": {
        "match": {
            "description": {
                "query": "apple smartphone",
                "operator": "and"
            }
        }
    }
}    

res2 = es.search(index=index_name, body=query2)

for hit in res2["hits"]["hits"]:
    print(hit["_source"])
    
# 3. Fuzziness 

query3 =  {
    
         "query" : {
             
             "match" : {
                 "name" : {
                     
                     "query" : "iphoen",
                     "fuzziness" : "AUTO"
                 }
             }
         }
}

res3 = es.search(index=index_name , body = query3)

for hit in res3["hits"]["hits"]:
    print(hit["_source"])
    
# 4. multi match

query4 = {
    "query": {
        "multi_match": {
            "query": "apple laptop",
            "fields": ["name", "description"]
        }
    }
}    

res4 = es.search(index=index_name , body = query4)

for hit in res4["hits"]["hits"]:
    print(hit["_source"])