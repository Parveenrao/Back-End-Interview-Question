""""

=> Image Optimization 

1. Base Image
   -> From python:3.11 
   -> Size  ~ 900 mb
   
2. Better use  smalle size image 
   # From python:3.11-slim 
   -> size = 120 mb 
   
   # From python:3.11 - alpine 
     -> alpine comes with 
     -> size = 50 mb 

3. use Docker ignore (.dockerignore)

   -> Docker copies everthing from your project directoty
   
   -> Without .dockerignore it might copy 
      -> .git , tests , logs , .env

-> Create .dockerignore file 
   add these 
   -> .git , .gitignore , .env , logs 
   
   
4. Optimized layer caching 

   # bad Dockerfile 
   
    COPY ..       
    
    RUN pip install -r requirements.txt
    
 => what happens copy ..
    docker file copies everthing from project dir  -> layer 1
    
    run pip  install -r reqirements.txt  -> layer 2 
    
     -> now imagine app.py file changed      
        docker see copy .. something inside folder change 
        
      -> Docker rebuild 
      and run again requirements 
   
   # now Good docker file 
   
    Copy requirements.txt 
    RUN pip install -r requirements.txt
    
    COPY .. 
    
    
    -> Now something change in project dir 
    
    docker see 
    
    -> copy requirments.txt  -> no chnage caches used

5. use --no-cache for pip 

  -> when you run 
  
     # RUN pip install -r requirements.txt 
      
       pip does two thing 
        
        1. Downloads two package 
        2. Store a cache of dowmload packages 
        
    -> good file 
    
    RUN pip install --no-cache-dir -r requirements.txt

6. Reduce RUN layer 
  
   # each run creates a new layer 
   
   RUN apt-get update
   RUN apt.get install  -y curl 
   RUN apt-get install -y gcc                
    
  -> Good file 
  
  RUN apt-get update &&\
      apt-get install -y curl gcc && \
       rm -rf /var/lib/apt/lists/*    -> when apt files run it downloads  the package index file 

7. Run as non root user 

   -> by default container run as root user 
     
     Root has full control over container 
     
   -> create a non root user 
   
   RUN useradd -m appuser
   USER appuser

8. Only copy what you need

 COPY app/ap      



# Overall GOOD docker file 

FROM python:3.12-slim

WORKDIR /app

RUN useradd -m appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

CMD ["python", "app.py"]



























"""