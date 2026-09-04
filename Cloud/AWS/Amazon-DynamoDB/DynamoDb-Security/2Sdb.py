""" 


=> Resources Policy In DynamoDB

     -> Resources policies are resources-based IAM policies that are attached directly to a
        DynamoDB resources (such as table or stream)

     -> They specify who can access that resources and under what conditions , making 
        them especially usefull for cross-account access


     ->  Identity based policy (IAM policy) = What is this user or role allowed to do

         Resources policy = who is allowed to access this table


=> Identity Policy                                   Resource Policy
 
   Attached to IAM users, groups, or roles	       Attached to a DynamoDB table or stream
   Defines what an identity can do	               Defines who can access the resource
   Managed in IAM	                               Managed on the resource
   Commonly used within an account	               Commonly used for cross-account access               

   


=> Resource Policy Example 
                                {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::222222222222:role/AnalyticsRole"
      },
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query"
      ],
      "Resource": "arn:aws:dynamodb:ap-south-1:111111111111:table/Orders"
    }
  ]
}


=>  What is a DynamoDB resource policy?

      -> A policy attached directly to a DynamoDB resource that 
         defines who can access it and what actions they can perform.

=> Why use a resource policy?

    -> Primarily to enable secure cross-account access without 
       relying solely on IAM role assumption patterns. 

=> Is a resource policy the same as an IAM policy?

     -> No. IAM policies are attached to identities (users/roles), 
        while resource policies are attached to the resource itself. 

=> Can a resource policy deny access?

    -> Yes. An explicit Deny in a resource policy overrides any Allow.  


=> Does a resource policy replace IAM policies?

    No. AWS evaluates all applicable policies together. Access is granted 
     only if the overall evaluation allows the request and there are no 
     applicable explicit denies.                        
"""