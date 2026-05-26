""" 
=> Write Path in MongoDB
   
    -> When we write or insert data in mongodb , it does not straight  to disk
    
    -> It goes through pipeline managed by WiredTiger


-----------------------------------------------------------------------------------------------------

=> PipeLine FLow    

      1. Request Comes In 
          
          -> Client send request 
          -> Mongodb validate it 
          -> Assings _id  if not present
      
      
      2. Converted to BSON
          
          DOcument converted to BSON
      
      
      3. Write to WiredTiger Cache 
         
         -> Data first is write to memory
         
         -> Not directly to disk 
           
           thats why write are fast 
      
      4. Journal Logging 
           
           -> Before confirm success 
           
           -> MongoDB write operation to journal log
           
           -> If system crash , journal replayed , data recovered
           
           
           -> Write is considered safe only after journal entry (depends on write concern)
       
       5. Update Indexes 
           
           -> If index exist , mongodb update indexes 
           
           -> More index slow write
       
       6. Acknowledge Write 
          
           MongoDB sends response back
           
           
           {"acknowledged" : true}
           
           -> At this point , data is in cache + journal 
           
            -> Not necessarilly in disk
       
       7. Flush to Disk (Later)

                  WiredTiger:

                  Periodically writes data from cache → disk
                  Uses checkpointing                              


---------------------------------------------------------------------------------------------------

=> Write Concern 
     
     -> Control how safe  a write must be before success is returned
         
         {"W" : 1}
         
         only primary acknowledges 
       
       
       Stronger 
          
          {w : "majority"}
          
          majority of replica confirm
          
        Journal based 
          {j : true}
          
          wait for journal    




"""