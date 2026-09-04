""" 

=> REST Constraint 

   -> Rest was introduced by Roy Fielding in his PDH (2000)

   -> A system is considered RESTful only if it follow all REST Constraints

   -> There are six constraint



1. Client - Server Architecture

    -> Client and Server should have separate responsibilities

       Client -> HTTP request -> server

       Client Responsibilities 

         1. UI
         2. User interaction 
         3. Sending request 
         4. Displaying responses


       Server responsibilities 

         1. Busniess logic 
         2. Database 
         3. Authentication 
         4. validation 
         5. Processing

     -> Pros 

        1. if tommorrow React change to flutter , nthng changes in backend 
        2. Database change , frontend dont care

        3. called loose coupling

2. Stateless

    -> Every request contains all the information needed to process it

        server does not remember previous request 


3. Cacheable

    -> Every response should specify , can it be cached

        can it be cached 

          or 

          should it always be fetched

    -> example 

       GET/logo.png

       does logo change every second

       No

       Browser cache it , next request no network call


3. Uniform Interface

   -> Every REST API should look and behave consistently , Regardless of application

   -> uniform interface has 4 principle


   A. Resource Indentification

      -> Resource should have unique URIs

         GET/users

         GET/users/10
         GET/orders/22

   B. Manipulation Through Representation

      -> client receive a representation (such as JSON) of a resources and use it to create or update 
         resources

      -> Example

          GET/user/10

          {
          
             "id": 10,
             "name": "Parveen
          }         

          client can change it 

          {
          
          "name" : "john"
          
          }

    C. Self Descriptive Message

        -> Every Request and response should contain enough information to be understood 
           independently 


       -> Examples 

            Headers

               Content-type:
               application/josn

               Authorization:
               Bearer JWT

               Accept:
               application/json

               Status 
               200 OK

           Everything required to interpret the message is included

   D. HyperMedia as the Engine of Application State

       -> The response tells the client what actions are available next 

   E. Layered System

      -> The client should not know whether it is talking directly to the application server 

         or through intermediate

         Client -> API Gateway -> Load Balancer -> Authentication Service -> Application server 

         -> cache -> database

   F. Code on Demand

      -> The server can send executable code to the client

      -> A web page send javascript to the browser                                                 

"""