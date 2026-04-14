"""   
=> CQRS
    
    -> Command Query Responsibility Segregation 
    
    -> We split data into 
       
       1. Command Side(Write) -> Change state
       2. Query Side(Read)    -> Fetch data

----------------------------------------------------------------------------------------------

=> In Traditional System 
   
   Client --- API ----DB       
              |
     same model for read / write 
     
     
=> CQRS System
            → Command Service → Write DB
  Client →
            → Query Service   → Read DB     
            
  
  Different models , differnt logic , something differnt db

------------------------------------------------------------------------------------------
=> Why CQRS Exist 
     
     -> Problem with Single model 
     
       1. Write needs 
          -> validation , txns , consistency
       
       2. Read Needs 
          
          -> Fast queries , joins , aggregations , caching 
     
     -> Try to optimize both in one model = messy + slow 
     
=> CQRS slow this 
    
    1. Write side => Clean , strict, Normalized 
    2. Read side  => Denormalized , optimized 


-------------------------------------------------------------------------------------------

=> Limitations 
    
    1. Complexity Explode 
        
        -> Separate models , separate tables , separate logics 
    
    2. Data consistency Problems 
       -> Order updated 
       -> but ordersummary is not updated 
       
       called eventual consistency 
    
    3. Not good for write heavy system
        
        1 actions -> multiple writes 
    
    4. Storage cost increase 
        
        -> Because of code duplication
        
             same data stored in multiple times
    
    5. Complex updates 
        -> user name changes 
        
        -> now we have to change all user tables                                                  
"""