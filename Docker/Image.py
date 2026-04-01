""" IMAGE 
 
-> An image is a blueprint / template of the application 
   
   or 
   
   => A Docker is read only template  used to create containers 
     
     Image = Blueprint 
     Container = Running application made from that Blueprint 
     
     
   => Real life Analoy 
   
      Image => Building Blueprint 
      Container => Actual building constructed from that container 
   
   => What inside a Docker image 
     
     A Docker image contains 
     
     1. Base OS (Minimal Linux)
     2. Runtime (Python , Node , Java)
     3. Your application code 
     4. Dependenices 
     5. Environement variables 
     6. Startup  command 
     
   => How Images Are Created 
   
     1. Pull from Docker Hub 
     
      # Docker pull python 
      
      # Docker pull python 3.12 (Specific version)
     
     2. See downloaded images 
     
      # Docker images 
      
      # Docker image ls
    
     3. Remove image 
     
      # Docker rmi image name
      
      # Docker rmi 34fgd343 (Using image Id)
      
      Docker rmi -f python  (Force Remove)
     
     4. Build your own image 
     
       Using docker-file 
     
      # Docker build -t my_app:1.0 . 
       
       -t Tag
        .  Current directory where dockefile exist
        
     5. Push Image to Docker Hub
     
        a. First login 
          
           Docker Login 
        
        b. Docker push username / myapp:1.0
        
        Now your image is public / private on registry
     
     6. Inspect Image 
      
       # Docker Inspect python 
       
         Shows 
         
         a. Metadat 
         b. Layers 
         c. Architecture 
         
     7. Show image history 
     
       # Docker history python 
    
     8. Save Image to file 
     
       # docker save -o myimage.tar python 
       
         Used for backup 
    
     9. Load image from file 
     
       # Docker load -i myimage.tar  
    
     10. Remove unsed images 
      
       # Docker image prune 
       
       Remove all unused images 
       # Docker image prune -a"""
        
        