""" 

=> API Types 

  
    1. Rest API

        -> Rest API is the original and most feature-rich API gateway offering

        -> it follows REST architectural principles using HTTP methods

        client -> REST API Gateway             -> Lambda / EC2 / ECS / HTTP backend

                     |-> Authentication
                     |-> Validation
                     |-> Transformation 
                     |-> Caching 
                     |-> Throttling

      -> Features 

         1. Resource and method-based routing 
         2. API keys 
         3. Usuage plans 
         4. Request validation 
         5. Request / response mapping technique 

         6. Stage variable 

         7. Caching 

         8. Canary deployments 

         9. Custom authorizes 

        10. IAM authorizes

        -> Uses

         1. Enterprises APIs

         2. banking system 

         3. E-commerce platforms

         4. Public APIs

         5. Legacy Rest services




=> Step 2 HTTP API

    -> HTTP API is a newer , lightweight version of API Gateway designed for modern application

    -> AWS built it to

        1. lower latency 
        2. lower cost 
        3. Simpler configuration

        client -> HTTP API -> JWT/IAM Auth -> Lambda/HTTP backend / ALB

     -> features 

         1. very low latency 

         2. lower price 

         3. JWT authorization 

         4. IAM authorization

         5. lambda integration 

         6. HTTP integration 

         7. CORS support 

         8. Custom domains


=> Websocket API

   -> Unlike REST and HTTP APIs which follow a request - resposne , websocket apis provide 

      persistent , bidirectional communication

   -> once connected , both the client and server  can send message at any time


   -> Lifecycle 

     client -> connect -> connected -> send message -> receive message -> disconnect

   -> Use case 

      1. Chat application 

      2. Multiplayer game 

      3. live dashboard 

      4. stock price update 

      5. IOt telemetry 

      6. live notification


       user A -> API Gateway -> User B     


"""