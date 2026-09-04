""" 

=> Last-Modified 

   -> Another HTTp caching used for cache revalidation

   -> instead of sending a unique version indentifier like Etag , the server send the date and
      time when the resource was last changed 


=> What is Last Modified 

   GET/products 

   Server responsd  


          HTTP/1.1 200 OK

              Last-Modified: Sat, 18 Jul 2026 10:30:00 GMT

               [
                  {
                        "id": 1,
                        "name": "Laptop"
                       }
               ]

      This tell browser , resources was last updated on xxx-yy-zzz


      browser store 

       1. response body 
       2. Last-modified timestamp

Client
   |
   |---- GET /products -------------------->
   |
Server
   |
   | 200 OK
   | Cache-Control: max-age=60
   | ETag: "abc123"
   | Last-Modified: Sat, 18 Jul 2026 10:30 GMT
   |
Client caches response
   |
   | (within 60 seconds)
   | Uses local cache
   |
60 seconds later
   |
   |---- GET /products
   |     If-None-Match: "abc123"
   |     If-Modified-Since: Sat, 18 Jul 2026 10:30 GMT
   |
Server
   |
   |-- If unchanged --> 304 Not Modified
   |
   |-- If changed ----> 200 OK + new body + new ETag + new Last-Modified       





"""