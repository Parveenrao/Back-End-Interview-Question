"""   
=> OutBox Pattern 
    
    -> We hvae 2 Steps 
       
       1. Save data to db 
       2. Send Event to Kafka
     
     -> If data is saved to db 
     -> Event failed
     
     
     -> Now system is incosistent , broker 
     
        Order exist in db
        but other services does not know 
    
    -> Outbox patter 
       
       'Dont send event directly , first saved in db

------------------------------------------------------------------------------------------------

=> Flow 

   Your Service
   ↓
[ DATABASE ]
   ├── Orders Table
   └── Outbox Table  ← events stored here

        ↓ (later)
   Worker reads Outbox
        ↓
   Sends to :contentReference[oaicite:0]{index=0}
   
----------------------------------------------------------------------------------------

=> Real life example 
    
    1. You write a letter(Event)
    2. put in into outbox tray
    3. Courier guy come later and deliver it
    
    
---------------------------------------------------------------------------------------------

=> Now
   
   Db txn gurantees 
   order + Event saved together     
                    



Saga → handles flow + failure
Outbox → ensures events are not lost
"""