""" 

=> API Gateway Component

    1. API 

      -> An API is the top level container that holds all the configuration for your application

      -> Think of it as a project

         Example 

            Shopping API

        Inside it we might have

           /users
           /orders
           /payments
           /products

       -> An API contain

          1. Resource 
          2. Methods
          3. Integration 
          4. Stage 
          5. Deployments 
          6. Authorizers
          7. Models
          8. Usuage plans


    2. Resources

       -> A resource represent an path(URL) in our api

          /users
          /orders
          /products
          /payments

       -> resource from treee

          users
            |-> id , 
            |-> profile 

         orders 
            |-> orderid               

         products 


         Every resources represent an endpoint

    3. Methods 

        -> A method define what HTTP operation is allowed on a resouces

        -> common methods

            1. GET
            2. POST
            3. PUT
            4. Patch 
            5. Options 
            6. Head

        -> each method have 

           1. authentication 
           2. authorization 
           3. request validation 
           4. integration 
           5. throttling 
           6. caching

    4. Integrations

       -> An integration tells API gateway where to send the request after all check are complete


       -> Supported integration include

          1. AWS lambda 
          2. HTTP endpoint 
          3. Application load balancer 
          4. Other AWS service

    5. Deployment

       -> A deployment is a snapshot of your api configuration at a point in time

    6. Stages

       -> A stage is a named environment that points to a specific deployment

       -> Typical stage 

          1. dev 
          2. test 
          3. staging 
          4. prod



"""