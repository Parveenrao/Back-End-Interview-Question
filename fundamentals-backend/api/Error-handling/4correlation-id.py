""" 


=> Correlation ID

    -> Is a unique indentifier to attached to a request that allows you to trace that
       request across multiple services , logs and database and microservices


=> Why do we need correalations IDs


  Client
   |
   | POST /orders
   v
API Gateway
   |
   +------> User Service
   |
   +------> Order Service
   |
   +------> Payment Service
   |
   +------> Email Service


-> One request may go through 4-5 servies 

-> without a correlation IDs

     1. User service log
       
         Order created 

     2. Payment service log

         Payment service successfull

     3. Email service log 

         Email sent


    How do you know these logs belong to the same request 

-> With correlationID

    1. Suppose the client sends

        every service log it

    2 user service
 
         [12345] User validated


   3. Order service

       [1234-abcd]  order created

   4. Payment service 

       [123-abcd]  payment successfull

   5. Email service

       [1233-avdf] email sent


=> Where it is stored

   -> Usually in an HTTP header 

GET /users/10 HTTP/1.1

Host: api.example.com

X-Correlation-ID: 8c4d7a1e-9d7f-45d6-b96f-c2f56c12c001


X-Correlation-ID
Correlation-ID
X-Request-ID
Trace-ID (in distributed tracing systems)


=> from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid

app = FastAPI()


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        correlation_id = request.headers.get(
            "X-Correlation-ID",
            str(uuid.uuid4())
        )

        request.state.correlation_id = correlation_id

        response = await call_next(request)

        response.headers["X-Correlation-ID"] = correlation_id

        return response


app.add_middleware(CorrelationIdMiddleware)


"""