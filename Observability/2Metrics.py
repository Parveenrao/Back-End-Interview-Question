""" 
=> Guage Metric
    
    -> Can go up and down 
    -> Represt a current value 
  
  -> Example 
     
     CPU usuage = 70 -- 20 --80
     active users 
     memory usage  

"""

from prometheus_client import Gauge
from fastapi import FastAPI
import random

app = FastAPI()

REQUEST = Gauge("cpu_usage" , "CPU usage")

@app.get("/")
def home():
    REQUEST.set(random.random())
    return {"msg" , "ok"}

# with lables 

ACTIVE_USERS = Gauge(
    "active_users",
    "Active users",
    ["region"]
)

ACTIVE_USERS.labels(region="india").set(120)
ACTIVE_USERS.labels(region="us").set(80)