""" => Docker Container 

       # A docker container is runnning instances of the image 
       # If image is building --> then conatiner is the acutal running building 
    
     1. YOu can 
         a. Start it 
         b. Stop it 
         c. Run it 
         d .Restart it 
         e. Delete it 
         f. Enter inside it
     
     2. Image has only read only layers --> Container adds one writable layer on  top it 
     
     => Container Commands 
     
     1. Start Container 
     
       # docker run python 
         -> Create container and start container 
     
     2. Run in detached mode 
     
        # -> docker run -d python 
    
     3. List running container only 
     
       # Docker ps 
   
     4. List all running + stopped container s
     
       # Docker ps -a 
     
     5. Start a stop container 
     
       # Docker start python 
    
     6. Stop a running container 
     
      # Docker stop python 
      
     7. Restart container 
     
      # Docker restart python 
    
     8. Remove container 
     
       # Docker rm python 
      
       Force remove 
       
       # Docke remove rm if python 
    
     9. See logs 
     
       # Docker logs python 
       
       Live logs 
       
       # Docker logs -f python 
    
     10. Rename Container 
     
       # Docker rename old_name new_name 
    
     11. Pause and Unpause Container 
     
        # Docker pause python 
        # Docker unpause python """           
            
             
             
""" Real Backend Flow 

 -> You build as fastapi image 
 
  docker build -t fastapi-app .
  
  -> Run it 
  
  docker run -d -p 8000:8000 --name fastapi-app
  
  -> check 
  
  docker ps 
  
  -> See logs 
  
  Docker logs -f api
  
  """