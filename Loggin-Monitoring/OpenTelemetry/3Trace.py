""" 
=> Create a process , endpoint add 2-3 span with attribute and error


"""


from opentelemetry import trace
from opentelemetry.trace import Status , StatusCode
from fastapi import FastAPI
import time

app = FastAPI()

tracer = trace.get_tracer(__name__) 


@app.get("/process")
def process():
    
    with tracer.start_as_current_span("process_request"):
        
        # validate step 
        with tracer.start_as_current_span("validate") as span: 
            span.set_attribute("step" , "validation") 
            time.sleep(0.3)
        
        # DB call setup 
        
        with tracer.start_as_current_span("Db-call") as span:    
            span.set_attribute("db-systen" , "postgressql")
            time.sleep(0.5) 
        
         # ✅ Payment step (with error)
        with tracer.start_as_current_span("payment") as span:
            span.set_attribute("payment.method", "card")
            try:
                time.sleep(1)
                raise Exception("Payment failed ❌")
            except Exception as e:
                span.record_exception(e)
                span.set_status(Status(StatusCode.ERROR))

        return {"msg": "process completed"}        