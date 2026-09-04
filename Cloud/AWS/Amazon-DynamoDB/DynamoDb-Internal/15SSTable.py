""" 

=> WHat does an SSTable look like 


+------------------------+
| Data Block             |
+------------------------+
| Data Block             |
+------------------------+
| Data Block             |
+------------------------+
| Index Block            |
+------------------------+
| Bloom Filter           |
+------------------------+
| Metadata               |
+------------------------+



1. Data blocks 

   -> This is where actual records are stored


   Block 1

   User 1
   User 2
   User 3

   -------------------

   Block 2 

   User 4
   User 5
   User 6

   Large SStable are split into many blocks


2. Index Block

   -> Instead of scanning of entire file 

      User 1 
      user 2 

      ....


      User 1000

      THe index store 

      User 1 -> block 1

      User 2 -> block 2 

      User 3 -> Block 3

      Much faster than reading the whole file

3. Bloom Filters

   -> Before Reading as SStable , the database ask.

      Could this key possible be in this SStable

      The file is not read at all

      Bloom filter say 

      Definitely not present 

      Possible present -> then the database check sstable


4. Metadata 

   -> Store information such as 

      1. Smallest key 
      2. Largest key 
      3. Timestamp 
      4. Compression
      5. Checksum

   use for locating and validating data 


=> Complete storage flow 


                Write

                 │

                 ▼

            Write-Ahead Log

                 │

                 ▼

             MemTable

                 │

         MemTable becomes full

                 │

                 ▼

          Immutable MemTable

                 │

                 ▼

              SSTable

                 │

        Many SSTables exist

                 │

                 ▼

            Compaction

                 │

                 ▼

        Fewer, larger SSTables


"""