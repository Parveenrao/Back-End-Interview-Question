""" 

=> DyanmoDB Internal Storage Engine


              Application
                  │
                  ▼
              API Layer
                  │
                  ▼
            Request Router
                  │
                  ▼
          Partition Manager
                  │
                  ▼
             Storage Engine
                  │
                  ├── Memory Cache
                  ├── Commit Log
                  ├── SSTables
                  ├── Background Compaction
                  └── Replication

        -> Imagine a Table

           1. Suppose we create a table , Post 

           2. Primary key 

              Partition key = UserId
              Sort Key      = Timestamp


            3. Items 

                       User1   10:00   Post A
                       User1   10:05   Post B
                       User1   10:10   Post C

                       User2   09:00   Hello
                       User2   11:00   Bye    

            4. Inside One Storage Partition


                     +--------------------------------------+
                     | Memory Cache                         |
                     +--------------------------------------+

                     +--------------------------------------+
                     | Write Buffer (MemTable)              |
                     +--------------------------------------+

                     +--------------------------------------+
                     | Commit Log                           |
                     +--------------------------------------+

                      +--------------------------------------+
                      | SSTable 1                            |
                      | SSTable 2                            |
                      | SSTable 3                            |
                      +--------------------------------------+

                      +--------------------------------------+
                      | Bloom Filters                        |
                      +--------------------------------------+

                      +--------------------------------------+
                      | Background Compaction                |
                      +--------------------------------------+                    

                      

=> Step 1 , Client Sends Write 


    Client -> Storage engine

    -> Storage engine must gurantee durability

=> Step 2 , Commit Log (Write Ahead Log)

    -> First write goes here 

    -> This is an append only file 

    -> Nothing is overwritten

        Entry 1 -> Entry 2 -> Entry 3 -> Entry 4 -> Entry 5

        just keep adding 

        because appending is extremely fast 

=> Step 3 , Memtable (Write buffer)

   -> After logging 

   -> Data goes to RAM

   -> Ram is very fast 

   -> Future read can return immediately


   -> why not write directly to disk

       Hard disk and even SSD are much slower than RAM for random writes

       suppose we receive 10, 000 writes

       writing every item separately to disk would be expensive 

       Instead 

         RAM -> A B C D E F

         Accumulate many writes 

         Then flush together

         Improve throughput significantly 

=> Step 4 MemTable Gets Full

    -> Suppose buffer reaches , 64MB

    -> Now , flush to disk

    -> Disk - SSTable-001

    -> Memory become empty

    -> Ready for new writes


    -> What is SSTable 

        1. Sorted String Table 

        2. It is an immutable (read - only file)

    -> Reading Data

       Memory -> NewSStable -> olderSStable 


       Memory -> No -> SSTable 3 -> Found Return


=> Step 5 Bloom Filter     

    -> Searching Every table would be slow

    -> Imagine 100 SStable , we have to scan 100 tables 

    -> Instead , each SStable has Bloom filter , a probabilistic Data structure 

       Need user 9 -> Bloom filter -> Definitely not here -> skip ss table


    -> Bloom filters never incorrectly say "not present" when the item exists, 
      but they can occasionally say "maybe" for an item that is not actually there 
      (a false positive).   

=> Step 6. Compaction 

    -> After many flush 

        SST1
        SST2
        SST3
        SST4 
        SST5

     Reading become slower because more file must be checked

     background compaction merge them

     SST1 -> SST2 -> SST3 -> Large SST 


     During compaction 

      -> Duplicate versions are resolved 

      -> Deleted items (tombstone) can eventually be discarded after they are no longer needed

      -> fewer files remain


=> Read Cache 

   -> Frequently accessed items are cached

      Cache User 1 -> Return 1ms


=> Complete Write flow 

                  Client
                    │
                    ▼
              Request Router
                    │
                    ▼
            Correct Partition
                    │
                    ▼
               Commit Log
                    │
                    ▼
             MemTable (RAM)
                    │
                    ▼
           Acknowledgement to Client
                    │
                    ▼
                  Flush
                    │
                    ▼
                 SSTable
                    │
                    ▼
           Background Compaction

           
=> Complete Read flow 


            Client
              │
              ▼
           Partition
              │
              ▼
            Cache?
              │
              ├── Yes → Return
              │
              ▼
           MemTable?
              │
              ├── Yes → Return
              │
              ▼
         Bloom Filter
              │
              ▼
        Relevant SSTable
             │
             ▼
       Return Result

=> Key interview takeaways
     Writes are first appended to a commit log for durability.
     Recent writes are kept in an in-memory MemTable for fast access.
     When the MemTable fills, it is flushed to immutable, sorted SSTables.
     Bloom filters help skip SSTables that definitely don't contain the requested key.
     Compaction merges SSTables, removes obsolete versions, and cleans up tombstones.
     Hot items are served from memory caches whenever possible.
     Data is replicated across multiple nodes for high availability and durability.       

"""