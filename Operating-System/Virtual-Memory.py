""" 
=> Virutal Memory
   
   virtual memory = illusion 
   
   -> The operating system makes each program think that it has own large contiguos memory , even if physicall RAM is limited
   
------------------------------------------------------------------------------------------------------------------------------

=> Why we need it
    
    -> Ram is limited , but program often need more memory then what physically available
        
        so program use disk space as extra memory

=> How it works
   
   -> Instead of giving direct access to RAM
   
   -> Each program gets a virtual address space
   
   -> The OS + hardware(MMU) map virtual address -> physical address

============================================================================================================================

=> Paging 
    
    -> Paging is a memory management technique where
    
       1. Virtual memory is divided into fixed size pages
       
       2. Physical memory RAM divided into frames
    
    
    -> Pages(Virtual Memory)
        
        1. Fixed size (usually 4KB)
        2. Belong to process
    
    
    -> Frames (Physicall Memory)
        
        1. Same size as page
        2. Located in RAM
 

=> Page Table
    
    -> For every process 
       
       1. Os maintain page table
       
       2. IT store 
          
          which page is in which frame
          
          or if it in frame


=> How address Translation works
   
   1. When a program accesses memory
   
   2. CPU generate virtual address
   
   3. Virtual address split into 
        
        1. pages 
        2. offset
   
   4. OS use page number to look into page table
   
   5. Find corresponding frame number
   
   6. Combine frame + offset  -> physical address


=> Page Fault 
     
     1. When page is not found in RAM , called page fault
     
     2. OS pause program
     
     3. Load required page from disk(swap)
     
     4. update page table
     
     5. Resume program
     
     Swap in / Swap out
     Swap out → move page from RAM → disk                                             

=======================================================================================================================

=> Thrashing 
    
    -> Thrashing happens when system spend more time in swapping page in/ out of disk than executing program   
    
    -> CPU is idle 
    
    -> Disk swap overloaded
    -> system feel frozen

=> How Thrashing happens
   
   1. We run multiple process / large program
   
   2. Ram is not enough 
   
   3. Os start paging + swapping 
   
   4. page fault increase 
   
   5. each page fault -> disk access , slow
   
   6. System spend more time
       
       swapping page
       
       not doing useful works

=> Low memory = high page fault

=> Enough memory → low page faults


# huge memory usage
arr = [i for i in range(10**9)]

RAM fills
Swap starts heavily
Disk goes crazy
System hangs              


"""