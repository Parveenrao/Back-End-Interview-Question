""" 

=> Linux Kernel 

    -> The Linux kernel is the core program of the operating system 

    -> It loaded into memory when the computer starts and remain running until the computer shut down

    -> Think of it as bridge between hardware and application 

        Application -> System call -> Linux kernel -> Hardware 


=> Why do we Need kernel 

   1. Imagine there is no kernel 
   
   2. Three program are running 

      -> Chrome 
      -> Vs code 
      -> Python 

      All try to use CPU at the same time 

      what happens 

        -> who gets the cpu time 
        -> who gets the memory 
        -> who can use the disk 
        
        -> Without kernel , every program compete directly for hardware , causing crashes and 

           corruption

           kernel acts a controller



"""