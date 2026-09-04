""" 

=> Breaking Changes 

    -> A breaking change is any modification to an API that cause existing client to 
       stop working or behave incorrectly without changin their code 

    -> If an old client that worked with API v1 fails after upgrading the server to
       v2 , the change is a breaking change 


=> Real Life example

    1. Suppose a shopping apps calls 

        GET/products/101

        old response 

            {
            
            "id" : 101,
            "name" : "Laptop",
            "price" : 5000
            
            
            
            }   

    2. Now the backend change the response

         {
         
         "id" : 101,
         "name" : "Laptop",
         "amount" : 5000
         
         
         }             


       console.log(product.price)

       output -> undefined 


       The app may crash or display incorrect data 


       This breaking

=> Types of Breaking Change 

   1. Renaming Fields

      {"name" : "Parveen"}

      to 

      {"full_name" : "Parveen"}

   2. Removing fields 

      1. old 

         {
           "email" : "abc@gmail.com"
         }   

      2. New {}


      3. Fails because the field no longer exist 


   3. Chaning data type 

      Old:

             {"age" : 25}

     New

            {"age" : "25"}

   4. Changing endpoint url

      1. Old -> GET/users

      2. New -> GET/customers


   5. Changing HTTP method

       1. Old -> GET/users/1

       2. New -> POST/users/2

   6. Changing Request Request Body 

   7. Changing Query Parameters

   8. Changing Response Structure 


   9. Tightening Validation Rules

      1. Old API accepted

         {"username" : "john"} 


          New API requires

            Minimum 10 characters 
            Special character 
            Number 

        Old request now fail

    10. Chaning status code 


    11. Changing Authentication

    12.Removing an Endpoint                                        


"""