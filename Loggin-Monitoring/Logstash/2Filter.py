""" 
=> Filter 
   
    -> Where raw data become usefull
       
       transform + clean  + Extract data
   
   -> Input give this 
       
       error user = 123  login failed at 10:03
    
   -> After filter    
       
       {
           "level"  :  "error",
           "user:   :   123,
           "action" :  "login failed",
           "time"   :  "10:30"
       }        
   
   -> What filter does 
        
        1. Extract fields 
        2. Rename fields 
        3. Remove data
        4. Covert type 
        5. Add new field
        6. Parse format

-------------------------------------------------------------------------------------------------------------

1. GROK
    
    -> A pattern matching tool to extract data from text 
    
    filter {
         
         grok {
             
             match => {"message" => "%{WORD:level} user = %{NUMBER:user} %{GREEDYDATA:msg}}
             } }   
    
    
    -> Input =  error user = 123 login failed
    
    -> Filter 
        
        {
            "level" : "error",
            "user"  : "123",
            "msg"   : "login failed"
        }
        
        %{IP}	                IP address	192.168.1.1
        %{TIMESTAMP_ISO8601}	timestamp	2024-01-01
    
    
    -> Input = INFO user=456 action=login status=success
    
    -> Filter 
    
       filter {
           grok {
            match => {
                "message" => "%{WORD:level} user=%{NUMBER:user} action=%{WORD:action} status=%{WORD:status}"
                 }
              }
            }
        

---------------------------------------------------------------------------------------------------------------------

2. Mutate 
    
    -> Modify , clean , shape data 
    
    -> Grok = extract fields , mutate => edit those fields
    
   -> GROk 
      
          {
      "level": "error",
      "user": "123",
      "msg": "login failed"
      }  
    
   -> Mutate 
        {
     "level": "ERROR",
     "user": 123,
     "msg": "login failed"
     }     
           
     string -> convert -> integer
     lowercase -> convert -> uppercase
 
 
 filter {
  grok {
    match => { "message" => "%{WORD:level} user=%{NUMBER:user} %{GREEDYDATA:msg}" }
  }

  mutate {
    convert => { "user" => "integer" }         ->  convert user = "123" into 123
    uppercase => ["level"]                     ->  convert level into uppercasee 
    rename => { "msg" => "message_text" }
    add_field => { "env" => "dev" }
    remove_field => ["host"]
  }
}         

   -> split and  join also 


----------------------------------------------------------------------------------------------

3. Date Filter 
    
    -> Convert time string into real timestamp
    
    -> Log = 2026-04-13 10:30:00 user=123 login failed
    
    filter {
         grok {
           match => {
             "message" => "%{TIMESTAMP_ISO8601:log_time} user=%{NUMBER:user} %{GREEDYDATA:msg}"
           }
           }

         date {
            match => ["log_time", "yyyy-MM-dd HH:mm:ss"]
            }
          }    
         
         
         -> Output  
                  {
                  "@timestamp": "2026-04-13T10:30:00",
                  "user": "123",
                  "msg": "login failed"
                     }

----------------------------------------------------------------------------------------------------------------

4. Json Filter 

    -> Use it when logs are already in json 
    
    -> Input = {"user":101,"action":"signup","status":"fail"}
    
    
    filter {
        json {
         source => "message"
         target => "parser"    -> now logs to parsed  , without logs go to root
           }
          }                
                 
"""