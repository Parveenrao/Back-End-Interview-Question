""" 

=> Data Modelling 

    -> Data modelling is the process of deciding 

       1. What data to store 

       2. How to partition it 

       3. How to query it efficiently 

       4. Which indexes are needed 

       5. How items are related to each other

    -> Goal is 

        One Request  = One query

    -> dynamo Db does not support joins


=> SQL Vs DyanmoDB Modeling 


    SQL                                               DynamoDB

    -> Design table first                              -> Design query first 

    -> Normalize                                       -> Denormalize 

    -> Joins                                           -> No joins 

    -> Multiple table                                  -> Often one table 
                                               
    -> Query anything                                  -> query only planned pattern


=> SQL 

    User 

      UserID 
      Name 

    Orders 
      OrderId 
      UserId 
      Price

    To fetch User + order 

    select * from users join orders  on user.userid = orders.orderid

=> DynamoDB

    Pk = User#101
    SK = Profile

    Name = Parveen

    -------------------------------

    PK = User#101
    SK = Order#101

    price = 700


    Now one query return everything


=> DynamoDB Data Modeling Process

   
    Step 1  Identify entities ->  Step 2 Identify access pattern -> Step 3 Choose partition key 

    Step 4 Choose sort key ->   Step 5 Design Item collection -> Step 6 Need GSI 

    Step 7 -> Need LSI  , Step 8 -> Denormalize -> Done



=> Step 1 Identify Entities 


    1. Suppose building instagram 

    2. Entites are 

       1. Post 
       2. Comment 
       3. Like 
       4. Follow

    3. Each become an item 


=> Step 2 Identify access pattern

    -> What queries will the application perform

    -> Get user profile 

    -> Get all post of user 

    -> get post by id 

    -> get comment of a post 

    -> get latest post 

    -> get followers

    -> get following 

    -> get likes


    Every access pattern should ideally be satisfied with a query operation rather than a Scan

=> Step 3 CHoose Partition key 

    -> Partition key decide 

       1. Data replacement 

       2. Scalability 

       3. throughput

=> Step 4 Choose sort key 

    -> Sort key organizes data inside partition

    -> sort key enables 

       1. Range queries 

       2. prefix query 

       3. sorting 

       4. versioning 


=> Step 5 Item collection 

   -> Everything sharing same Pk is an item collection


=> Step 6 Composite keys


=> Step 7 Denormalization 

   -> DynamoDB is user duplicate


=> Step 8 Secondary Index 

   -> Need another  access pattern 


=> Step 9  Handle Many - to many Relationship   


"""