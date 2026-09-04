""" 

=> User space And Kernel Space 

    1. User space = Employee working in office 
    2. kernel space = The CEO and management with full authority

    -> Employee cannot directly open the company vault and change company policy
       They must request management

    -> Similary application cannot directly access hardware , they must ask the kernel



 => User space 

    -> User space is where normal application execute

    -> Example 

       1. Chrome 
       2. Vs code
       3. Python programs 
       4. Games

    -> Application in user space have limited privileges

    -> They cannot 

      1. Access hardware directly
      2. Read another process memory 
      3. Execute privileged CPU instruction
      4. Modify kernel memory


=> Kernel Space 

   -> Kernel space is where operating system kernel runs

   -> The kernel has complete control over the machine

   -> It can 

      1. Access all memory 
      2. Access all hardware 
      3. Schedule cpu time 
      4. Create and destroy process 
      5. Manage virutal memory 
      6. Handle interrupts
      7. Communicate with device driver 


 => Why They are Separated 

    -> Imagine if every application could write directly to disk and ram

    -> One buggy program 

       1. Crash the os 
       2. Delete system files 
       3. Read passwords 
       4. Corrupt memory used by other program     



"""