""" 

=> Amazon-API-Gateway 

     -> Amazon API Gateway exist to provide a single , secure ,scalable entry point for clients 
        to access your backend services without exposing those service directly 


     -> Imagine we have multiple backend services

        1. user service 
        2. payment service 
        3. order service 
        4. notification service 
        5. inventory service

    -> without gateway


         Mobile app / webapp 
             |-> User service 
             |-> Order service 
             |-> payment service
             |-> inventory service

    -> Problems 

        1. Client must know every service URL
        2. Every service must implement authentication 

        3. Every service must implement rate limiting 

        4. Every service must implement logging 

        5. Every service handle cors separately 

        6. hard to change CORS separately

        7. Difficult version management


    -> With amazon API Gateway

                    Clients
                (Web/Mobile/API)

                     |
                     |
              -----------------------
              | Amazon API Gateway |
               -----------------------
                 |      |       |
                 |      |       |
              User  Order  Payment Lambda
             Service Service Service  etc   

        The client  talks only to API Gateway

        API Gateway forwards the request to the correct backend

=> WHy AWS built API Gateway

    -> Modern applications have many

    -> Example , An E-commerce application

      Customer -> Login -> User Service -> Place Order -> Order Service -> Pay -> Payment Service -> Track

      Tracking service -> Reviews -> Review Service

    -> Instead of exposing five different public endpoint , AWS recommends exposing only one 

         https://api.company.com


         API gateway internally routes 

            /login 
            /order 
            /review
            /tracking

=> Main Reason for API Gateway

    1. Single Entry Point

        -> Instead of 
         
        
            user.company.com

            payment.company.com

            order.company.com

        user access.com

        API Gateway routes request

    2. Security

       -> Without API Gateway

          -> Every service must implement

             1. Authentication
             2. Authorization 
             3. API keys 
             4. JWT validation

        -> With api gateway


          client -> API gateway -> auth / authorization /api keys /rate limit /loggin/-> backend

          security is centralized

    3. Protect Backend

       -> Never expose internal service

         internet -> api gateway -> private vpc -> ec2/lambda/containers

         attackers cannot reach directly to backend

    4. Request Routing

       1. Get user -> User service -> payment service -> Order service 

    5. Authentication

         API gateways support

           -> IAM 
           -> JWT 
           -> OAuth 
           -

    6. Rate limiting

       -> Suppose client send

          10000 request/sec

          lmabda become overhead

          gateway can limit , 100 req/sec

    7. Request validation

       -> Support the backend expects 

          {
          
           "name" : "Parveen",
           "age"  : 25
          }                                        

          
        -> Client sends

           {
              "xyz" : 5
           
           }

    8. Monitoring 

       -> Gateway automatically provides

          1. Request count 
          2. Errors 
          3. Latency 
          4. Integration latency

          5. 4XX response 

          6. 5XX response

          These metrics integrate with Amazon Clodudwatch       

"""