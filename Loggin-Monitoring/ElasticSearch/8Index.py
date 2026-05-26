from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

doc = {
     
     "name" : "i_phone",
     "price" : 70000,
     "category" : "mobile"
}

response = es.index(index="products" , id=1 , document=doc)  
print(response)


# Bulk insert 

from elasticsearch import helpers

actions = [
    {
        "_index": "products",
        "_id": 1,
        "_source": {"name": "iPhone 14", "price": 80000}
    },
    {
        "_index": "products",
        "_id": 2,
        "_source": {"name": "Samsung Galaxy", "price": 70000}
    }
]

helpers.bulk(es, actions)