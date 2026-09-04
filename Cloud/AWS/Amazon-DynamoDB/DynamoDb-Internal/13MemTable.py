""" 

=> MemTable 

    -> Memtable is an In-Memory , sorted data structure that temporarily store recent write before 

       they are written to disk an SST table

    -> Write buffer 

    -> Instead of writing every request directly to disk. DynamoDB stores it in memory first

=> Why do we Need MemTable 

   1. Suppose users are writing data continuously 

      Write 1 -> Write 2 -> Write 3 -> Write 4 -> Write 5

      if every write goes to disk, which are inefficient

   2. Instead 


      Writes -> MemTable(RAM) -> When full -> One large sequential write to disk

=> Where Does MemTable Fit 

   CLient -> Write Ahead Log(Durable) -> MemTable (RAM)  -> Immutable Memtable -> SSTable (DISK) -> Compaction

=> What happen when the MemTable Become full

   -> Suppose memtable reaches its configured size limit

   -> it is frozen

       Immutable Memtable

       No new write are allowed into it

    -> A new empty Memtable is created immediately


=> Why is the MemTable important?

      Very fast writes because updates occur in RAM.
      Sorted data ready to be flushed to disk.
      Efficient batch writes instead of many small disk writes.
      Low write amplification by accumulating writes before flushing.    


=> Complete write flow 

            Client
              │
              ▼
     Write-Ahead Log (durability)
              │
              ▼
     MemTable (sorted, in RAM)
              │
              ▼
     MemTable becomes full
              │
              ▼
      Immutable MemTable
              │
              ▼
        Sequential flush
              │
              ▼
        SSTable on disk
              │
              ▼
     Compaction merges SSTables over time

"""