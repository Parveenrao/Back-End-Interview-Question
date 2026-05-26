"""" 

=> What is Multi-Processing 
   
      -> Running multiple process simulataneously to execute task in parallel
      
      -> Instead of one python process doing all , Python creates multiple independent process
      
      -> Each process can run of different CPU core
      
    -> Example Suppose we want to process 4 different large image 
      
        1. Without multiprocessin , image 1 -> image 2 -> image 3  
     
        2. With multiprocess , image 1 
                               image 2
                               image 3
                               image 4  // all at the same tim 
                               
                           This make CPU-heavy program much faster 

---------------------------------------------------------------------------------------------------------------

=> What is Process 
    
     -> An independent running program with its own memory and resources 
     
     -> if my computer has chrome , vs code,  spotify are all separate process
     
     
     -> In Python , script itself it one process
     
     -> Multiprocess allows your script to create more processs
     
     -> WHy Multi-Processing exist 
           
            1. Python has something called GIL
            2. So threading is not ideal for CPU-Bound task
            3. Multi-processing solve this by, each process have its own interpreter , each process has its own GIL
     
     -> Multi-PRocess is good for
        
         1. calculations
         2. image processing 
         3. simulations
         4.video rendering                                      

"""