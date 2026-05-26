"""  
=> Buffering 
    
       -> Temporary storage of data in memory (RAM)  or disk before sending it forward 

-----------------------------------------------------------------------------------------
=> Two Types of Buffering Nginx use

   1. Response Buffering 
      
      Backend -> Nginx -> Client 
      
      -> Backend (Fastapi , Django) send response 
      
      -> Nginx store it into buffer 
      
      -> Then send it directly to client  
   
   
   2. Request Buffering 
   
       Client -> Nginx -> backend 
       
       -> Client upload data (Post , file upload)
       
       -> nginx buffers it first 
       
       -> Then send it to backend   

----------------------------------------------------------------------------------------------------------
=> Response Buffering 


      proxy_buffering on;        -> Enable buffering 
      proxy_buffer_size 16k;     -> first chunk
      proxy_buffers 8 16k;       -> number + Size of buffers 
      proxy_busy_buffers_size 32k; -> active sending buffers 


=> Request Buffering 
     -> user upload files (client -> Nginx(buffer) -> Backend)
     
     client_body_buffer_size 16k;
     client_max_body_size 10m;
     proxy_request_buffering on;
     
     
   -> What happen if Buffer exceed 
      
      If response is too big (Nginx write to disk (Temp_files))  
      
      proxy_max_temp_file_size 1024m;
      proxy_temp_path /var/lib/nginx/tmp;

-----------------------------------------------------------------------------------------------------------

=> When to turn off buffering 
   
   proxy_buffering off;
   
   -> Disable buffering when you need real time data / streaming

              
"""