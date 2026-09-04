""" 

=> Linux

     -> Most People say Linux is operating system , partially correct but not accurate

     -> Linux is the kernel , the core software the manage computers's hardware and provide 
        services to program

     -> A complete Linux operating system is called  Linux distribution combines Linux kernel 
         with utilities , libraries and shell and application 

         

=> What happen when you press power button

  
   Power button -> BIOS/UFEI -> Linux kernel -> System service -> Login screen -> Desktop or terminal



   1. Power supply 

         -> Electricity Reach

            1. CPU 
            2. RAM 
            3. SSD
            4. Motherboard 

         The CPU starts executing instructions from a predefined location in firmware 

   2. BIOS/UEFI

      -> The firmware checks

         1. Is Ram working 
         2. Is the CPU working 
         3. Is the keyboard connected 
         4. Is storage device available 

       This is called Power-on-self-test (POST) 

       if everything is okay 

       It looks for an operating system to boot

    3. Bootloader 

       -> Commonly GRUB on Linxu system is responsible for loading the linux kernel into memory

       -> It can also

           1. Show a boot menu 
           2. Let you choose betweeen operating system 
           3. Pass startup to kernel 

   4. Linux kernel starts 

       -> Kernel 

          1. Detect hardware 
          2. Load device drivers 
          3. Intializes memory management 
          4. Starts CPU scheduling 
          5. Mounts the root file system 
          6. Start the first user-space process

   5. System Services 

      -> Background services start , such as 

         1. Networking 
         2. Logging 
         3. Time synchronization 
         4. SSH server 
         5. Database server 

   6. Login 

      -> You enter 

        Username and password

        if correct -> You get access to the system                                  

"""