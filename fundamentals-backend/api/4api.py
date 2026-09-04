""" 

=> What is Resource 

   -> A resource is any object data or entity that your application manage

   -> An e-commerce application has

       User 
       Product
       Order 
       Cart 
       Category 
       Payment 
       Review

       Each of these is a resources

    -> Every resource has an identifier

        every resource has a unique identifier

        User 
      -----------

      ID : 101
      Name : Parveen

      REST identifies it using A URL

       /users/101

     -> Resource Naming

         URLs , should represent resources , not actions

         /users
         /products
         /orders
         /payment

       then use HTTP methods

       GET     /users
       POST    /users      
       PUT     /users
       DELETE  /users

       URLs does not change , only the HTTP method change


      -> Naming Rules

         1. Use nouns (plural nouns)

            /users
            /books
            /orders

         2. Use lowercase

            /products
            /orders

         3. Use hyphens 

            /user-profiles 

            /orders-items

      -> Nested Resources 

         Sometime one resources belongs to another

         -> an order has items 

           /oders/100/items

         -> a post has comments

            /post/25/comments

         -> user has address

            user/15/address


       -> Real example

          1. Resource

              User
              Post
              Comments
              Likes
              Stories

          2. Endpoints

            GET    /users/15
            GET    /posts
            POST   /post                         
            GET    /post/20/comments
            POST   /post/20/comments
            DELETE /comments/55



"""