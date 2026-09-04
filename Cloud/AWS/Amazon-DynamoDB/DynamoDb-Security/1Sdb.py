"""" 

=> IAM Integration In DynamoDB
  
 
   -> Biggest advantage of DynamoDb is that it does not manage users or passwords itself.

   -> Instead , it relies on IAM (Identity and access Management) to control who can access and 

      what operation they can perform 


=> High Level Architecture 

                User / Application
                      │
              AWS Credentials
                      │
                      ▼
             AWS SDK / CLI / Console
                      │
          Signed Request (SigV4)
                      │
                      ▼
          DynamoDB Front-End Service
                      │
          IAM Authentication Check
                      │
        Is the identity authenticated?
             /                 \
          No                    Yes
          │                      │
      Reject Request      IAM Authorization
                                │
                 Check IAM Policies
                                │
                 Is action allowed?
                    /          \
                 No             Yes
                 │               │
            AccessDenied     Execute Request
                                │
                                ▼
                     Read / Write Data

                     
=> Step 1 Authentication 

    -> Before DynamoDB checks permission , AWS first verifies who you are

    -> Authentication answer ,
        
        "Who is making this request"

        AWS support 

        1. IAM User 
        2. IAM Role 
        3. EC2 Instance Profile 
        4. Lambda Execution Role 
        5. ECS task Role 
        6. EKS IAM Role 
        7. Federated Role 
        8. AWS SSO

     application -> access key / secret key -> Request signed using SigV4 -> AWS verifies signature

     if the signature is invalid , 403 forbidden

     No request reaches DyanmoDB


=> Step 2 Authorization 

   -> Now AWS knows the caller identity

   -> Next it ask

       Is this identity allowed to perform this operation

    -> example , GetItem 

                  Policy

                     Allow
                     Action:
                        dynamodb:GetItem

                     Resource:
                        Orders Table  

        if yes , continue

        otherwise , AccessDeniedException


=> IAM Policy Structure 

                {
         "Version":"2012-10-17",
          "Statement":[
              {
               "Effect":"Allow",
                "Action":[
                    "dynamodb:GetItem",
                    "dynamodb:PutItem"
                ],
            "Resource":"arn:aws:dynamodb:us-east-1:123456789012:table/Orders"
            }
          ]
        }

=> Policy Component 


Policy
│
├── Effect
│      Allow / Deny
│
├── Action
│      GetItem
│      PutItem
│      DeleteItem
│      Query
│      Scan
│
├── Resource
│      Table ARN
│
└── Condition


=> Step 3 Resource ARN

    -> Every DynamoDB table has a unique ARN  

            arn:aws:dynamodb:region:account-id:table/Orders


            arn:aws:dynamodb:ap-south-1:123456789012:table/Orders
    -> Policy example 



                              Only Orders table

                                 Allowed

                                 Orders

                                 Denied

                                 Users
                                 Payments
                                 Logs        

                                 
=> Step 4 Action Level Permission

   -> IAM allow fine-grained control over operation

                           Operation	   IAM Action
                            Get Item	    dynamodb:GetItem
                            Put Item	    dynamodb:PutItem
                            Update Item	    dynamodb:UpdateItem
                            Delete Item	    dynamodb:DeleteItem
                            Query	        dynamodb:Query
                            Scan	        dynamodb:Scan
                            Batch Write	    dynamodb:BatchWriteItem
                            Batch Get	    dynamodb:BatchGetItem
                            Create Table    dynamodb:CreateTable
                            Delete Table	dynamodb:DeleteTable

=> Step 5 Explicit Deny

    -> AWs always execute 

      
       explicit Deny -> allow -> Default -> deny

=> Step 6 IAM Role

    -> Instead of storing keys inside application , AWS recommends using IAM Roles


      EC2 -> Attached IAM Roles -> Temporary Credentials -> DynamoDB

      No access key or secret key is hardcoded

=> Step 7 Temporary Credentials

    -> AWS use the Security Token Service(STS)


    IAM Role -> STS -> Temporary credentials -> Expire in hours

=> Does DynamoDB maintain its own user database?

     -> Answer: No. DynamoDB relies on IAM for authentication and authorization.   

=> Why should IAM Roles be preferred over Access Keys?

    -> Answer: IAM Roles provide temporary credentials via STS, 
       avoid hardcoded secrets, and automatically rotate credentials, 
       improving security.  

=> What happens if no IAM policy allows an action?

    -> Answer: Access is denied by default (implicit deny).  

=> What if one policy allows an action and another explicitly denies it?

    -> Answer: The explicit deny takes precedence, and the request is rejected.      

=> Can IAM restrict access to specific DynamoDB items?

    -> Answer: Yes. By using condition keys such as dynamodb:LeadingKeys, you can implement fine-grained, item-level access control.            

"""