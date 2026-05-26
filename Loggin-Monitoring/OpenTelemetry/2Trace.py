""" 
=> Manul Tracing 

"""

from opentelemetry import trace
from fastapi import FastAPI
import time

tracer = trace.get_tracer(__name__)    # create span 



app = FastAPI()


@app.get("/")
def home():
    return {"msg" : "ok"}


@app.get("/process")
def process():
    with tracer.start_as_current_span("process-request"):
        time.sleep(1)  # simulate work
        return {"msg": "processed"}

# add multiple span 

@app.get("/span")
def span():
    with tracer.start_as_current_span("process_request"):
        
        with tracer.start_as_current_span("step-1"):
            time.sleep(0.5)
            
        with tracer.start_as_current_span("step-2") as span:
            span.set_attribute("User_id" , 123)
            span.set_attribute("operation" , "payment")
            time.sleep(1)
        
        with tracer.start_as_current_span("step-3") as span: 
            try:
                raise ValueError("Payment failed")
            
            except Exception as e:
                span.record_exception(e) 
                span.set_status(trace.Status(trace.StatusCode.ERROR))   
        
        return {"msg" : "processed"}    
    
                   