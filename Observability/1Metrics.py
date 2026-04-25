"""  
=> Metric
    
    -> A number over time 
        http_requests_total{method="GET", status="200"} = 1200
     

--------------------------------------------------------------------------------------------------------

1. Counter Metric
    
    -> Only increase 1,2,3........
    -> Never decrease 
    -> Reset only when app restarts
    
  ex , Total login , Total Request , Total errors
  
  
  -> Rules 
      
      1. NEver use raw counter value in queries , http_total_request 
      
          -> use rate(http_total_request[5m])   request per second in last 5 min 
          


"""

from prometheus_client import Counter
from fastapi import FastAPI

REQUEST = Counter("http_request_total" , "Total request")

app = FastAPI()

@app.get("/")
def home():
    REQUEST.inc()            # increment by 1
    return {"msg" : "Okay"}

# add label 

REQUESTS = Counter(
    "http_requests_total",
    "Total requests",
    ["method", "endpoint"]
)

@app.get("/")
def home():
    REQUESTS.labels(method="GET", endpoint="/").inc()
    return {"msg": "ok"}