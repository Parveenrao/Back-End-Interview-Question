""" 
=> Segment Cleanup 
    
    Every refersh = new segment (tiny)  
       
       if one doc per second = one segment 
   
   -> Seach become slow 
      
      1. check many segments
      2. memory usuage increase 
      3. File handle increase 
      4. Disk fragmentation
   
   
   -> Solution 
      
       Segment Merging = Automatically merge small segments into bigger one

--------------------------------------------------------------------------------

=> Working 

    Segment A (10 docs)
    Segment B (15 docs)
    Segment C (20 docs)

        ↓ merge

       New Segment D (45 docs)

       Old segments deleted  

---------------------------------------------------------------------------------------

=> What happens during merge?
     1. New bigger segment is created
           Data copied + reorganized

     2. Deleted documents are removed
          (this is key — cleanup happens here)
     
     3. Old segments are deleted    


------------------------------------------------------------------------------------------

=> Delete Documents 
    
    -> When you delete a document 
         
         its not removed immedaitely(soft delete)
         
    
    -> Only during merge  
        
        actually removed from disk                  
                   

"""