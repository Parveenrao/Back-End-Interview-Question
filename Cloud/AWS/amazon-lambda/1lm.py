""" 

=> AWS Lambda 

    -> Is a serverless computing service provided by amazon web services that lets you run 
       code without provisioning or managing server

    -> Instead of running an application on a dedicated server , you write a function , upload it to
        Lmabda and AWS execute it whenever it's triggered


    -> How it works 

        1. You write a function (Python , Node , C++ , Go and other supported language)

        2. You configure a trigger , such as 

              -> An HTTP request via API Gateway
              -> A file uploaded to an S3 bucket 
              -> A database updated 
              -> A scheduled event 

        3. AWS automatically 

             1. Start the execution environment 
             2. Runs your code
             3. Scales up or down based on demand 
             4. Charge only for the compute time used 


        4. Example

            1. Imagine we have an online-photo-sharing app

            2. when a user upload an image to s3

                1. The upload trigger a lambda function 
                2. lambda function resize the image 
                3. The resize image is stored in another bucket 

            3. No server need to be running continuously 

=> Benefit 

    1. No server management -> AWS handle infrastructure , patching , and scaling 

    2. Automatic scaling  -> can handle one request or thousand simultaneously 

    3. Pay-per-use -> You pay only for the number of request and the execution time

    4. Event-driven -> Runs only when an event occur


=> Common Use Case 

   1. Building REST APIs
   2. Processing uploaded files 
   3. Automating backups 
   4. Sending notifications 
   5. Running scheduled jobs (cron jobs)
   6. Processing data streams 
   7. backend logic for mobile and web application


"""