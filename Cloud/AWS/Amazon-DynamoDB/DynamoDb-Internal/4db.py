""" 

=> DynamoDB Internal Architecture 


                    Your Application
                           │
                           ▼
                    AWS SDK (boto3)
                           │
                           ▼
                    DynamoDB Endpoint
                           │
                           ▼
                  Request Router Layer
                           │
                           ▼
                Metadata & Partition Map
                           │
                           ▼
          ┌────────────┬────────────┬────────────┐
          ▼            ▼            ▼
         Partition A   Partition B   Partition C
            │            │            │
         Leader Node   Leader Node   Leader Node
            │            │            │
         Replica 1     Replica 1     Replica 1
         Replica 2     Replica 2     Replica 2


=> Client Layer 

    -> Application never talks directly to storage server 


                 table.put_item(
                        Item={
                          "UserId": "U101",
                          "Name": "Parveen"
                       }
                      )

        The AWS SDK creates and HTTP request and sends it to DynamoDB Service 

        Application -> AWS SDK -> HTTP Request -> DynamoDB

=> Request Router

    -> First AWS component that receives your request is the Request Router 

    -> Its job to answer 

       1. Which partition contains this item 

       2. It does not store data 

       3. It simply routes the request 

=> Metadata Service 

   -> The router needs to know where every partition is located 

   -> AWS maintain metadata like 

      Hash Range (0-1000) -> Partition 1 (1001-2000) -> Partition 2 (20001-3000)

      mapping is continuously updated as DynamoDB grows and split partitions

=> Hash Function 

   -> Partiton key , UserID = U101

   -> hash , U101 = 7454534 -> Partition B

   -> we never see the hash value , aws use it internally

=> Storage Partition

   -> Once DynamoDB indentifies correct partition

       Partition B 

       The item is stored here 

=> Replication

    -> One partition is not stored on a single machine

    -> AWs create multiple copies


=> Write Request Flow 


           Application -> Amazon SDK -> DynamoDB API -> Reqest Router -> hash(userId)

            Partition B -> Leader Node -> Replicate to Replica 1 -> Replicate to Replica 2 -> Success Resposne


=> Read Request Flow 

  Application -> Router -> Hash(userid) -> partiton B -> Read item -> Return resposne


  becuse dynamodb  knows exactly where the item is, it does not scan every parition it 

  this is why key-based lookup are fast 

=> Partition Splitting 

    1. Imagine one partition grows too large 

       Partition A -> 10GB 

       Over time 

       Partition B -> 50GB, too much traffic

       DynamoDb spread the workload

       Partition D


       AWS redistribute the data and updates its metadata so future request go to correct partition

"""