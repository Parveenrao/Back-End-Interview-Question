""" 
=> Public Vs Private Bucket

    -> Who can access the object stored on the bucket 



    1. Private Bucket 

        -> A private bucket is accessible only to authorized AWS indentities (IAM users , IAM roles
           or AWS services) that have been granted permission

        -> Characteristics 

            1. Block Public address is Enabled 

            2. Bucket policy allws only authorized user/roles

    2. Public Bucket 

       -> A public bucket allows anyone on the internet to access some or all of its objects 


       -> how bucket become public

          1. Block public address -> disable 

          2. A bucket policy or acl grants public permission


=>  Are S3 buckets public by default?

    -> Newly created S3 bucket are private by default , and block public address is enabled by defult

=>  Should application backups be stored in a public bucket?

    -> No. Backups should always be stored in a private bucket with encryption 
       and restricted access.    




"""