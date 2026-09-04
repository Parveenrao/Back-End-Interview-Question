""" 

=> Introduction To Infrastructure As a Code 

     -> To Run application we need 

        1. VPC
        2. 2Public Subnet 
        3. 2private Subnet 
        4. Internet Gateway 
        5. NAT Gateway 
        6. Route Table 
        7. Security Groups 
        8. EC2 Instances 
        9. Load Balancer 
       10. Auto-Scaling Group 
       11. RDS Database 
       12. S3 Bucket 
       13. IAM Role 
       14. CloudWatch 
       15. SNS
       16. SQS


      This is your infrastructure

    -> before IAC , engineers created everything manually 

    -> Every resource required clicking through the AWS Management Console 

    -> Creating one environment take hours


    -> Problem With Manual Infrastructure 

       1. Human Error 

       2. No documentation

       3. Not Repeatable 

       4. Difficult Diaster Recovery

       5. Team collaboration 



=> Why it is called Infrastructure As Code 

 
   1. Because infratstructure is treated exactly like application code 


=> Key Characteristics OF IAC 

   1. Declarative -> We described the end state and tool figure out how to create it 

   2. Version controlled -> Infrastructure definitions live in GIT alongside your application code 

   3. Automated -> Updates are executed with commands or CI/CD pipeline 

   4. Consistent => Development , staging , and production enviroment can be created 

      from same codebase with different configuration 

   5. Reusable => Common infratstructure (VPC OR security groups) can be packed into reusable module   




"""