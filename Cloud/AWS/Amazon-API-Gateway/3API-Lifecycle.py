""" 

=> API Gateway Lifecycle 

                      Client
                        │
                        ▼
                 1. DNS Resolution
                        │
                        ▼
                2. TLS Handshake
                        │
                        ▼
             3. API Gateway Listener
                        │
                        ▼
             4. API & Stage Resolution
                        │
                        ▼
              5. Route Matching
                        │
                        ▼
              6. Authentication & Authorization
                        │
                        ▼
             7. Request Validation
                        │
                        ▼
             8. Throttling & Quotas Check
                        │
                        ▼
             9. Request Transformation
                        │
                        ▼
             10. Integration Invocation
                        │
                        ▼
              Backend Service
                        │
                        ▼
           11. Backend Response
                        │
                        ▼
           12. Response Transformation
                        │
                        ▼
             13. Logging & Metrics
                        │
                        ▼
                Client Response


                
=> Step 1 DNS Resolution

    -> Client calls   https://api.example.com

    -> DNS resolve the domain

       api.example.com -> Regional endpoint / nearest edge location

=> Step 3 TLS handshake     

   -> API-Gateway accpet

      HTTPS

    It perform

      1. TLS negotiation 
      2. Ceritificate verification 
      3. Encryption setup

    -> After TLS succeed 

         Encrypted HTTP request

         enters api gateway

=> Step 3 Listener Accept Request

   -> Listener 

      1. Aceept TCP connection

      2. parse HTTP request 

      3. extract


         -> Path , headers , authorization , content-type

=> Step 4 API & Stage Resolution     

   -> API Gateway determine

       which api

       which stage


       https://api.example.com/prod/orders

       configuration is loaded from control plance


=> Step5  Route matching

   -> Gateway find the configured route

   Post / orders  -> matched route -> Integration -> order lambda


=> Step 6 Authentication

   -> Now identity is verified

   -> depending on configuration

   -> Possible methods

       1. IAM signature 
       2. JWT 
       3. Amazon authorizer

=> Step 7 Authorization

   -> What are you allowed to do


      user -> allowed post / orders

      but delete order -> forbidden 


=> Step 8 Request validation

   -> suppose schema validation

      {
      
      "item" : "Laptop",
      "quantity": 1

      }

      client send ->  {
                          "abc" : 10
                        }

      validation fails

      client immediately receive , 400 bad request


=> Step 9 Throttling and Quotas

   -> gateway checks request limit

      allowed = 100 req/sec

      current = 150 req/sec

      result -> 429 too many request


=> Step 10  Request Transformation

   -> API Gateway prepares the backend request 

   -> it may 

       1. Map headers 
       2. Rename fields 
       3. Add context value

       4. convert payload format


=> Step 11 Integration Invocation

   -> Now API Gateway invokes the backend

   -> Possible integration

       1. lambda
       2. HTTp service 
       3. EC2 , ECS, EKS

=> Step 12 backend Processing

   -> Business logic executes

       insert order -> calculate tax -> save db -> return json


=> Step 13 Request Transformation

   -> API gateway may modify the backend request

=> Step 14 Logging and Metrics 
   
     -> Request count 

     -> Latency 

     -> integration latency 

     -> 4xx errors 

     -> 5xx errors


=> Step 15   Response sent

   {
   
          HTTP/1.1 201 Created

          {
   "orderId":12345,
   "status":"Created"
             }
   
   }


"""