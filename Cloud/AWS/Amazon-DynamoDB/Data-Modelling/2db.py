""" 

=> Access Pattern 

    -> The first pattern in data modeling is access pattern


    -> Access pattern 

       How our application read and write data 

       what question will application ask the database

    -> Get user profile 

    -> Get all order of a user 

    -> get latest post 

    -> find product by id 

    -> get comments of a post 

   Each of these is access pattern

=> DynamoDB is different 

   -> We must design the table around the queries we already know 


   Application -> What data do I need -> Access Pattern -> Design partition key -> Design sort key  -> Create table

   Table is come after access pattern


=> Example 

   1. Suppose we are building instagram

   2. Entities 

      Users 
      Post 
      Comments
      Like 
      Followers


   3. Access pattern 

     1. get user profile 

        Show profile of user101

        access pattern Get user by UserId 

        key design

        PK = USER#101

        SK = PROFILE

    2. Get ALL post of user 

       Show all post created by user101

       PK 

       SK = POST

    3. Latest post

       -> Show latest post 

       -> Design sort key

               POST#2026-07-01

               POST#2026-07-02

               POST#2026-07-03      

    4. Get comments 

       Show comments of user 101

       -> Store 

          PK = Post#100

          Sk = Comment#1

          PK = Post#100 

          SK = Comment#2

    5. Get orders 

       Show all order of customer 

       PK = Customer#10

       SK = Order#100

       PK = Customer#10 

       SK = Order#101                        


"""