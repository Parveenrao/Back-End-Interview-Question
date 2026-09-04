""" 

=> Compaction 

    -> Compaction is a background process that 

        1. Merge multiple SStable 
        2. Remove duplicate version 
        3. Remove deleted version(tombstone when safe)

        4. sorts data 

        5. create fewer , large sstable

        6. It runs automatically 

        7. Application never trigger it 

    -> Example 

       1. Suppose we have three SStable

            SSTable1

             A = 10 
             B = 20 
             c = 30 

            SStable 2     

            b =25 
            d =40

            SStable 3 

            c = 35 
            e = 50


            c appear twice

            newest value shoudl win

            compaction merge everything


            New sstable 

            New SSTable

            A=10
            B=25
            C=35
            D=40
            E=50


            older sstable removed 

            SST1  , SST2 , SST3 -> SST4

=> Types of compaction 

   
   1. Minor compaction 

       Small SStables are merged 

       10Mb , 20MB , 15MB -> 45MB  

       frequent and lightweight 

   2. Major Compaction 

      -> ALmost all SStable are merged

        500 sstable -> 20 Large sstable    

        

=> complete flow 


          Write Request
               │
               ▼
        Write Ahead Log (WAL)
               │
               ▼
         MemTable (RAM)
               │
               ▼
             Flush
               │
               ▼
             SSTable 1

           More Writes
               │
               ▼
            SSTable 2

           More Writes
               │
               ▼
            SSTable 3

           More Writes
               │
               ▼
            SSTable 4

        Background Compaction
               │
               ▼
         Merge SSTables
               │
               ▼
        Remove Duplicate Versions
               │
               ▼
      Remove Expired Tombstones
               │
               ▼
     Create Larger Sorted SSTables
               │
               ▼
        Delete Old SSTables
               │
               ▼
     Faster Reads + Lower Storage Usage
"""