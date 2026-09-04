""" 


=> UpdateItem Internals 


=> High level Update Flow 

               Client
                 │
                 ▼ 
              AWS SDK
                 │
                 ▼
       DynamoDB Front-End Router
                 │
                 ▼
         Find Target Partition
          (Hash Partitioning)
                 │
                 ▼
          Leader Replica
                 │
                 ▼
        Authenticate & Validate Request
                 │
                 ▼
     Check ConditionExpression (Optional)
                 │
                 ▼
     Read Current Item (if needed)
                 │
                 ▼
       Apply Update Expression
                 │
                 ▼
        Write Ahead Log (WAL)
                │
                ▼
     Write New Version to MemTable
               │
               ▼
       Replicate Update
       to Replica Nodes
              │
              ▼
     Update GSIs / LSIs
              │
              ▼
    Write to DynamoDB Streams
        (if enabled)
              │
              ▼
       Return Success
              │
              ▼
     Background Compaction
      (Removes old versions)


=> Request Reaches Front End Router

    1. Authenticate the request
    2. Check IAM permissions 
    3. Hash the partition key
    4. Locate the storage partition


=> Step 2 Leader Replica Recieve Update

     Every partition has 

     Leader

     Replica A 

     Replica B


     Only leader perform the action

=> Condition check (Optional)

    ConditionExpression ' "Age = :old"

    if the stored value is 

       age = 24

=> Step 4 Read Existing item

    -> Unlike PutItem, an update often needs the current item


=> Step 5 WAL

   -> If the node , crashes immediately afterwards , WAL can replay the operation during recovery

=> Step 6 New version written to memtable

    -> Many database overwrite the existing record 

    -> DyanmoDB does not

    -> it appends a new version

    -> the memtable now contains the latest version

=> Step 7 Replication 

   -> Leader sends the replication to follwer replicas

   -> once enough replica ack the write , DynamoDN returns the success

=> Step 8 Update GSI 

=> Step 9  Dynamo Streams 

   if streams are enabled

               MODIFY

              Old Image

               Age=24

              New Image

               Age=25

          event can trigger

            1. lambda 
            2. Audit system 
            3. ETL pipeline


=> Step 10 Return success

    -> depending on Return Values , DynamoDb can return

        None 

        ALL_new 

        Updated_new 

        ALL_old 

        updated_old

=> step 11 Background compaction         
"""