"""  
=> Output
   
   -> Where processed data is sent


------------------------------------------------------------------------------------------------------------

1. stdout 
    
    -> Print logs in terminal 
    
    output {
        stdout {
            codec => rubydebug
        }
    }

-----------------------------------------------------------------------------------------------------------

2. ElasticSearch 
    
    output {
        elasticsearch {
            hosts => ["http://localhost:9200"]
            index => "my-logs"
        }
    }       
    
    
    -> send data to elasticsearch


-----------------------------------------------------------------------------------------------------------=-----

3. Send To file 
     
     output {
             file {
           path => "/tmp/output.log"
          }
        }    
        
    -> Sent processed logs to file 

---------------------------------------------------------------------------------------------------------------------

4. Multiple output 
    
    output {
         file {
         path => "/tmp/output.log"
         }
      }    


----------------------------------------------------------------------------------------------------------------------

5. Conditional Output 
                
     output {
        if [level] == "ERROR" {
         elasticsearch {
         index => "error-logs"
         }
           } else {
             elasticsearch {
            index => "general-logs"
            }
         }
       }
"""