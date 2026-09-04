""" 

=> Amazon API-Gateway 

    1. Is a fully managed service from AWS that lets you create , publish , secure and monitor 
       and manage API at any scale

    2. It act as a front-door of our backend service


=> What API gateways does

    Client(web/mobile) 
          |-> aws lambda
          |-> ec2
          |-> ecs/eks
          |-> any http/https endpoint

    API gateway receives client request , authenticates and validates them , forward them 
    to backend and return the response


=> Features 

   1. Authenticate and Authorization

      -> IAM 
      -> JWT / OAuth 
      -> amazon congnito 
      -> lambda authorizes

   2. Rate limiting 

   3. api keys and usuage plans 

   4. request / response transformation 

   5. cors support 

   6. monitoring with cloudwatch 

   7. custom domain name

   8. API versioning 

   9. Request validation


 => Browser
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
     DynamoDB                RDS


=> Choose HTTP API

   -> Lower cost 

   -> lower latency 

   -> simple rest endpoints 

   -> jwt authentication


=> Choose RestAPI

   -> API keys 

   -> usuage plans 

   -> response caching 

   -> Advance request transformation 

   -> more granular api managment


=> Benefit

   -> No server managment 

   -> Automatic scaling 

   -> Pay only for request 

   -> Built in security 

   -> Tight integration with aws serives 

   -> easy monitoring and logging


=> if we are building , serverless architecuter , common architecture is 

    client -> api gateway -> lambda -> dynamodb


"""