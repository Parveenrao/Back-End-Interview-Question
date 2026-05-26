from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

print(es.info())

index_name = "products"

mapping = {
          
          "mappings" : { 
              
              "properties" : {
                  
                  "name" :{"type" : "text"}  ,           # full text
                  "description" : {"type" : "text"} ,    # full text
                  "category" : {"type" : "keyword"} ,    # exact match
                   "price": {"type": "integer"}
              
              
              }}  
}

if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)


es.indices.create(index=index_name, body=mapping)

print("Index created")


docs = [
    {"id": 1, "name": "iPhone 14", "description": "Apple smartphone with A15 chip", "category": "mobile", "price": 80000},
    {"id": 2, "name": "iPhone 14 Pro", "description": "Apple premium smartphone", "category": "mobile", "price": 120000},
    {"id": 3, "name": "Samsung Galaxy S23", "description": "Samsung flagship phone", "category": "mobile", "price": 90000},
    {"id": 4, "name": "Dell Gaming Laptop", "description": "High performance gaming laptop", "category": "laptop", "price": 70000},
    {"id": 5, "name": "Apple MacBook Air", "description": "Lightweight laptop with M1 chip", "category": "laptop", "price": 95000}
]

for doc in docs:
    es.index(index=index_name, id=doc["id"], document=doc)

es.indices.refresh(index=index_name)

print("Data inserted")   


# Simple match 

query = { 
         
         "query" : {
             "match" : {
                 "description" : "apple"
             }
         }} 


res = es.search(index=index_name , body = query)

for hit in res["hits"]["hits"]:
    print(hit["_score"] , hit["_source"])                 # full text search
    

query1 = {
         
         "query" : {
             "bool" : {                                           # use bool when we have multiple conditions
                 "must" : [
                     
                     {                                             # must = exact match
                         "match" : {"description" : "apple"}
                     }
                 ],
                 
                 "filter" : [
                     
                     {
                         "term" : {"category" : "mobile"}         # term exact match 
                     }
                 ]
             }
         }
}    

res2 = es.search(index=index_name , body = query1)

for hit in res2["hits"]["hits"]:
    print(hit["_source"])
    
    
# Add rangee  

query2 = {
    
    
       "query" : {
           "bool" : {
               "must" : [
                   
                   {
                       "match" : {"description" : "apple"}
                   }
               ],
               
               "filter" : [
                   
                   {"term" : {"category" : "mobile"}},
                   {"range" : {"price" : {"lte" : 100000}}}
               ]
           }
       }
}    

res3 = es.search(index=index_name , body = query)

for hit in res3["hits"]["hits"]:
    print(hit["_source"])


# Add must_not 

query4 = {
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "description": "phone"
                    }
                }
            ],
            "filter": [
                {"term": {"category": "mobile"}}
            ],
            "must_not": [
                {"match": {"name": "samsung"}}
            ]
        }
    }
}    

res4 = es.search(index=index_name , body = query4)

for hit in res4["hits"]["hits"]:
    print(hit["_source"])
    
    
# Add should (boost ranking)

query = {
    "query": {
        "bool": {
            "must": [
                {"match": {"description": "phone"}}
            ],
            "should": [
                {"match": {"name": "iphone"}}
            ],
            "filter": [
                {"term": {"category": "mobile"}}
            ]
        }
    }
}    

# All phone returned , iphone get higher score


#-------------------------------------------------------------------------------

query = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": "apple phone",
                        "fields": ["name", "description"]
                    }
                }
            ],
            "filter": [
                {"term": {"category": "mobile"}},
                {"range": {"price": {"lte": 100000}}}
            ],
            "must_not": [
                {"match": {"name": "samsung"}}
            ],
            "should": [
                {"match": {"name": "iphone"}}
            ]
        }
    }
}

res = es.search(index=index_name, body=query)

for hit in res["hits"]["hits"]:
    print(hit["_score"], hit["_source"])                # final 