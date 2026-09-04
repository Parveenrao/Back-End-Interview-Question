""" 

=> AWS Lambda Environment Variable

   -> Env variable are key-value pair that AWS lambda provide to our function at runtime

   -> they allow you to configure our application without changing the source code 

   -> Environment Variables = Configuration values that are injected into your Lambda 
                               execution environment before your code starts running.


=> Why do we need Env Variables 

    -> Suppose your code connect to db

    -> if we deploy the same code to development  , testing and production we would need to edit 
        and redeploy the code each time


    -> Instead use env variables

        Development 


        DB_HOST = dev-db.example.com


        Production

        DB_HOST = prod-db.example.com    


     same code work in every environment



=> How They work 


                        Invocation

                           ↓

                 Create Execution Environment

                           ↓

                      Load Runtime

                           ↓

               Inject Environment Variables

                          ↓

                 Run Initialization Code

                          ↓

                   Execute Handler

=> Where are they stored

    -> Environment variables are managed by the Lambda control plane
"""