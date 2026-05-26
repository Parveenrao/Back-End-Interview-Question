"""  
=> Analyzer 
   
   -> Pipelines of 3 steps 
        
        1. Character Filters 
        2. Tokenizer (core)
        3. Token Filters

---------------------------------------------------------------------------------------------------------------

1. Tokenzier 
    
    -> It decide how text is split 
    
    a. Standard 
         
         "Apple iphone 14"  -> ["apple" , "iphone" , "14"]  , best for normal text
    
    b. whitespace 
         
         "Apple iPhone 14" → ["Apple", "iPhone", "14"] , no lowercase , no clearning 
    
    c. keyword
    
        "Apple iPhone 14" → ["Apple iPhone 14"] , whole text = one token 
        
        used for exact search , sorting 


2. Token Filters 

     A. Lowercase Filters
         
         "Apple" = apple
     
     B. Stepwords filters 
        
        "this is iphone  = "iphone"
     
     C. Stemmer 
           
           "running" = "run"
           "phones" = "phone"
     
     d. Synonym filter 
         
         "mobile" = "phone" 
         
         user search mobile , get phone

3. Character Filters 
       
       -> used before tokenization 
       
       "i-phone" = iphone                                   
         
                      
        




"""

from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

res = es.indices.analyze(
    body={
        "analyzer": "standard",
        "text": "Apple iPhone 14!!!"
    }
)

print(res)

# Custom Analyzer 


index_name = "products_custom"

mapping = {
    "settings": {
        "analysis": {
            "analyzer": {
                "my_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "stop"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "description": {
                "type": "text",
                "analyzer": "my_analyzer"
            }
        }
    }
}

if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

es.indices.create(index=index_name, body=mapping)

# Synonym Analyzer 

mapping = {
    "settings": {
        "analysis": {
            "filter": {
                "synonym_filter": {
                    "type": "synonym",
                    "synonyms": [
                        "phone, mobile",
                        "laptop, notebook"
                    ]
                }
            },
            "analyzer": {
                "synonym_analyzer": {
                    "tokenizer": "standard",
                    "filter": ["lowercase", "synonym_filter"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "description": {
                "type": "text",
                "analyzer": "synonym_analyzer"
            }
        }
    }
}