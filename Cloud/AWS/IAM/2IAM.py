""" 

=> IAM User Deep Dive 

    -> An IAM user is a identity that represent one person or one application inside your 
       application 

    -> Each IAM user has 

       1. Username 
       2. Password 
       3. Access keys (for APIs/CLI)
       4. Permissions 
       5. MFA(Optional)

=> AWS Account Vs. IAM User 

    1. When we sign up for aws , we create on AWS account 

    2. Inside AWS account , we create IAM users 

    3. One AWS account -> Many IAM Users


=> What Does IAM user contain 

   1. Username -> Just like a window username 

   2. Passowrd -> If the user needs to log into the AWS Console , they need a password 

   3. Access Keys 

      -> Suppose python code wants to upload a file to S3

      -> How AWS know it is your application

      -> It uses  Access key ID
 
      -> The Secret Access key is shown only once when it is created 
         if we loose it , we cannot retrieve it -> we must create a new access key 

   4. IAM User Permission 

       -> New IAM user start with no permission by default 

       -> Where Do Permission come from 

          Policies / Group or both        



"""