""" 

=> Context Switching
  
     -> Process of saving the current state of running process/thread and laoding the state of another process/thread
     
       so that cpu can switch execution
       
      -> Working
        
          1. Process A is running
          2. A timer interrupt happens (A wait for I/O)
          3. Os pause a
          4. Os saves state A
          5. OS load process B' state
          6. CPU start running B
       
       
       -> Example 
           
           -> Suppose we have Chrome , vs code , Music Player 
           
           -> What actually happens 
           
              Chrome ->  Vs Code -> Music -> Chrome -> Vs code
              
              os switch very fast     


"""