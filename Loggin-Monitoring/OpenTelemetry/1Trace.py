""" 
=> Tracing 
    -> Tracking a request journey across services
    
    -> Imagine 
       1. user hit API
       2. API call service A
       3. Service A call DB
       4. Service A call Service B
       
       User Request → API → Service A → DB → Service B
    
    -> It answer
        
        where did the request go 
        which part is slow
        where did it fail

---------------------------------------------------------------------------------------------------

=> Core Concepts 
    
    1. Trace 
       
       -> Full journey of request 
       -> Has Trace ID 
     
      one request  = one trace
    
    2. Span 
       
       -> A single step in journey
       -> Has span Id 
     
     API call       = span
     DB call        = span 
     External call  = span   
    
    3. Parent child Relationship 
                Trace
                 ├── Span (API)
                 ├── Span (DB)
                 └── Span (Service B) 
    
    4. Attribute (Metadata)
    
          -> Extra info 
              
              1.URL
              2.status code
              3.query time
    
    5. Events 
       Logs inside span 
       
       -> Db query started 
       -> Timeout occurred

----------------------------------------------------------------------------------------------------

=> Practical Flow (How it works)
      1. Request comes in
      2. Trace ID is created
      3. Spans are created for each operation
      4. Data sent to backend (like Jaeger)

             👉 Example backend: Jaeger                                           

"""
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Service name
resource = Resource(attributes={
    "service.name": "fastapi-service"
})

trace.set_tracer_provider(TracerProvider(resource=resource))

# OTLP exporter (Jaeger supports this)
otlp_exporter = OTLPSpanExporter(
    endpoint="http://localhost:4317",
    insecure=True
)

span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

@app.get("/")
def root():
    return {"message": "Tracing via OTLP"}