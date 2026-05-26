""" 
4. Drop Filter 
    
    -> Completely remove an event (log) from pipeline
        
        if condition match , log is deleted
        
    
    filter {
        
        if "debug" in [message] {
            
            drop{}
        }
    }   
    
    
    -> keep only error level 
        
        if [level] != "error" {
            drop{}
        }
    
    -> Remove health check
    
    if "healthcheck" in [message] {
          drop { }
       }    


-----------------------------------------------------------------------------------------------------------

=> correct order

           
           filter {
  # 1. Parse
  grok {
    match => {
      "message" => "%{TIMESTAMP_ISO8601:log_time} %{WORD:level} user=%{NUMBER:user} %{GREEDYDATA:msg}"
    }
  }

  # 2. Clean / Convert
  mutate {
    convert => { "user" => "integer" }
    uppercase => ["level"]
  }

  # 3. Timestamp
  date {
    match => ["log_time", "yyyy-MM-dd HH:mm:ss"]
  }

  # 4. Logic
  if [level] == "ERROR" {
    mutate {
      add_field => { "alert" => "true" }
    }
  }

  # 5. Drop unwanted
  if [level] != "ERROR" {
    drop { }
  }
}       

"""