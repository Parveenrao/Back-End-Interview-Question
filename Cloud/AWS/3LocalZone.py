""" 
=> LocalZone
    
    -> Aws service physically closer to your users  to reduce latency

-------------------------------------------------------------------------------------------

-> Why it exist 

 1. Normally
     
     User -> Aws Region(far away) -> delay
 
 2. with local zone
      
      User -> Local Zone(nearby city) -> Faster response
       
       Reduce latency (delay) significantly

-------------------------------------------------------------------------------------------------

-> Example 
    
    AWS Region -> Mumbai
    User -> Delhi
   
   without local zone -> Request go to mumbai
   with local zone(delhi) -> hanled locally


------------------------------------------------------------------------------------------------------

=> Local zone are for 
   
   Gaming 
   Video streaming
   Real time apps                   


"""