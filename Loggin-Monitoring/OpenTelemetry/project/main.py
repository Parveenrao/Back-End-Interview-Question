from fastapi import FastAPI
from tracer import setup_tracer
from opentelemetry import baggage, context
from opentelemetry.trace import Status, StatusCode

app = FastAPI()
tracer = setup_tracer()

@app.get("/process")
def process():
    
    # Root span 
    with tracer.start_as_current_span("process_request") as span:
        
        # baggage 
        ctx = baggage.set_baggage("user_id" , "123")
        token = context.attach(ctx)
        
        try:
            
              # validate 
              with tracer.start_as_current_span("validate") as s:
                  s.set_attribute("step" , "validation")
              
              with tracer.start_as_current_span("db-call") as s:
                s.set_attribute("db.system", "postgres")
                fake_db()
               

            # ---- External API ----
              with tracer.start_as_current_span("external-api") as s:
                s.set_attribute("api.name", "payment-service")
                fake_api()
        
        except Exception as e:
            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR))

        finally:
            context.detach(token)

        return {"status": "done"}


def fake_db():
    return "db ok"


def fake_api():
    # simulate error
    raise Exception("payment failed")            