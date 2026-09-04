""" 

=> IAM (Identity And Access Mangement)

    -> Almost every Aws services use IAM for authentication and authorization 


=> What is IAM 

   -> IAM is the AWS services that lets you control 

      1. Who can access your AWS account 
      2. What they can access 
      3. What action they perform 
      4. Under what condition they can perform action

    -> Think of IAM as the security guard of your AWS account 

    -> Example 

       Suppose a company has 

       1. 50 developers 
       2. 20 Devops Engineers
       3. 10 Data scientist 
       4. 5 Managers 

       Not everyone should have access to everything 

       Developer     -> EC2 , Cloudwatch 
       Devops        -> EC2 , VPC , IAM
       DataScientist -> S3, SageMaker 
       Manager       -> Billing Dashboard 

       IAM control these permission

       
=> Why Do we Need IAM   


    -> Imagine there were no IAM 

       1. Everyone would log in using AWS Root Account 

       2. Anyone could delete EC2 instance 

       3. Anyone could delete S3 buckets 

       4. Anyone could create expensive resouces 

       5. Any could remove database 

       6. No accountability for who made changes 

     This follows the Principle of Least Privilege , give user only the permission required to do
     their nothing more


=> Authentication 


   -> Who are you 

     1. Username 
     2. Password 
     3. MFA 
     4. Access Key 
     5. SSH key 

    Aws verify user identity 

    You are authenticated 


=> Authorization 

    -> What are you allowed to do , after logging

       1. Launch EC2 instance 
       2. Delete S3 buckets 
       3. Create IAM users 
       4. Stop databases 


=> IAM components 


   1. IAM user 

      -> An IAM user represent one person or application 

         Parveen 
         Rahul 
         Priya 
         BackendServer 
         Githubaction 

      Each user get its own unique credentials 


      -> Root User Vs. IAM user 

         1. When we create AWS account , AWS automatically  create one special account
             Root user 

         2. Root user has unrestricted access

            1. Delete entire access
            2. Close AWS account 
            3. Change billing information 
            4. Delete all resources 
            5. Create IAM user 

           It has full administrative power 

           Only one Root user exist per AWS account 

         3. IAM User
          
            -> Only one Root user exist per AWS account 


         4. Should we use Root user daily -> No 

           1. Create the AWS account 
           2. Enable MFA on the Root user 
           3. Store the Root credentials securely 
           4. Create an Administration IAM user 
           5. Use the IAM User for daily work

   2. IAM Group 

      -> Suppose a company has 100 developers

      -> without group , we have to assign permission to each developer individually 

      -> That does not scale 

      -> Instead , Add all developers ,to this group 

      -> Now every member automatically gets the group's permission

   3. IAM Policy 

      -> A Policy is a JSON document that define permission

      -> Contains 

         1. What action allowed or denied 
         2. On which resources 
         3. Under what conditions 

   4. IAM Role 

     -> A Role is an identity that is assumed temporarily rather than permanently assigned to person

     -> Example 

        An EC2 instance needs to read files from s3


        Create an IAM Role with S3 read permission and attach it to the EC2 instance 

        AWS automatically provide temporary credentials to the EC2 instance.

        No long-lived keys are stored on the server             

   6. MFA (Multi-Factor Authentication)

      -> MFA adds an extra layer of security

      -> with MFA 

          1. username 
          2. password 
          3. OTP from Authenticator App                              
              
       
      


"""