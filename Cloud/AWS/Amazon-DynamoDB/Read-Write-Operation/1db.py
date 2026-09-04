""" 


=> DynamoDB Request FLow 

    1. Imagine application does this

       table.put_item(
       
           items= {
           
                  "UserId" : "123",
                  "Name"   : "Parveen",
                  "Age"    : 24     
                  }
                )


   2. High level flow 

                                   Application

                                       │
                                       ▼

                                     AWS SDK

                                        │
                                        ▼

                                    HTTPS Request

                                        │
                                        ▼

                              DynamoDB Front-End Router

                                       │
                                       ▼

                                 Partition Metadata Lookup

                                       │
                                       ▼

                               Find Correct Storage Partition

                                       │
                                       ▼

                                  Leader Node

                                       │
                                       ▼

                                Write Log (WAL)

                                       │
                                       ▼

                                    MemTable

                                       │
                                       ▼

                                   Replication

                                       │
                                       ▼

                                   ACK Returned

                                       │
                                       ▼

                              Client Receives Success


=> Step 1 Application send request

    table.put_item()

    -> SDK creates an internal request

=> Step 2  AWS SDK
    
    -> SDK convert request into json payload


         {
            "TableName":"Users",
             "Item":{
                  "UserId":{"S":"123"},
                   "Age":{"N":"24"}
         }
        }

    -> Everything become an attribute

    -> SDK also 

        1. Calculate request size 
        2. Add authentication headers
        3. Signs the request using AWS signature version 4
        4. open or reuse an HTTPS connection

=> Step 3 HTTP Request 

    -> Request goes over 

      Application -> Internet / AWS network -> DynamoDB endpoint 


=> Step 4 

   -> Front end router

   -> The request first reach the DynamoDB front-end service

   -> Like traffic controller 

   -> It does not store your data 


   -> Job is to

       1. Authenticate the request 
       2. Authorize it using IAM permission
       3. Validate the request format 
       4. Enfore api limit 
       5. Route request to the correct storage partition


    -> Router does  not scan all partitions

    -> it perform a metadata lookup to identify the correct partition and forward the request 

       directly 


=> Step 5 Partition Leader 

     -> Every storage has multiple replica

        Replica 1 
        Replica 2
        Replica 3 

       One replica is the leader 

       ALl write go to leader first  , only one node  coordinate  writes , preventing conflicting 
       updates and ensure consistency

=> Step 6 WAL

   -> Leader does not immediately update the main storage files

   -> it append the opertion to WAL 

=> Step 7 Memtable 

   -> After log is safely written , data is stored in an In-memory structure called 
      Memtable

    -> Later memtable is flushed to sstable 


=> Step 8 Replication 

   -> The leader then replicate the write to followe replica

   -> leader wait until the required number of replica ack the write before 
      considering it successfull.


=> Step 9

   -> After the write is durable recorded and replicated acc to DynamoDb consistency gurantees 

       leader return success to front end router

=>  Logical partitions never store other partitions' replicas. 
    Replicas are stored on physical storage nodes, and each replica belongs 
    only to its own logical partition.       

    
=> Logical Partition A
    ├── Replica on Storage Node 1
    ├── Replica on Storage Node 2
    └── Replica on Storage Node 3

Logical Partition B
    ├── Replica on Storage Node 1
    ├── Replica on Storage Node 4
    └── Replica on Storage Node 5    




"""