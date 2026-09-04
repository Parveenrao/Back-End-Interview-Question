""" 
=> Bucket Policies 

   -> A bucket policies is a json document attached to S3 bucket that define who can access the 
      bucket  and what action they can perform


 => Why do we bucket policies 

    -> Suppose we have bucket , parveen-video-storage 

       1. can everyone read the files 
       2. can only my ec2 instance  upload video 
       3. can specific iam user delete objects 
       4.      


=> Structure of Bucker Policy 


       {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "...",
      "Action": "...",
      "Resource": "..."
    }
  ]
}

   1.  Version 

        -> This is not the bucket version 

        -> It specifies the policy language version

   2. Statement 

      -> A policy can contain one or more rule

               "Statement": [
                     Rule 1,
                     Rule 2,
                     Rule 3
                ]

      -> Allow uploads 

      -> Deny deletes

      -> Allow reads


    All exist in one policy


  3. Effect 

    -> Determine whether action is allowed or denied


  4. Principal 

      -> Specifies who the policy applies to 


            "Principal": {
                 "AWS": "arn:aws:iam::123456789012:user/Parveen"
                }                 
       
      -> Only this IAM user can access


   5. Action 

      -> Specify what action is allowed 

      -> Download object , upload object , delete object 

   6. Resources 

       -> Specifies which bucket or object the policy apply to


       arn:aws:s3:::parveen-video-storage/* 


        /* -> all resources


     -> Example allow only read only access 


          {
          "Version": "2012-10-17",
           "Statement": [{
           "Effect": "Allow",
           "Principal": {
                 "AWS": "arn:aws:iam::123456789012:user/Parveen"
             },
                "Action": "s3:GetObject",
             "Resource": "arn:aws:s3:::parveen-video-storage/*"
          }]
       }         

"""