""" 


=> Delete Operation Internal 


=> High Level Delete Flow

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
                  Write Ahead Log (WAL)
                          │
                          ▼
                Delete from MemTable
                (Mark item as deleted)
                          │
                          ▼
                 Replicate Delete
                   to Replica Nodes
                          │
                          ▼
                    Update GSIs / LSIs
                   (Delete index entries)
                          │
                          ▼
                 Write to DynamoDB Stream
                     (if enabled)
                          │
                          ▼
                     Return Success
                          │
                          ▼
                Background Compaction
             Physically removes data later


=> Step 1 Client send deleteItem

            table.delete_item(
                  key = {
                  
                  
                  "UserId" : "101",
                  "OrderId" : "5001"})

            -> Request contain 

                1. Table name 
                2. primary key 
                3. optional condition 
                4. Return values


=> Step 2 Front-End Router

    1. authenticate request 
    2. check IAM permission
    3. hash the partition key
    4. find correct storage partition 

=> Step 3 Leader Accept write


=> Step 4 Condition check (Optional)

    -> if we specify 

       ConditionExpression="attribute_exists(UserId)"

       ConditionExpression="Status='Pending'"

       the leader first check the condition

       if condition fails 

         1. Deleted reject 

         2. ConditionalCheckfailed exception

         No deletion happen

=> Step 5  WAL 

   -> before deleting 

   -> Write delete operation in wal

   
=> Step 6 Memtable update

    -> The in-memory structure is updated

    -> instead of immediately erasing the item , DyanmoDB records a delete marker(tombstone)


    -> after deleting 

                     101
                       ├── Order1
                       ├── Tombstone
                       └── Order3

        the tombstone tells the storage engine that the item is logically deleted

=> Step 7 Replica to other replicas

   -> Leader sends the delete to follower replicas

   -> Once enough replicas ack the write DynamoDB reports success

   -> writes are synchronously replicated within the partition for durability

=> Step 8 Update secondary indexes 

    -> if deleted entries appears in

       1. LSI 
       2. GSI

=> Step 9 DynamoDb streams

   -> if streams are enabled , a delete event is generated


                       DELETE

                         Old Image

                          {
                            UserId:101
                            Status:Pending
                           }

         event can be trigger by 

          1. lambda 
          2. Eventbridge 
          3. CDC pipeline 
          4. Audit processing

=> Step 10  Return Success


=> Step 10 Compaction 

    -> Data is not immedaitely removed from disk

    -> Storage looks like 

        SStable 

           Item A
           Item B
           Tombstone 
           Item D

        During compaction 

        Old  compaction 

           old sstable 

           Merge 


           discard tombstone 

           new sstable


           only then this deleted data physically reclaimed.


=>   Does a DeleteItem consume RCUs or WCUs?
       -> It consumes Write Capacity Units (WCUs) because a delete is a write operation.                        



"""