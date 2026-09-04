""" 

=> Write Operational Internal 
   
    -> A write operation is any operation that modifies data in DynamoDB

      
       PutItem              -> Create or repace an item 
       UpdateItem           -> Update specific attribute 
       DeleteItem           -> Delete an item 
       BatchWriteitem       -> Multiple puts/deletes 
       Transactionwriteitem -> Multiple write as a transaction  

       
=> Flow 

                           Client
                             │
                             ▼
                          AWS SDK
                             │
                             ▼
                  DynamoDB Front-End Router
                             │
                             ▼
                      Find Partition
                             │
                             ▼
                      Leader Replica
                             │
                             ▼
                     Validate Request
                             │
                             ▼
                 Check Conditions (if any)
                             │
                             ▼
                    Write Ahead Log (WAL)
                             │
                             ▼
                      Update MemTable
                             │
                             ▼
                        Update LSI
                             │
                             ▼
                   Replicate to Followers
                             │
                             ▼
                     Acknowledge Success
                             │
                             ▼
                 Asynchronously Update GSI
                             │
                             ▼
                  Background Flush to SSTables       


=> Step 1 Request Reaches the Leader

     -> Front end router already determined the correct partition

     -> Why only the leader

     -> imagine two client updating the same item simulataneously 

        Client A = 24

        Client B = 25

        if both follower accepted write independently 

        Now replica disagree , which value is correct

     -> One leader coordinator all writes

=> Step 2 Request Validation 

     -> Before writing anything , DynamoDB validates the request 

     1. Authentication -> Is request signed correctly 

     2. Authorization 

        -> Does the IAM policy allow this operation 

                 {
               "Effect": "Allow",
               "Action": "dynamodb:PutItem"
             }

             if not -> AccessDeniedException 

        -> Table exist , if table not exist , ResouceNotfoundException

        -> Primary key present

            Table require PK , SK

            we send {
                        "PK" : "User101" 
                          }

            missing sort key 

            Result -> Validation exception

        -> Item size 

            Maximum Item size = 400kb

            if larger -> validation exception

        -> Data type 

           Expected Age -> number 

           send age -> binary 

           Validation fails 


=> Step 3 Conditional Check

    -> We write 

                      table.put_item(
                           Item=item,
                          ConditionExpression="attribute_not_exists(UserId)"
                          
                       )

     before  writing , DynamoDB checks

     Does USER#123 already exist 

     if it exist 

     ConditionalCheckFailedException

     No write happen 

     Nothing reach wal

     this is how DynamoDB prevent accidental overwrites and support optimistic concurrency control

=>  Step 4 Update Memtable 

=> Step 5 Update LSI synchronous 

=> Step 6 Replicat to Followers



=> Step 7 Update GSI Async

=> Step 8 Memtable -> SStable 

=> Step 9 Compaction 

"""