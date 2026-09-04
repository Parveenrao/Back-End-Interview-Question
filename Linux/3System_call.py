""" 

=> System Call

    -> System call is a mechanism that allows a user-space application to request a service 
       from the operating system kernel 

    -> A system call is made by program  to the operating system to perform 
       privileged operation

       Since application cannot directly access hardware , they ask the kernel to do it 
       for them using system call


=> WHy do we need system calls 

    1. Suppose python program wants to open a file 

    2. can python directly read from SSD -> No

    3. Python run in user space 

    4. Only kernel can access storage devices

    5. So python ask kernel 
       
        -> Open the file and read its content

        -> This request is called system call


=> What operation Require System call

    1. File operation 

        -> open()
        -> read()
        -> write()
        -> close()
      
      kernel performs 

      Read ssd
      write sdd
      check permission

    2. Process management 

       -> kernel create new process

    3. Memory management 

       -> ALlocating memory 

    4. Networking 

       -> Kernel create a socket 

    5. Keyboard input

        -> Kernel read keyboard input 

    6. Display output 

        -> print("hello")               


"""