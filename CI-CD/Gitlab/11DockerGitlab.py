""" 

=> FLow 
   
   
   Developer Push code
          |
   Gitlab Pipeline Start
          |
   Build Docker image
          | 
   Run test inside container
          |
   push image to registry 
          |
   deploy to kubernetes / server

-------------------------------------------------------------------------------------------------

=> Simple Docker File 
     
     From python : 3.18
     
     WORKDIR /app
     
     COPY Requirements.txt
     
     RUn pip install requirements.txt 
     
     copy ...
     
     CMd [""start]
     


stage:
  - build 
  - test
  
  variables:
  IMAGE_NAME: registry.gitlab.com/your-username/your-project

build:
  stage : build
  
  image : docker :latest
  
  services:
   - docker : dind
  
  script:
    - docker build -t $Imagename
    - docker save $Imagename > image.tar
  
  artifacts:
     path:
       - image.tar

push:
  stage : push
  
  image : docker:latest 
  
  sevices : 
     - docker : dind
  
  script:
     
    - docker load< image.tar
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker tag $IMAGE_NAME $IMAGE_NAME:latest
    - docker push $IMAGE_NAME:latest                  
        
 
 
 -> Docker 
     
     docker : dind 
     
     Docker in docker
     
     lets gitlab runnne run docker commands
  
  -> build docker image 
      
      save it as artifact 
   
   -> push stage 
       
       loads image 
       
       pushes to gitlab container registry             

"""