""" 
=> Import and Export In DynamoDB 

    -> Import and export are managed features that let you move large amount of data into and 
       out of DynamoDB using Amzon S3


    -> Unlike reading and writing items through the APIs , these operation are performed by
       AWS in the background and are intended for bulk data movement 




                 Amazon S3
              /              \
             /                \
        Import              Export
           │                    │
           ▼                    ▼
      DynamoDB Table      DynamoDB Table       


=> Why we import and export 

    -> suppose we have 

        1. 500 millions customers 
        2. 2 Tb of historical logs 
        3. 100GB of product catalog


    writing them using putitem one by one would be very slow and expensive


    -> Instead 

       Amazon S3 -> Import -> DynamoDb


       DynamoDB -> Export -> Amazon S3 -> Athena / EMR / Spark


=> Import into DynamoDB

    -> Import creates a new DynamoDB table from data stored in s3

        Amazon S3 

         user.csv


      -> flow 

         Amazon S3 -> import service -> Create new table -> Load items -> table Ready


=> Internal Architecture Of import 


              Amazon S3
                    │
                    ▼
          Import Coordinator
                    │
      Read Files in Parallel
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
 Parse Data                 Validate Data
      │                           │
      └─────────────┬─────────────┘
                    ▼
           Create DynamoDB Items
                    │
                    ▼
         Parallel Bulk Write Engine
                    │
                    ▼
            DynamoDB Partitions


=> Step 1 Read files 

    -> AWS Read files from s3

       
        s3 

        users.csv
        orders.csv
        product.csv

   -> Large files are divided into chunks

       users.csv

       chunk 1 
       chunk 2
       chunk 3
       chunk 4

       multiple chunks are processed simultaneously


=> Step 2. Parse Data 

   -> Import services converts each row into DyanmoDB item

   -> csv = 101,Parveen,23

   -> becomes 

             {
              "UserId":"101",
              "Name":"Parveen",
              "Age":23
            }

=> Step 3 Validation 

   -> AWS validate 

      1. Required attributes 
      2. Data types 
      3. file format 
      4. Duplicate primary keys (last processed value for a duplicate key become the final item)

=> Step 4 Parallel write

   -> Import service groups items by partition key

   -> each partition writes independently  , allowing high throughput


=> Export from DynamoDB

    -> export copies table data into Amazon S3


      DynamoDb -> Export service -> Amazon S3


      original table reamain avaible for reads and write during the export 


   -> Internal architecture 


               DynamoDB Table
                    │
                    ▼
         Export Coordinator
                    │
        Scan All Partitions
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
Partition A    Partition B    Partition C
     │              │              │
     └──────────────┼──────────────┘
                    ▼
        Serialize Items
                    │
                    ▼
      Write Files into Amazon S3   


=> Step 1 Partition Scan 

    1. Suppose table has three partition

    2. each partition is scanned independently 


=> Step 2 Serialize

   -> Item are converted into the selected export format

                        {
              "UserId":"101",
              "Name":"Parveen"
            }

=> Step 3

    -> Write to S3

    -> files are written to s3 bucket


=>  Does Export lock the table?

     -> No. The table continues serving reads and writes while the export runs. 


=> Does Export consume RCUs?

     -> No. Export uses DynamoDB's internal storage snapshot mechanism 
        rather than normal read APIs, so it does not consume your table's read capacity.        


=>  How is Export different from using the Scan API to copy all items?

    Scan API	                        Export
Uses DynamoDB read APIs	                Uses internal storage snapshots
Consumes RCUs	                         Does not consume RCUs
Usually slower for very large tables	 Optimized for bulk export
Application must read and write data	 AWS manages the entire export process
Suitable for online processing	       Suitable for backups, analytics, and large-scale data movement           

    


"""