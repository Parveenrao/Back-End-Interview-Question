""" 
=> DAG
    
    -> Directed Acyclic Graph 
      
    -> instead of running job stage by stage  ,you define who depends on whhom
      
    -> Traditional job 
        
        build -> test -> deploy
        
        test wait for all build
    
    -> Dag
       
       As soon as dependencies are ready. faster

------------------------------------------------------------------------------------------------------

stage:
  - build 
  - test 
  - deploy 
  

build:
  stagge : build
  
  script : echo "Building"

test:
  stage : test
  needs : [build]
  script : echo "Testing"

lint :
  stage: test
  needs : [build]
  script : echo "Linting"

deploy:
  stage : deploy
  
  needs : [test , lint]
  
  script : echo "Deploying"                  


"""