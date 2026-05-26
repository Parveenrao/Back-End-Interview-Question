"""  
=> Context Propagation 
   
   -> Passing information across services 
   
   -> Context propagation is the mechanism by which trace state (trace_id, span_id, baggage) is 
      carried across process boundaries so that a distributed system behaves like a single trace.
   
   -> Why it is exist 
       
       Let suppose we have three services 
       
       Client --> Service A --> Service B --> Service C 
       
     -> without Propagation 
        
        1. Each service creates its own trace 
        2. You see threee separate trace
        3  Debugging  = nightmare
     
     -> With propagation 
        
        1. All service share same trace_id 
        2. Each creates child span
        3. will see one compelet trace


--------------------------------------------------------------------------------

=> Core Component 
    
    1. Trace Context 
        
        trace_id -> identiy whole request
        span_id -> identify current operation
        parent_span_id -> links hierarchy
    
    2. Baggage 
        
        -> Key-value pairs 
           
           user_id = 123 
           plan = premium
         
--------------------------------------------------------------------------------

=> How context travel  
    
    1. Http headers 
    2. gRPC metadata
    3. kafka message headers 

---------------------------------------------------------------------------------

=> Types of Propagation 
   
   1. W3C Trace Context
      -> standard 
      -> used everywhere
      -> work across languages
      
   2. B3 Propagation 
       
       -> used by zipkin 
       -> legacy , but still common
   
   3. Jaegar propagation 
       
       -> Custom format
 
 
 -> Always use W3C
------------------------------------------------------------------------------------

=> Context Flow 
     
     1. Incoming Request Service A
          No headers  -> new trace created 
          context initlization 
     
     2. Service A -> Service B 
        
        Before calling B 
        inject into headers 
     
     3. Service B Recieve Request
          extract context
          
     4. Create child span
            
                                                         
"""

from fastapi import FastAPI, Request
from opentelemetry import trace
from opentelemetry.propagate import extract

app = FastAPI()
tracer = trace.get_tracer(__name__)

@app.get("/process")
async def process(request: Request):
    # Extract context from incoming headers
    ctx = extract(request.headers)

    with tracer.start_as_current_span("service-b-span", context=ctx):
        return {"message": "Processed by Service B"}
    

from fastapi import FastAPI
import requests

from opentelemetry import trace
from opentelemetry.propagate import inject

app = FastAPI()
tracer = trace.get_tracer(__name__)

@app.get("/start")
async def start():
    with tracer.start_as_current_span("service-a-span"):
        headers = {}
        
        # Inject context into headers
        inject(headers)

        response = requests.get(
            "http://localhost:8001/process",
            headers=headers
        )

        return response.json()    