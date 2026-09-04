""" 

=> Read Operation Internals 

           Client
             │
             ▼
           AWS SDK
             │
             ▼
      Front-End Router
             │
             ▼
        Find Partition
             │
             ▼
        Choose Replica
             │
             ▼
        Check MemTable
             │
             ├── Found? → Return Item
             │
             ▼
        Check Block Cache
             │
             ├── Found? → Return Item
             │
             ▼
        Use Bloom Filters
             │
             ▼
        Read SSTables
             │
             ▼
        Merge Results (if necessary)
             │
             ▼
        Return Response

        

=> Client Send Read Request

          response = table.get_item(
             Key={
              "UserId": "123"
            }
        )


    The SDK convert this into an HTTPS request and send it to DynamoDB

=> Router Find the Partition

     -> No table scan 

     -> Router knows exactly which partition owns the item

=> Choose A replica

    -> Now dynamoDB decide which replica should serve the read


    -> Eventual consistent Read (Default)


         Leader -> Replica 1 , Replica 2

     Read can be served by any replica , which distribute load and reduce latency

    -> Strong consistency read

       Leader 

       -> Read come from the leader , ensure the latest committed write a returned

=> Check the Memtable

   -> If the requested item was written recently and has not yet been flushed to SStable, it
      is still in the memtable

   -> if found , no sstable is accessed

=> Block cache 

   -> Suppose an item has already been flushed from the memtable to an sstable

      Memtable -> SStable(disk)

      Now client repeadetly reads the same item

      without cache , every read woudl requiring accessing the disk

      disk is much slower than reading from RAM

    -> Solution , Block cache

       1. DynamoDB keeps recently accessed blocks of SStable in memory


                                       RAM

                         +-------------------------+
                         | Block Cache             |
                         |                         |
                         | Block 1                 |
                         | Block 7                 |
                         | Block 12                |
                         +-------------------------+

                                    ▲

                                    │

                           SSTables on Disk  


                        when read arrive 

                        1. check memtable 
                        2. check block cache 
                        3. only if not found , read from sstable on disk

    -> Why it is called block cache

        -> An sstable is not read one item at a time

        -> Imagine sstable look like this 
 
               SSTable

+--------------------------------+
| USER#1                         |
| USER#2                         |
| USER#3                         |
| USER#4                         |
| USER#5                         |
| USER#6                         |
| USER#7                         |
+--------------------------------+         


        -> file is divided into blocks


                  SSTable

+------------+
| Block 1    |
| USER1      |
| USER2      |
+------------+

+------------+
| Block 2    |
| USER3      |
| USER4      |
+------------+

+------------+
| Block 3    |
| USER5      |
| USER6      |
+------------+


         -> storage engine reads an entire block into memory , not just single item


         -> First read happen 

            Client -> Disk -> Read block 15 -> Store block in cache  -> Return response

         -> Why cache blocks instead of individual items

              suppose block contains

                User101 
                User102
                User103

                if user requesed 102

             caching block is more efficient than caching one item at a time

             storage device naturally need contiguous chunk of data 


=> Merge result 

     Read USER#123

        │

        ▼

    MemTable
     Age = 24

        │

        ▼

    SSTable 2
    Age = 22

        │

        ▼

    SSTable 1
    Age = 20

        │

        ▼

    Choose Latest Version

        │

        ▼

    Return Age = 24


=> high level flow

 Client
   │
   ▼
AWS SDK
   │
   ▼
Front-End Router
   │
   ▼
Find Partition
   │
   ▼
Choose Replica
   │
   ▼
Check MemTable
   │
   ├── Found? → Return Item
   │
   ▼
Check Block Cache
   │
   ├── Found? → Return Item
   │
   ▼
Use Bloom Filters
   │
   ▼
Read SSTables
   │
   ▼
Merge Results (if necessary)
   │
   ▼
Return Response    
"""
