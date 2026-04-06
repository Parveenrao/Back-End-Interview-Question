""" 
=> Internal Architecture
    
    Async Code 
       |
    Event Loop
       |
    OS I/O  Multiplexing (epool / Kqueue / select)
       |
    Network Disk 

--------------------------------------------------------------------------------------------

1. Event Loop 

    -> Scheduler that run task 
    
    -> Run task , pause them  , resume them  , message I/O
    
    -> One worker == many task , switch between them smartly
    
  asyncio.run()
  
  1. Creat event loop 
  2. Add couroutine task 
  3. Run unitl await 
  4. Pause task 
  5. Run other task 
  6. Resume when ready
  
  await asyncio.sleep(2) 
  
  Task says "I need 2 second"
  Event loop stores it 
  Moves to another task 
  Timer Complete
  Event loop assume it 
  
  
  A. Ready Queue
      
      -> Task Ready to run 
  
  B. Waiting Queue
      
      -> Task waiting for  I/O , timer 
  
  c. Selector 
      
      -> Talk to os 
      
      Tell me when something is ready      
              
"""