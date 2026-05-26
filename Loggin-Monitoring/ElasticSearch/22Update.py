""" 
=> Update in Elastic-Search 
    
    -> Elastic search  does not update document in place
    
    -> It perform
        
        Read -> Modify -> reindex cycle 


---------------------------------------------------------------------------------------

=> Flow 
   
   1. Fetch document from index 
   2. Apply changes
   3. mark old as deleted 
   4. Index new version of doc
   
   
   update  = delete + reindex

=> Why 
   
   -> Becase Elastic search built on Lucence
      
      -> NO immutable segmetns 
   
   -> So every update creates 
      
      1. New version of doc 
      2. Old one mark deleted (cleaned later via merge)

=> Implification 
   
   -> Update frequently 
       
       1. Index sixe grows 
       2. performance impact(segment merge)
       3.Write heavy system need tuning
       

=> Translog 
   
   -> Every update 
       
       1. Written to memory 
       2. Logged in translog
       
    Ensure durability before segment flush
 
=> Segment Merge  
    
    -> When many updates happen 
    -> Old one mark deleted 
    -> background merge remove them
    
    heavy update = heavy merge 


------------------------------------------------------------------------------------------------------------

=> High Update Rate 
    
    -> Same document update frequently
    
    -> Why this is bad 
       
       1. Beacuse every update 
           
           read + delete + reindex 
       
       2. So if you update  1000 times/sec 
          
          1000 new doc created 
          1000 old doc deleted 
          heavy segment merge pressure
        
         -> CPU spike 
         -> disk I/O  high
         -> latency increase 
    
    
    -> Use Parital Index 
        
        Update only some field not whole document
        
        -> But es still read full doc , modify it , reindex full doc
        
        -> It saves you network + payload size
    
    
    -> Scipted Update 
       
       Update using logic inside elastic search                                                    
        

"""