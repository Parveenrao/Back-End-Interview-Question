"""  
1. Input in Logstash 
    
    -> where your data enter pipeline
        
        where is my data coming from
        
 
---------------------------------------------------------------------------------------

1. stdin{}
    
    input { 
          stdin{}
         }       
         
    -> Type and logstash , read it 

2. File Input 
    
    input {
         
         file {
             
             path => "/var/log/app.log",
             start_position => "beginning"
         }
    }          
    
    -> Used in backend app , system apps , System logs

3. HTTP input 
     
     -> Recieve data from api 
     
     input {
         
         http {
             port => 8080
         }
     }

4. kafka 

     input {
          kafka {
            bootstrap_servers => "localhost:9092"
            topics => ["logs"]
            }
           }        


-------------------------------------------------------------------------------------

input {
  file {
    path => "/var/log/app.log"
    start_position => "beginning"
    sincedb_path => "/dev/null"
    mode => "read"
  }
}

-> Since_db == read logs again and again from starting

-> mode = read  , Read entire file once , doest not for new data

-> mode = tail , Read new lines as they are added , keeps watching the file             

"""