""" 
=> Oplog Internal 
    
    -> Operation log 
    
    -> Special capped collection that records every write on primary 
    
    1. CLient write to primary 
    
    2. Primary write 
        
        actual data in oplog
    
    3. Secondary 
         
         continue tail the oplog 
         
         replay operation 
     
     Called Log-based Replication

---------------------------------------------------------------------------------------------------------

=> Structure of Oplog
          {
          " ts": Timestamp(1710000000, 1),
            "op": "i",
            "ns": "db.users",
            "o": { "_id": 1, "name": "Parveen" }
         }                      

       
       ts(timestamp) -> Odering of timestamp 
       op (operation type)
          
          i -> insert 
          u = update 
          d = delete 
          c = command
       
       ns(namespace) = db.collection
       
       o(object)  = (actual data)  
    
    
    => MongoDB replication 
        
        1. Not copying full data 
        
        2. Its replaying operation 

-------------------------------------------------------------------------------------------------------

=> WHy Oplog is capped
    
    fixed size 10Gb 
    older entries get overwritten automatically


=> Oplog window 
   
   Time span covered by oplog
   
   covers last 24 hours
   
   
   if secondary is down for 2 days 
   
   oplog has only 1 day history 
   
   it cannot catchup  
                    

"""