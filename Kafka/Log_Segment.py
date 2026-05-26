"""" 
=> Log Segment
    
    -> A file segment  that store  a portion of message of a partition
    
    
    Partition 0:
     [segment-0] → messages 0-999
     [segment-1] → messages 1000-1999
     [segment-2] → messages 2000-2999

-------------------------------------------------------------------------------------------------

-> Why kafka use log segment 
    
    1. Efficient Storage management 
            
            -> Instead of one huge segment
                 kafka rotates segments after a size / time  limit     
    
    
    2. Fast deletion
         
         -> if retention policy says , delete old data 
         
            kafka can simply delete entire segment file
             
             no need to delete individual file


---------------------------------------------------------------------------------------------------

-> How segment are created 
     
     kafka create new segment when
      
      file size limit exceed(log.segment.bytes)
      
      time limit reached (log.segment.ms)


-> What inside a segment 
 
     .log → actual messages
     .index → offset lookup
     .timeindex → timestamp lookup      
                               
       Partition 0
           │
           ├── 00000000000000000000.log
           ├── 00000000000000000000.index
           │
           ├── 00000000000000001000.log
           ├── 00000000000000001000.index
           │
           └── 00000000000000002000.log                         
                                



"""