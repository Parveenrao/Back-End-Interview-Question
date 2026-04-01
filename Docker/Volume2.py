"""  version: '3.8'

services:
  db:
    image: postgres
    container_name: pg
    environment:
      POSTGRES_PASSWORD: 1234
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata: 
  

# Now we run command 

  -> Docker compose up 
  
     1. Reads your docker-compose-yaml file 
     2. Create network 
     3. Creates volumes 
     4. creates containers 
     5. start containers 
     6. if image is not present it pull --> automatically 
     
   
   -> docker compose up -d (detached mode)
   
  
    -> docker compose down 
    
     1. Stop container 
     2. Remove container 
     3. Remove default network 
     4. It doesnt remove volume by default 
     5. Your database still exist
     
   -> If you want to remove volume to 
   
       # docker compose down -v
        
         1. Containers removed
         2. Networks removed 
         3. Volumes removed                                   
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    """