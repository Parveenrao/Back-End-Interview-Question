""" 

=> What is Terraform 

    -> Terraform is an Infrastructure as Code(IAC) tool developed by HasiCorp

    -> It allow you to define cloud infrastructure in code of creating resources manually through 

       AWS console

=> How Does Terraform Work 

   -> Terraform does not log into AWS console and click buttons 

   -> Instead , it communicate directly with AWS service through Their APIs


      Terraform code -> Terraform CLI -> AWS provider -> AWS APIs -> AWS infra.


=> Internal WOorking 


   You -> terraform apply -> terraform core -> Read .tf files , builds Dependency graph , Calculates change -> AWS provider plugin -> 

   convert terraform into AWS API calls -> AWS API -> EC2, S3 , IAM , VPC


   -> Terraform core 

       -> Brain of terrform 

       -> Reading .tf files 

       -> Understanding resources dependencies 

       -> Comparing the current infrastructure with the desired state 

       -> Creating an execution plan

=> Provider 

   -> Provider is a plugin that knows how to talk to specific platform 


   -> without provider , terraform would not know how to create resource on that platform


=> Resources

   -> A resources is any infrastructure object terraform manages

=> Terraform workflow 

   
   write code -> terraform init -> terraform plan -> terraform apply -> infrastructured created


   1. Write code

      -> Create one or more .tf files 

   2. terraform init

      -> intilizes the project 

      -> downloads 

         1. AWS provider 
         2. Required plugins 
         3. Project metadata


   3. Terraform plan 

      -> terraform compare


         current infrastructure vs Desired infrastructure

   4. terraform apply

      -> terraform execute the plan by calling the AWS APIs and creating updating resources


=> What is provider 

   -> A plugin that allows terraform to communicate with specific platform such as 
      AWS , Azure , or kubernetes 

=> Resources 

   -> A resources represent a single infrastructure object managed by terraform , such as 

      EC2 instance , an S3 bucket or VPC


"""