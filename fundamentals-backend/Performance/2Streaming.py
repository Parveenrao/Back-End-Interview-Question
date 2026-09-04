""" 

=> Streaming in API Performance 

    -> Streaming is a technique where the server starts sending data immediately in small
       chunks instead of waiting to generate the entire resposne


=> Without Streaming 

   -> Suppose the server need 10 seconds to generate a large report


Client
   |
   | GET /report
   |
Server
   |
   | Generate report (10 sec)
   |-------------------------
   | Send complete response
   |
Client receives everything after 10 sec


-> The client waits 10 seconds before seeing any data 



=> With Streaming

   -> Server send data as soon as it is available 

   -> Server 

       Generate first part   -> chunk 1

       Generate second part  -> chunk 2
       
       Generate third part   -> chunk 3

       Client starts receiving immediately 

    The user start receiving immediately 

    The user sees much data sooner 

=> Why Streaming

   -> Lower latency 

   -> handle very large response 

   -> Avoid loading the entire response into server memory 

   -> Real-time updates 

   -> large file download


=> Use case 

    1. Video streaming 
    2. Audio streaming 
    3. Chatbot response 
    4. Live logs 
    5. Server sent events 
    6. Large csv export 
    7. large file download 


=> Normal API vs Streaming API

   1. Normal APIs

      Request -> Server -> Generate complete response 

      Return json 


   2. Streaming APIs

       Responses in sent in pieces 

       chunk1 , chunk2 , chunk3 

=>  

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

def generate_numbers():
    for i in range(5):
        yield f"{i}\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(
        generate_numbers(),
        media_type="text/plain"
    )          

    
=>  What is streaming in an API?

    ->  Streaming sends data to the client in chunks as it becomes available instead of waiting 
        for the complete response.    


=> Why is streaming faster?

      -> It reduces time to first byte (TTFB) because the client starts receiving data 
         immediately instead of waiting for the full response.        

=> Streaming is the process of sending an API response to the client 
   incrementally in chunks as data becomes available, rather than waiting for the 
  entire response to be generated first.         


"""