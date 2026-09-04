""" 

=> Log Structured Storage 


    1.Why Traditional Storage is Slow 

       -> Imagine you have a file on disk

           User 1 
           User 2 
           User 3
           User 4

         Traditional storage updates in-place


          User 1 
          Updated User 2 

          user 3 

          user 4 

        -> Problem 


           Hard Disk and SSD don't like random writes 

           updating in middle requires 

           -> Finding location 

           -> Moving disk head (HDD)

           -> rewriting blocks 

           -> Updating indexes

           Many random writes becomes expensive 


=> Better Idea 

   -> Instead of modifying old data 

   -> Never modifying anything 

   -> just append new data

      User 1 
      User 2 
      user 3
      updated user 2

      Nothing was overwritten

      Only appended

      This is called Log-Structured Storage 

    -> Reading data 

       1. Suppose we ask 


           Get(User2)

           Database sees 

           PUT user 2 
           Update user 2


           Latest entry wins

           Result -> latest entry wins


=> Why writing is fast 

   -> Disk like sequentiall writes 

   -> no jumping around 

   -> No seeking 

   -> Much faster 


=> But there is a problem 

   -> Suppose user 2 updated 100 times

   -> if dataabase reads from beginning

   -> very slow 

   -> Need to scan everything


   -> SOlution 1 . Memory Index

      Database keep an index in RAM

      User 1 -> offset 100mb

      User 2 -> offset 250MB 

      User 3 -> offset 300mb

      Now get user 2 

      Immediately jumps to
         
        250MB

=> Problem 2 

   -> After million of update 

   -> Most records are garbage 

   -> Disk become huge

   -> solution = compaction





"""