""" 

=> Amazon ApiGateway 

     -> Is a fully managed service from AWS that lets you create , publish , secure , monitor ,
        and manage API at any scale

     -> It acts as a front door for our backend service


=> What API Gateway does

    -> A typical request flow looks like this

                  Client (Web/Mobile)
                          |
                          v
                 Amazon API Gateway
                          |
                          +--> AWS Lambda
                          |
                          +--> EC2
                          |
                          +--> ECS/EKS
                          |
                          +--> Any HTTP/HTTPS endpoint

                          
    -> API Gateway receieve client requests, authenticate and validates them , forwards them 

       to your backend and return the response

    -> Key features 

        1. REST APIs -> Feature-rich APIs with authentication , caching , throttling ,and API keys

        2. HTTP APIs -> Lower latency and lower cost , ideal for modern REST services

        3. WebSocket APIs -> Real-time , bidirectional communication (chat , notification gaming)


    -> Features

       1. Authentication and authorization 

          -> IAM 
          -> JWT / OAuth 

          -> Amazon Congnito

          -> Lmabda authorizes

          -> Rate limiting and throttling 

          -> API keys and usuage plans 

          -> Request / Response transformation 

          -> CORS support 

          -> Monitoring with cloudwatch

          -> Custom domain names 

          -> API versioning 

          -> Request validation 

=>    Browser
       |
      HTTPS
       |
    API Gateway
       |
   +----------------------+
   |                      |
  Lambda A             Lambda B
  (User API)           Order API
   |                      |
  DynamoDB              RDS     


=> Choose HTTP API if you want

   1. Lower cost 
   2. Lower latency 
   3. Simple Rest Endpoint 
   4. JWT authentication 

=> Choose REST APi

   1. API keys 
   2. usuage plans 
   3. Response caching 
   4. Advance request transformation 
   5. More granular API managment

"""