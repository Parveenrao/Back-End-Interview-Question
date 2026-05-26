""" 
=> Compresssion 
     
     -> In MongoDb compression is handled inside storage engine , WiredTiger
     
     -> It compress data before writing to disk and sometime in memory structure


-----------------------------------------------------------------------------------------------------

=> Why Compression Exist
    
    1. More disk usage
    2. More disk I/O
    3. SLower read / write
 
 
 WIth compression 
    
    -> Less data written to disk 
    -> Faster I/O 
    

-------------------------------------------------------------------------------------------------------

=> Where Cache Happens
   
   1. On Disk (Primary use) 
      
      Data is stored in compressed form in .wt files
      
      When reading 
      
      Data is decompressed 
      Returned to query engine
   
   
   2. IN Cache (Partially)
      
      -> WiredTiger may compress page 
         
         fit more data in Ram 
         improve cache efficiency

-----------------------------------------------------------------------------------------------------------

-> Compression Algorithms 
   
   1. Snappy
      
      -> Fast compression 
      -> Fast decompression
      -> Moderate compression ratio
   
   
   2. ZLib
       
       -> Higher compression 
       
       -> SLower 
       
       -> Best for 
           
           storage optimization 
           
           less frequent access
   
   3. Zstd 
       
       -> Better compression than Snappy
       -> Faster than Zlib
       
       Best modern choice

------------------------------------------------------------------------------------------------------

=> When Compression Hurt 
    
    1. CPU bound system
        
        if CPu is already high 
        
        compresssion add overhead 
    
    2. Very small document
    
    
    3. Real time ultra-l0w latency system 
        
        -> Decompresssion add slight delay                                               


"""