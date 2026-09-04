""" 
=> IAM Role 

   -> An IAM Role is an AWS identity that does not belong to specific person

   -> Instead , it is assumed temporarily by:

       1. AWS services (EC2, Lambda, ECS)
       2. IAM user 
       3. Application 
       4. AWS account 
       5. Identity provider (Google , Azure )

     Unlike IAM user , A Role has no username and password 

=> Why do we need IAM Role 

   -> Imagine you launch an EC3 instance 

   -> Inside the server , python application uploads images to s3

       AWS ask how do i know application is allowed to access S3

       1. Method 1
         
          -> Store credentials inside your server 

          -> Application need them 

          -> if someone hacks your EC2 instance , they steal Access key , Secret key 

       2. Method 2

          -> Create an IAM Role 

            EC2 -> IAM Role -> S3 permission

            Now. no access keys ,no secret keys , AWS automatically provide temporary credentials

=> Temporary Credentials 

    1. When an EC3 instance assume an IAM Role , AWS generate credentials like

       -> Access key 
       -> Secret key 
       -> Session token

    2. IAM user have only -> Access key , Secret key 

    2. Roles have -> Access key ,Secret key , Session Token 

        -> Session token make the credentials temporary

        -> After some time , credentials expire

        -> AWS automatically referesh them 

        -> We do not have to manage them

=> Trust Policy     

    -> Every IAM user have two type of policies 

       1. Trust policy 
       2. Permission policy


    1. Trust Policy 

       -> Who is allowed to assume this role 

    2. Permission Policy 

       -> Once EC2 assumed this role , what can it do

=> Cross Account Access

    1. Imagine two AWS account

      Company A , Company B

      Company A wants to read and S3 bucket in Company B

      Instead if sharing password 

      Company B creates a Role

=> Real world Architecture



                    Internet
                        │
                  Application Users
                        │
                    Load Balancer
                        │
                    EC2 Instance
                        │
                 IAM Role Attached
                        │
        ┌───────────────┼───────────────┐
        │               │               │
       S3             DynamoDB      CloudWatch


"""