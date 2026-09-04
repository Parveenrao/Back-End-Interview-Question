""" 

=> Backup And Restore In DynamoDB

    -> backup and restore protect your data from accidental deletion , corruption ,
       or operational mistake

    -> Snapshot of table creating a snapshot of your table that you can restore later 


    Dynamo Table -> Create backup -> Backup storage -> Restore backup -> New DynamoTable

    -> A restore does not overwrite the existing table , it always creates a new table


=> Types Of backup 

    DynanmoDB provides two main backups mechanisms.

    1. On Demand Backup

       -> An on-demand backup is manual snapshot of your table at a specific moment.

       10:00 AM user table -> Create table -> backup stored

       if data change later , 10:30 AM user#5 added ,

       the backup still contains only the data as it existed at 10:00 AM


       -> Flow 

          DynamoDb table -> Create backup -> Encrypted backup storage

       -> Restore from on-Demand backup

          suppose table is deleted

          backup -> restore -> new table created


    2. Point-in-Time Recovery (PITR)

        -> PITR continuously records changes so you can restore your table to almost 
           any second within the retention window.


         -> Timeline

                        Time

                        10:00
                          │
                        10:05
                          │
                        10:10
                          │
                        10:15
                          │
                  10:20  Accident
                          │
                Restore to 10:19:59              


                

=> Internal Architecture



                Application
                    │
                    ▼
              DynamoDB Table
                    │
      ┌─────────────┴─────────────┐
      │                           │
      ▼                           ▼
On-Demand Backup          PITR Change Log
      │                           │
      ▼                           ▼
 Backup Storage          Continuous Recovery Data
      │                           │
      └─────────────┬─────────────┘
                    ▼
             Restore Process
                    │
                    ▼
           New DynamoDB Table


=> What gets Backed up 

    1. Table data (items)

    2. Table schema (Partition key , sort key)

    3. Local secondary index (LSI)

    4. GSI

    5. Provisioned secondary index and other table configuration


    -> It does not backup

        1. DynamoDB streams 
        2. Auto scaling process
        3. Cloudwatch alarms 
        4. IAM permissions
        5. Application code

=> Performance Impact

     1. Does not require taking the table offline 

     2. Does not block reads or writes


=> Can we restore only one item

   -> No backup and PItR restore entire table 

=> Does backup stop read and write 

   -> backup operation are designed to occur without taking the tab

"""