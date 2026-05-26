"""  
=> Segment 
     
     -> A segment is a acutal physical storage unit inside a shard 
     
     -> Shard logical container 
     -> Segment = Real life / disk 
  
  -> Each shard is made of multiple segments

Index
 └── Shard
      ├── Segment 1
      ├── Segment 2
      ├── Segment 3

-----------------------------------------------------------------------------

=> what inside a segment 
   
   1. inverted index (for search)
   2. Stored fields (original json)
   3. Term dictionary
   4. Posting list 
  
  
  -> A segment is immutable (cannot change)

-------------------------------------------------------------------------------

=> Why segment exist 

    -> Writing directly disk is slow 
    
    -> Elastic search use
       
       in memory -buffer
       
       then writes to disk as new segment 

---------------------------------------------------------------------

=> Data Flows 
    
    1. When you insert a document 
    2. Document comes in 
    3. Stored in in-memory-buffer 
    4. after a trigger -> written as new segment 
   
   Process called Refersh                      
"""