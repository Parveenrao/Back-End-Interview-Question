""" 
=> Context 
    -> Context propagation works only in simple flow 
    
    -> context follows across 
        
        1. async work
        2. thread 
        3. services

---------------------------------------------------------------------------------

1. aysnc/thread/background_jobs
    
    -> context get lost
    -> trace break , span id disconnected

2. Messaging QUeue kafka , RabbitMq
     
     -> context does not automatically go to kafka 
     
     worker start a new trace    

3. Delayed jobs 
   
   -> celery , cron jobs

4. Custome instrumentation 
    
    -> If span is wrong  , attach to wrong parent                  
"""

from fastapi import FastAPI
from opentelemetry import trace

# setup tracer
trace.set_tracer_provider(trace.TracerProvider())
tracer = trace.get_tracer(__name__)

app = FastAPI()

@app.get("/")
def home():
    # parent span
    with tracer.start_as_current_span("request"):
        
        # child spans
        with tracer.start_as_current_span("validate"):
            pass

        with tracer.start_as_current_span("db"):
            pass

        return {"msg": "ok"}


import threading
from opentelemetry import context

def task(ctx):
    token = context.attach(ctx)   # restore context
    with tracer.start_as_current_span("thread-work"):
        print("running")
    context.detach(token)

@app.get("/thread")
def thread_api():
    ctx = context.get_current()   # capture context
    threading.Thread(target=task, args=(ctx,)).start()
    return {"msg": "done"}    