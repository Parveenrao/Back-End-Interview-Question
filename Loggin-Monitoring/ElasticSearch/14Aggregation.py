"""   
=> SQL Group by 
   Aggregation = Elasticsearch

-------------------------------------------------------------------------------------------------

=> Types Of Aggregation 

  
  1. Metric Aggregation 
       
       -> Find average price 
       {
           
           "size" :0 ,
           
           "aggs" : {
               
               "avg_price" : {
                   
                   "avg" : {"field" : "price"}
               }
           }
       }   


      -> Size = 0 , don't return documents 
      -> only return aggregation result
   
   
   2. Bucket Aggregation  
        
        -> Group by categor 
        
   
            {
           "size": 0,
           "aggs": {
           "category_group": {
           "terms": {
              "field": "category.keyword"
                 }
                }
               }
              }
    
    3. Bucket + Metric    
    
                
                       {
                 "size": 0,
                "aggs": {
                "category_group": {
                 "terms": {
                 "field": "category.keyword"
                        },
                      "aggs": {
                        "avg_price": {
                          "avg": {
                           "field": "price"
                               }
                             }
                             }
                             }
                            }
                        }         
    
    
    4. Multiple Aggregation 
    
                          GET products/_search
            {
           "size": 0,
           "aggs": {
               "max_price": { "max": { "field": "price" } },
            "min_price": { "min": { "field": "price" } },
            "avg_price": { "avg": { "field": "price" } }
                }
               }     
    
    
    5. Date histogram 
            
            
          
                   {
                  "size": 0,
                  "aggs": {
                 "sales_per_day": {
                   "date_histogram": {
                      "field": "order_date",
                        "calendar_interval": "day"
                       }
                        }
                      }
                       }
                       
                   -> Group by time                                   
"""