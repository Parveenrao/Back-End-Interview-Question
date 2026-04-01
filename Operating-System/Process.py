"""  Process 

=> Process is a program in execution 
  
   -> When you run a program , os create a process for it 
      
      lets say if open chrome  -> os create a process for it 
      
      if i open chrome twice then  
       -> chrome 1  --- Process 1
       -> Chrome 2  --- Process 2   
       
    Each process run independently 
    
1. What happen when a program start 

    -> Create a new process
    -> Assign a process id (PID)
    -> Allocate memory  
    -> Load program in memory 
    -> Start execution                                  Process ID: 1234
                                                        Program: python app.py

    
    
2. Process Layout         
        
+-------------------+
| Code (program)    |
+-------------------+
| Global variables  |
+-------------------+
| Heap              |
| (dynamic memory)  |
+-------------------+
| Stack             |
| (function calls)  |
+-------------------+


-> Every process has its own memory space 

->Explanation:

Code section

contains compiled instructions

Global section

global variables

Heap

dynamic memory (malloc/new)

Stack

function calls and local variables


"""