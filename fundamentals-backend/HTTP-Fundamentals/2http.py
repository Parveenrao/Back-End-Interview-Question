""" 

=> Anatomy of HTTP Request

    -> It has 4 main parts


       1. Request Line

           GET/user/10 HTTP/1.1

           GET -> http method 

           user/10 -> URI

           HTTP/1.1 -> HTTP version


      2. Headers 

          -> headers provide additional information 

               1. who is sending the request 

               2. What data format is expected 

               3. Is the user authenticated 

               4. Can the response be cached


      3. Body 

         -> Body contains the data sent to the user 


                   POST /users
                   Content-Type: application/json

                   {
                  "name": "Parveen",
                  "age": 22
                   }     





=> HTTP is stateless

   -> Request 1 GET/login

   -> Request 2 GET/login

   The server does not automatically remember that both request came from the same server 

   Each request must carry the information needed to process it , such as sessionID or JWT in headers




"""