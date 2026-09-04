""" 


=> HTTP Methods 


    -> An HTTP method tells the server what action the client want to perform on a resource


    1. GET

       -> Used To Retrieve data

            GET/users

            get one users 

            GET/users/10

       -> characteristics


           1. Read data
           2. Does not modify data 
           3. safe 
           4. idempotent
           5. can be cached

    2. POST


       -> Create a new resources

       -> characteristics 

          1. Creates new data 
          2. Not idempotent 
          3. change server state 

   3. PUT

     -> Replace an entire resources

     -> entire representation is replaced 

     -> replace everything


   4. PATCH 

     -> Update only specific fields

     -> modify only what is provided


   5. DELETE

      -> Remove a resource


   6. HEAD

     -> SAME as GET , but returns only headers

         HEAD/file.pdf 

         content-lenght 1250000
         content-type : application/json

     -> usefull when checking metadata  without downloading the contetn


   7. OPTIONS

      -> What options are allowed

         OPtions/users

   8. TRACE

     -> used for debugging

   9. CONNECT

      -> Used to establish a tunnel commonly through a HTTP proxy                                        




"""