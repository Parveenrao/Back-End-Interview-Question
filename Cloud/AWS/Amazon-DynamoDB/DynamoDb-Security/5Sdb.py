"""" 

=> VPC Endpoint For DynamoDB

    -> A VPC endpoint for dynamodb allows resources inside our Virtual Private cloud to 
       access DynamoDB using public internet , even though DynamoDB is a fully managed 
       AWS service

    -> This improves security , reduces latency and keeps traffic inside aws network

=> Why do we need VPC endpoint

   -> Suppose our application is running inside a vpc

      EC2 -> Internet Gateway -> Public Internet -> DynamoDB

      even though the communication is encrypted using HTTPs , it still leaves  VPC

      Some companies do not allow this because of security or compliance requirements

      AWS provide VPC endpoints to solve this


=> With DynamoDB VPC Endpoint    


            AWS Network
+-------------------------------------------+

        VPC

+----------------------------+
|                            |
|   EC2 / Lambda / ECS       |
|          │                 |
|          ▼                 |
|    VPC Endpoint            |
|          │                 |
|          ▼                 |
|      DynamoDB              |
|                            |
+----------------------------+

No Internet Gateway
No NAT Gateway
No Public IP


-> Traffic never goes through the internet

-> Everthing stays on the AWS private backbone


=> Types of VPC endpoints

    1. Gateway endpoint 

    2. Interface endpoint (Privatelink)


    DynamoDB use Gateway endpoint


=> Why Gateway Endpoint

    -> DyanmoDB is a regional service 

    -> Instead of creating network interface (ENIs) , AWS simply add a route to our route table


                Route Table

             Destination                Target

              10.0.0.0/16               Local
              0.0.0.0/0                 NAT Gateway
              pl-xxxxxxxx               DynamoDB Gateway Endpoint

        when taffic matches the DynamoDB prefix list it is routed directly to DynamoDB over 
        aws network

=> Internet Flow 

    Application
      │
      ▼
AWS SDK
      │
      ▼
DNS Resolution
      │
      ▼
Route Table
      │
      ▼
Gateway Endpoint
      │
      ▼
AWS Backbone Network
      │
      ▼
DynamoDB Frontend
      │
      ▼
Storage Nodes


-> No internet is allowed


=> Without Endpoint

Application
      │
      ▼
Route Table
      │
      ▼
Internet Gateway
      │
      ▼
Public Internet
      │
      ▼
DynamoDB


=> Does DynamoDB become part of my VPC?

      No.



Your VPC

EC2
Lambda
ECS
RDS

↓

Gateway Endpoint

↓

DynamoDB

DynamoDB remains an AWS-managed regional service outside your VPC. 
The endpoint simply provides a private route from your VPC to the service


=> Security 

   -> A dynamoDb gateway endpoint support an endpoint policy

   -> we can control 

       1. Which dynamoDB table can be accessed 

       2. WHich IAM principle can use the endpoint 

       3. Which dynamoDB actions are allowed


       Allow

Table:
Orders

Actions:
GetItem
PutItem
Query

Deny

DeleteTable
Scan


-> This adds another layer of access control in addition to IAM
"""