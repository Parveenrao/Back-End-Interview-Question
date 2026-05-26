"""
=> Translog 
     
     -> Transaction log (write-ahead log for durability)
     
     -> It ensure  , data is lost even if ElasticSearch crash
---------------------------------------------------------------------------------------------------

=> Why Transaction Log Exist 
     
     Refersh -> Make data searchable 
      
      But refersh does not gurantee data is saved safely on disk

----------------------------------------------------------------------------------------------------

=> Solution Translog 
     
     when you index a document 
     
     1. Document -> in-memory buffer 
     2. Document -> Trans log (Written to disk immedaitely)

---------------------------------------------------------------------------------------------------

=> Write Flow 
        
        Client → Index API
                 ↓
        In-memory buffer (for search later)
                 ↓
        Translog (for safety)
                 ↓
        ACK sent to client ✅
                 ↓
        Refresh (later → searchable)
                 ↓
        Flush (later → permanent storage)  

--------------------------------------------------------------------------------------------------------

=> Crash happen 
    
     1. You insert a document 
     2. it goes to trans log 
     3. Refersh has'nt happened yet 
     4. Node crashes
   
   On restart 
   
    1. ElasticSearch reads translog 
    2. Replay operation
    3. Recover data 
    

=> Replay 
  
  Trans log
  [index doc 1]
  [index doc 2]
  [index doc 3]
  
  
  => Trans Log is not forever 
      
      -> it grow continuosly
    
    -> It use Flush 

-------------------------------------------------------------------------------------

=> Flush 
    
    -> clear translog + persist data into segments
    
    After flush 
    
       -> Translog is trimmed / reset 
       -> Data is safely in segments 
     
     Flush = make data permanent   
                                    

"""