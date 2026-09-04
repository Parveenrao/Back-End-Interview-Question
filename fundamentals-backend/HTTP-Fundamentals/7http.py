""" 

=> HTTP Status-Code

   -> HTTP status code are 3 digit numbers returned by the server to tell the client what 
      happened with the request 


   1. 1xx informational 

       -> I received request 

       Rarely used in REst API


   2. 2xx Success

     1. 200 OK
       -> Everything worked

           GET/user/1 

       -> used for 

          1. Get 
          2. put 
          3. patch 
          4. delete(sometime)

     2. 201 OK

        -> A new resource has been created

     2. 202 Accepted

        -> requested has been accepted , but processing has not finished yet 

        -> uploading huge video

        -> common in

            1. background job
            2. email sending
            3. video processing
            4. queue sysem 

     3. 204 NO content

        -> succes 

        -> but nthng returned

   3. 3xx Redirection

       -> Server says , The resource moved


       1. 301 Moved permanently

          old url , /old-blog

          New url , /new-blog 

       2. 302 found

          -> temporary redirect 

             used when something temporarily changes

       3. 304 Not modified

           -> browser ask 

              has this image changed

              server says , 304 not modified

   4. 4xx Client error

       -> Means , client made a mistake


       1. 400 Bad Request

           -> request form is valid

      2. 401 Unauthorized

          -> user is not authenticated

      3. 403 forbidden

          user is logged in , but doesnot have permission

          normal user tried to delete/admin/users

      4. 404 Not found 

          -> Resource does not exist 


      5. 405 Method Not allowed


         Endpoint , Get/users 

         but client send , post/users


      6. 409 Conflict

         -> conflict with current state


         -> email already exist 


      7. 410 Resource existed earlier 

          -> Now permanently deleted

     8. 415 Unsupported Media type 

       -> APi accept json

       -> client send content-type / application/xml

     9. 422 Unprocessable content

        -> request form is correct , but validation fails

             POST /users

               {
                "email":"wrong-email"
               }       ,

             json is valid , 

             but validation is failed

     10. 429 Too many request

         -> Rate limit exceed

   5. 5xx Server Error

       -> Client did everything right , but the server failed


       1. 500 Internal server error
    
          -> Unexpected server error

       2. 501 Not implemented

           -> Server does not support the requested functionallity


           -> client send method or feature the server does not implement



      3. 503 Bad gateway 

         -> occur when one server act as a server or proxy and gets an invalid response  from an upstream server 


         client -> api gateway -> backend service(return invalid response) -> gateway returns -> 502 bad gateway


      4. 503 Service Unavailable 

         -> Server is temporarily unavailable

      5. 504 

        -> Gateway did not receieve a response in time                                                                                                   



"""