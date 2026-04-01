"""   => Container storage is temporary 
          -> if you run # docker run python  
          -> and then delete the container 
          -> all your database in gone 
       
       
       => Now here volume comes in 
       
          -> A Docker volume is a persistent storage managed by docker
              -> It lives outside the container filesystem 
              -> So even if container is delete or removed the data stays 
       
       
       => Example postgres without voulme 
       
        # docker run -d --name pg -e POSTGRES_PASSWORD = 1234 postgress
         
         if your docker rm -f pg  (data loss)
         
       => Example postgress with volume (Correct way ) 
       
          -> Create volume 
       
             # Docker volume create pgdata
              
          -> Now 
          
            docker run -d --name pg -e POSTGRES_DATA = 1234 -v pgdata:/var/lib/postgresql/data -p 5432:5432 postgres
            
            pgdata -> docker volume name 
            /var/lib/postgress/data -> postgres data directory insider container 
            -p expose postgress port 
            postgress - image
            -d pg -- container in detached mode
            
            Now delete container -> data stays 
            restart and stop container -> data stays 
            """
            
            
# Real backend flow  

"""

version 3.8 

services:
   db:
     image:postgres
     container_name:pg
     enviroments:
                POSTGRES_PASSWORD:1234
     ports:
         - "5432 : 5432"
     volumes:
            - pgdata:/var/lib/postgresql/data
            
volumes:
      pgdata            

""" 

""" Volume Commands 

    1. Create a volume 
        
        # docker volume create pgdata
   
    2. List all volumes 
       
        # docker volume ls  
    
    3. Inspect a volume 
       
        # docker volume inspect pgdata
        
    4. Remove a volume 
    
       # docker volume rm pgdata
        
        delete the volume permanently 
        all database inside it gone 
        
    5. Remove unused volume 
    
       # docker volume prune """ 
       
                          