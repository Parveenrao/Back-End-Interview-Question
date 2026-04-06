""" 
=> How Python Code Run Internally
        
        
        Your Code (.py)
              ↓
       Python Compiler
              ↓
       Bytecode (.pyc)
              ↓
     Python Virtual Machine (PVM)
              ↓
    Execution (Memory + Objects)



1. Compilation 
   
   -> Python is interpreted , not directly
      
      when you run , print("Hello")
      
      -> Complies to bytecode 
          
          stores in __pycache__
        
        hello.py → hello.cpython-311.pyc
    
    -> Bytecode = Low level instruction for Python VM


2. Python VM 
   
   -> Read ByteCode 
   -> Execute line by line 
   -> Manage stack & memory 

3. Stack-Based Execution 
    
    -> Python use stack machine 
        
        a = 2 + 3
        
        PUSH 2
        PUSH 3
        ADD
        STORE a
        
        Everything happens via stack operation

4. Object Model 
   
   -> Everything is object 
      
      a = 10 
      
      10 is object 
      
      create object for 10 
      a -> reference to object 
  
   
   -> Each object 
       
       1. Ref_count  
       2. Type pointer
       3. Value 
       
       implement in cpython 

5. GIL 
   
   -> ONly one thread is execute python bytecode at a time                              


"""