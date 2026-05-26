""" 
=> Histogram 
     
     -> A histogram store distribution of values
     
     -> How many request fall into different time ranges

----------------------------------------------------------------------------------------

=> Example 
    
    -> Let suppose our api request respone time are 
       
       0.05s , 0.04s , 0.01s, 1.2s , 0.1s
       
       histogram group them into bucket 
       
       bucket (less than or equal)  
       
       0.1s = 2 
       0.5s = 4
          
    -> Histogram store   
       
       1. Bucket
       2. count 
       3. sum      

"""
from fastapi import FastAPI
from prometheus_client import Histogram, generate_latest
from starlette.responses import Response
import time
import random

app = FastAPI()

# 🔥 Create Histogram
REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Request latency"
)

@app.get("/")
def home():
    with REQUEST_LATENCY.time():   # ⏱️ auto measure time
        time.sleep(random.uniform(0.1, 1))  # simulate delay
        return {"msg": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
