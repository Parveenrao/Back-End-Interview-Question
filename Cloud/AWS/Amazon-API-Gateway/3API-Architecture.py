""" 

=> High Level Architecture

                 Clients
          (Web, Mobile, CLI, IoT)
                     |
                     |
              DNS Resolution
                     |
                     |
             +----------------+
             | API Gateway    |
             | Edge Endpoint  |
             +----------------+
                     |
        +------------+-------------+
        |            |             |
 Authentication  Request       Throttling
 & Authorization Validation    & Quotas
        |            |             |
        +------------+-------------+
                     |
              Route Resolution
                     |
             Integration Engine
                     |
      +--------------+---------------+
      |              |               |
   Lambda         HTTP API       AWS Service
      |              |               |
   Business Logic / Backend Services
                     |
              Response Pipeline
                     |
              Transformation
                     |
                  Client


=> Client Layers

    -> Client can be 

       1. Web applications 
       2. Mobile apps 
       3. Iot devices 

       4. Other backend services

       5. CLI tools

=> DNS Layer

   -> When the client calls

        https://api.example.com

     DNS resolve it to an API Gateway endpoint

    -> for edge optimized API

       client -> DNS -> Nearest Edge locatipon

    -> for regional API

       Client -> Regional API Gateway Endpoint


=> Request Listener 

   -> Listener accept

      1. HTTPS connection

      2. HTTP/2 (where supported)

      3. TLS termination

      internet -> HTTPS Request -> API Gateway Listener

    -> Responsibility 

       1. Accept TLS connections 
       2. Perform TLS handshake 
       3. Read HTTP request 

       4. Pass request internally

=> Step 4 Authentication Layer

     -> Before routing , API gateway check identity

     -> Supported method include

        1. IAM authorization 
        2. JWT tokens 
        3. Lambda authorizers 

        4. API keys

=> Step 5 Request Validation

    -> API gateway validate

        1. Headers

             content-type
             authorization

        2. query parameters

            ?page = 1

        3. Path parameters

           /users/{id}

        4. Request body

           {
             "name" : John,
             "age" : 25
           }

           if required fields are missing , 400 Bad Request

=> Step 6 Throttling Layer

    -> This protect backend service

    -> prevent a single client from overwhelming backend

=> Step 7 Routing Engine

    -> The routing engine decide where the request goes


      incoming request -> Route matcher -> Users / orders


=> Step 8 Integration Engine

   -> This component invokes the backend

   -> Supported integrations include:

      1. AWS lambda 
      2. HTTP endpoint 
      3. Amazon EC2
      4. Amazon ECS
      5. Amazon EKS

      6. Other AWS services

=> Step 9 Backend

    -> This is where business logic runs

      API Gateway -> Lambda -> Python code -> Database

      API Gateway does not care what language the backend use


=> Step 10 Response Pipeline

   -> backend returns

      {
      
      "message" : "Success"
      
      }      


=> Step 11 Monitoring

   -> API Gateway publish metrics such as

      1. Total request 
      2. Latency 

      3. Integation latency 

      4. 4xx errors 

      5. 5xx errors

      6. cache hit/miss

      These integration with Amazon CloudWatch for dashboard and alarms



"""