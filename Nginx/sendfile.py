"""  
=> sendfile 
    
    -> sendfile is a zero-copy optimization
        sendfile on;
        
    -> It tells NGINX
        
        Don't copy file into user space  - send it directly from disk to network space 

-------------------------------------------------------------------------------------------------

=> Without Sendfile 
    
    Disk - kernel - User space(Ngnix) - kernel -Network
    
    file is copied multiple time 
    
    CPU overhead is high 
    
    slower for larger files 

=> With sendfile
     
     Disk - kernel - Network(direct)
     
     No extra copying , Faster , less overhead 

=> What happens internally 

    Nginx Use the OS system calls 
    
     Sendfile()
     
     So nginx says , 
     
     hey OS ,  send this file directly to os
     
     Os handle everything internally

-----------------------------------------------------------------------------------------

=> What it matters 
    
    When you serve 
    
    1. Image 
    2. CSS/js
    3. Videos
    4. PDFs
    
 huge performance boost 
 
 Especially when 
 
 Huge traffic , 
 
---------------------------------------------------------------------------------------------

=> When to use sendfile on;
  
  1. Serving static file from local disk 
  
  2. High traffic static server                      
         

"""