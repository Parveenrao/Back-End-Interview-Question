"""" 
=> Transaction In MongoDB
    
    -> MongoDB normally gurantees atomicity ata single  document level
    
    -> But when you are working with  multiple documents or collections  , you need transaction to keep data
         consistent
    
-------------------------------------------------------------------------------------------------------------------

=> Imagine Booking a movie ticket
    
    1. Decrease available seats 
    
    2. Add booking records 
    
    3. Deduct money from wallet


=> MongoDB Transaction follow 
     
     1. Atomicity = all or nothing 
     2. Consistency = valid state always 
     3. Isloation = no interfare
     4. Durability = committed data is safe 
 
 
 --------------------------------------------------------------------------------------------------------------------
 
 => Important points
    
    1. txn is slower than single-documents apps
    2. Shoud be short lived
    3. Avoid large data inside txn 
            


"""