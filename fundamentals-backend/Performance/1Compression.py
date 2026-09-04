""" 


=> Compression 

    -> Compression convert a large response into a smaller one before sending it to the client


    -> without compression

      Server (JSON 500Kb) -> Internet -> client


    -> with compression 

       Server -> compression(json) (80kb) -> internet -> client (decompress automatically)

    -> less data travel over the network, API become faster


=> How compression work

    1. Client request compression response 

         GET/user/ HTTP1.1
         host api.example.com
         Accept-encoding : gip , br

    2. Server compression response

        -> server sends 

            HTTP/1.1 200 ok
            Content-encoding : gzip
            binary compressed data 


   3. Client automatically decompresses

      -> Browser / Postman/ python application decompress it automatically 


=> Important HTTP headers 

    1. Accept-Encoding 

       -> sent by client 

         Accept-Encoding : gzip , br , defalte 

       -> means , i support these compression algorithms

   2. Content Encoding

      -> sent by server 

         Content-Encoding : gzip 

      -> i compress this response using gzip


 => from fastapi import FastAPI
    from fastapi.middleware.gzip import GZipMiddleware

    app = FastAPI()

    app.add_middleware(
         GZipMiddleware,
         minimum_size=1000  # Compress responses >= 1000 bytes
        )

=> 1. What is compression in APIs?

      -> Compression reduces the size of the response before sending it over the network, 
         improving response time and reducing bandwidth usage.                      
 
=> Where is compression implemented?

     Reverse proxy (Nginx, Envoy)
     API Gateway
     Web server
     Application middleware (e.g., FastAPI GZipMiddleware)

     
=> Does compression reduce server CPU usage?

    -> No. Compression increases CPU usage because the server must compress the response.
        It reduces network bandwidth, so there's a trade-off.     


=> How does the server know whether to compress a response?
 
    -> The server checks the Accept-Encoding header. If it supports one of the advertised 
       algorithms (e.g., gzip), it compresses the response and sets Content-Encoding.        
"""