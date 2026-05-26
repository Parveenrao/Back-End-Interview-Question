"""  
=> Compression 
    
    -> It compress response data before sending to client
    
    -> Example   
       
       original json = 200kb
       after compression = 20kb 

-------------------------------------------------------------------------------------

=> Why it matters 
    
    1. Withour Gzip 
       -> Large response = slow 
    
    2. With Gzip 
       
       -> Smaller response = faster 
          less network cost 
 
----------------------------------------------------------------------------------------
=> http {
    
    gzip on;

    gzip_comp_level 5;
    gzip_min_length 256;

 gzip_types
    text/plain
    text/css
    application/json
    application/javascript
    application/xml
    text/xml;

 gzip_vary on;
 
}

1. gzip on -> Enable compression 

2. gzip_comp_level 5;                   
        
        -> 1 to 9 
        
        1 -> fast 
        9 -> slow 

3. gzip_min_length 256
        
        -> Only compress respone > 256 bytes         
"""