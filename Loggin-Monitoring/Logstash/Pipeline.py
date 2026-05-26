"""   

input {
  file {
    path => "/var/log/app.log"
    start_position => "beginning"
    sincedb_path => "/dev/null"
  }
}

filter {
  grok {
    match => {
      "message" => "%{TIMESTAMP_ISO8601:log_time} %{WORD:level} user=%{NUMBER:user} %{GREEDYDATA:msg}"
    }
  }

  mutate {
    convert => { "user" => "integer" }
    uppercase => ["level"]
  }

  date {
    match => ["log_time", "yyyy-MM-dd HH:mm:ss"]
  }

  if [level] != "ERROR" {
    drop { }
  }
}

output {
  stdout { codec => rubydebug }

  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "error-logs"
  }
}

"""