""" 
=> SNS Topic Ownership
  
     -> Topic ownership defines who owns an SNS topic , who can manage it , and who is allowed
        to publish or subscribe to it


         this become especially important in multi account aws enviornment


=> What is topic ownership

   -> When an sns topic is created , AWS records the AWS account ID that created it

      Account A -> create topic -> orderEvents

      aws internally store it

      topic : Orderevents

      owner : 1112224444

      the owner is the aws account , not the IAM user


=> WHy does ownership matter

   -> Suppose anyone could modify topic

   -> someone could delete it

      1. delete it 
      2. change permission 
      3. subscribe malicious endpoints 
      4. publish fake message

    ownership prevent this


=> Internal Architecture

            AWS Account A
                │
                ▼
        Create SNS Topic
                │
                ▼
+--------------------------------+
| SNS Topic                      |
|--------------------------------|
| Topic ARN                      |
| Owner Account ID               |
| Topic Policy                   |
| Encryption Settings            |
| Access Control                 |
+--------------------------------+


=> What does owner control

    1. delete the topic 
    2. change topic attribute 
    3. enable encryption 
    4. modify topic policy
    5. allow or deny publisher
    6. allow or deny subscriber 
    7. add delivery policies


=> Topic ARN

   -> Every sns topic has a unique arn

arn
│
aws
│
sns
│
us-east-1
│
111122223333   ← Owner Account ID
│
OrderEvents

account id -> identifies topic owner


=> IAM user vs topic owner

           AWS Account
             │
             ├── Admin
             ├── Developer
             └── Intern

     developer creates

       OrderTopic

       is the deveoper the owner

       no

       aws store 

       owner = aws account

       even if the developer later leaves the company topic still belongs to the AWS ACCOUNT


=> Topic Policy

   -> Ownership alone does not who can use the topic

   -> sns also check the topic policy

   -> example policy
    {
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::444455556666:root"
  },
  "Action": "sns:Publish",
  "Resource": "arn:aws:sns:us-east-1:111122223333:OrderEvents"
}


=> Cross-Account ownership

   Imagine two companies

   Company A -> AWS Account A

      company a owns -> orderevent

   Company B want to publish

    without permission

    Account B -> publish -> Access denied


=> Can Ownerhsip change

   -> Normally no

   AWS does not provide a way to transfer ownership of an sns topic to another aws account

   if another account need ownerhsip , common approach is

    1. create a new topic in the new account 

    2. update publisher and subscriber 

    3. delete the old topic if it is no longer needed.

"""