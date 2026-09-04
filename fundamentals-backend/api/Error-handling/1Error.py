""" 


=> Error Handling 

    -> Error handling is the process of detecting errors and returing proper HTTP responses instead
       of crashing the response


    -> Instead of 

        500 Internal server error


    -> Return 

           {
             "error" : {
              
               "code" : "USER NOT FOUND",
               "message" : "User with id 10 does not exist"}
           }

        

"""