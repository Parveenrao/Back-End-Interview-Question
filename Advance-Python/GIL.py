""" 
=> Global Interpreter Lock 
    
    -> GIL is a mutex in CPython that ensure only one thread execute python bytecode at a time per process
    
    -> Multiple thread modifying object ref counting -> Race conditions -> memory corrupt
    
------------------------------------------------------------------------------------------------------------------

=> GIl is not for API calls , I/O taks File 

=> GIL is for CPU bound task

-------------------------------------------------------------------------------------------------------------------

=> What actually happens 
    
    1. When we run a .py file in CPython:
       
       .py file -> Compiled -> bytecode (.pyc) -> Executed by python vm
       
       .pyc is a compiled file 
       stored in _pycache_
       
       GIL  occur during execution time 
           

"""