""""    => ISR (IN-SYNC-Reply) 

         -> These are those replica which are up to date with leader 
         
         -> ISR is the set of replicas that have the same data as the leader and are safe to use.
        
        
        1. Data safety 
           -> Only isr replica are trusted
             
             if leader dies --> new leader is choosen from isr 
        
        2. Strong durability 
           
           -> acks = all
              message is considered commited if all isr replica confirms 
              
        
        
        🔹 min.insync.replicas

              Example:

               Replication factor = 3  
               min.insync.replicas = 2

               👉 At least 2 ISR replicas required to accept writes      

































"""