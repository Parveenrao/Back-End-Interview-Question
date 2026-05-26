from opentelemetry import trace                      # create trace , create span 
from opentelemetry.sdk.trace import TracerProvider   # manage how trace is created and behave 
from opentelemetry.sdk.trace.export import BatchSpanProcessor # sending span into bactaches instead of one by one , better peformance
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter # send data to tele collector , jaeger via collector
from opentelemetry.sdk.resources import Resource

resource = Resource.create({
    "service.name": "fastapi-service"   # 👈 IMPORTANT
})
 
def setup_tracer():
    provider = TracerProvider(resource=resource)

    exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

    processor = BatchSpanProcessor(exporter)   # how span are handled  , where they go
    provider.add_span_processor(processor)     # when span is created , send it using to processor

    trace.set_tracer_provider(provider)

    return trace.get_tracer(__name__)