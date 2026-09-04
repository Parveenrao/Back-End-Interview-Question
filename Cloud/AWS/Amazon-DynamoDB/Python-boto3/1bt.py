""" 

=> Boto3

    -> boto3 is the official AWS SDK for python

    -> It allows python applications to communicate with AWS services such as 

        1. DynamoDB
        2. S3
        3. Lmabda
        4. SQS
        5. SNS
        6. IAM
        7. EC2
        8. Cloudwatch

    python code -> boto3sdk -> HTTPs request -> AWS service


    -> Instead of manually creating HTTP request , boto3 handles.

       1. Authentication 
       2. Request signing
       3. Serialization 
       4. Retries
       5. Response parsing

 => Boto3 Architecture

                Python Application
                       │
                       ▼
                  boto3 SDK
                /             \
         Resource API      Client API
                │               │
                └──────┬────────┘
                       ▼
                 botocore Library
                       │
            Request Signing (SigV4)
                       │
                 HTTPS Request
                       │
                       ▼
                  DynamoDB API
                       │
                       ▼
                 JSON Response
                       │
                       ▼
                    Python    


=> boto3 component

1. Resource API

    -> high level , object - oriented and easier to use

       table.put_item(Item = item)

       feel like working with python objects 


2. Client API

   -> Low-level interface that maps closely to AWS service APIs


                      client.put_item(
                        TableName="Users",
                        Item={
                          "UserId": {"S": "101"}
                       }
                       )

    -> We specify dynamoDB attribute such as 

       s -> string 
       N -> number 

       Bool -> boolean 

       M -> Map 

       l -> list

=> Resource vs Client
           Feature	                    Resource	   Client
            Level	                        High	     Low
            Easier to use	                 ✅	       ❌
            Object-oriented	                 ✅	       ❌
            Better for beginners	         ✅	       ❌
            Direct API access	             ❌	       ✅
             More AWS features	              Limited	Full

In most application code, developers use the Resource API. 
Use the Client API when you need access to lower-level operations 
or features not exposed by the resource interface.       



=> How boto3 work internally 



         table.put_item(
    Item={
        "UserId": "101",
        "Name": "Parveen"
    }
)

    Python Code
      │
      ▼
boto3 Resource
      │
Convert Python Dict
      │
      ▼
botocore Serializer
      │
JSON Payload
      │
      ▼
AWS Signature V4
      │
HTTPS Request
      │
      ▼
DynamoDB Endpoint
      │
Store Item
      │
JSON Response
      │
Deserialize
      │
Python Dictionary


=> boto3 use HTTPs 


Application
      │
    HTTPS
      ▼
AWS Load Balancer
      │
DynamoDB Frontend
      │
Partition Router
      │
Leader Replica
      │
Storage Engine



"""