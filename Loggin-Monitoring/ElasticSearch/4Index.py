""" 
=> Refersh 
    
    -> Making new indexed documents searchable 
  
  -> When you add a document 
     
     1. It first goes to in-memory buffer 
     2. only after a refersh it visivle 

--------------------------------------------------------------------------------------

=> Internal Flow 
    
    Client → Index API → 
    In-memory buffer → 
    Translog (for durability) →
    (wait...) →
    Refresh →
    New segment created →
    Searchable       

--------------------------------------------------------------------------------------

=>   Refresh does NOT write to disk like commit
     It just creates a new segment from memory    

---------------------------------------------------------------------------------------
=> What exactly happens during refresh?
   Elasticsearch takes buffered documents
   Writes them into a new segment
   Opens that segment for search
   Now queries can see those docs     

---------------------------------------------------------------------------------------
=> Default Behavior
   Refresh happens every 1 second
  Only if index is being searched

   👉 Config:

    "refresh_interval": "1s"   
    
    POST /products/_doc/1?refresh=true

-----------------------------------------------------------------------------------------

=> Why not Refersh Every time 
    
    -> If we do  refersh  = True 
       
       1. crease too many segments 
       2. kill perfomance
       3. Merge segment pressure
  
  -> High write system
      
      refersh_interval = 30s
  
  -> Search heavy system 
     
     refersh_interval = 1s

----------------------------------------------------------------------------------------------

=> Why data is not immediately searchable 
    
    -> because elastic search use NRT(Near-real-time) search . Document visible only after refersh                  
     
"""