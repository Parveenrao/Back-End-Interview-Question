""" 
=> Kafka compression 
   
   -> Reduce message size  before sending to broker 
      
      instead or sending 
      
      100 kb -- send as 20kb , 30 kb 


------------------------------------------------------------------------------

=> Where compression happens 
   
   1. Producer Side
      
      -> Message are compressed before sending 
      
      -> Done per batach   (not per single message )
      
          Kafka compresses batches, not individual messages
   
   2. Broker side 
      
      -> Store data as - it (compressed)
         
         Does not decompress /  recompresss
   
   3.  Consumer Side

          -> Automatically decompresses       

----------------------------------------------------------------------------------------------

=> Why compression matters 
   
   1. Network Saving 
      
      less data -> faster transfer 
   
   2. Disk Saving
      
      Less storage -> Lower cost 
   
   3. Higher Throughput 
      
      More message -> per second

-------------------------------------------------------------------------------------------------

=> Compression Type in kafka 
    
    1. GZIP 
        compression.type=gzip
      
      -> High compression ratio
      
      -> Slow (CPU heavy)
    
    2. Snappy (Most common)
    
        compression.type=snappy
        
      -> Fast 
      -> balanced compression 
      
   
   3. LZ4 (Very popular)
      
      compression.type=lz4             
      
      
     -> Very fast compression & decompression
     
     -> Good ratio         
    
   4. ZSTD (Modern way) 
      
      compression.type=zstd
      
      -> Best compression + speed combo                  


"""