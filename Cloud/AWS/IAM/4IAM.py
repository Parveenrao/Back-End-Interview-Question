""" 

=> IAM Policies 

   -> An IAM Policies is a JSON Document that defines 

      1. Who gets the permission (when attached to user , groups or role)
      2. What action are allowed or denied 
      3. On which resources 
      4. Under what conditions


=> Why do We need Policies 

    -> Imagine AWS had no policies 

       1. Delete database 
       2. Delete EC2 instance 
       3. Read confidential S3 data 
       4. Create expensive resources 


=> Policy Structure 

   
     {
       "Version": "2012-10-17",
       "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:StartInstances",
      "Resource": "*"
     }
      ]
       }

    1. Version

        Version : 2012-10.17

        -> This is not version of the policy

        -> It specifies the version of the IAM policy language

        -> Today almost every IAM policy use 


    2. Statement 

        -> A policy can contain one or more statements.


          {

          "Statement" : [

             {.....},
             {.....},
             {.....},
          
               ]
             }           

        -> Think of each statment as a separate rule

        -> Rule 1 = Allow EC2

        -> Rule 2 = Allow S3 

        -> Rule 3 = Deny IAM

    3. Effect 

       -> Should AWS allow or deny this request 

          "Effect" : "Allow"
          "Effect" : "Deny"

       -> Allow EC2 

          {
          
             "Effect" : "Allow",
             "Action" : "ec2.*"
             "Resource" : "*"
          
          }   

        -> Deny S3 Delete 

          {
            "Effect":"Deny",
            "Action":"s3:DeleteObject",
            "Resource":"*"
          }   

    4. Action 

       -> Action specifies what operation is allowed or denied 

       -> Example 

          1. ec2:StartInstance 
          2. ec2:StopInstance 
          3. ec2:TerminateInstance 
          4. s3:GetObject
          5. s3:PutObject 

          6. lambda:InvokeFunction

       -> Every AWS services has its own action

         1. EC2

             -> ec2:StartInstances

             ->  ec2:StopInstances

             -> ec2:DescribeInstances

             -> ec2:TerminateInstances  

         2. S3 

             ->  s3:GetObject

             ->  s3:PutObject

             ->  s3:DeleteObject

             ->  s3:ListBucket   

    5. Resource

        -> Resource specifies which AWS resources the policy applies to

           1. Only one EC2 instance 
           2. Only one S3 bucket 
           3. Only one lambda function 

        -> "Resource" : "*"   -> Means all resources 



=> Example 

    {
  "Version":"2012-10-17",
  "Statement":[

      {
          "Effect":"Allow",
          "Action":"ec2:*",
          "Resource":"*"
      },

      {
          "Effect":"Allow",
          "Action":"s3:GetObject",
          "Resource":"*"
      }

  ]
}


=> Managed Vs Customer Managed Vs Inline Policies 

    1. AWS Manages Policies 

       -> Created and Managed By AWS 

          1. AmazonS3FullAccess
          2. AmazonEC2ReadOnlyAccess
          3. AmazonRDSFullAccess

    2. Customer Manages Policies        
 
          -> We create and managed these myselfs

          -> Allow EC2 , Stop EC2 , Read S3

    3. Inline Policies 

        -> Attached directly to a single user , group  or role

        -> Exist only that identity 
        -> cannot be reused elsewhere 

    -> Generally , customer managed policies are preffered because they can be reused and
       managed  centrally                  

"""