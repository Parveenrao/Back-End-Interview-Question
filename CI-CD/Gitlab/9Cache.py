""" 
=> Cache 
    
    -> Re-use file across pipeline/jobs to avoid re-downloading/re-building
    
----------------------------------------------------------------------------------------------------------

-> Problem without Cache

   job:
     script: pip install 
     
     -> every pipeline  download everything again 

-----------------------------------------------------------------------------------------------------------

=> Cache 
   
   cache:
      paths:
       - node_modules/
  
   job:
     script: - npm install

---------------------------------------------------------------------------------------------------------

=> Important Fields in Path 
   
   1. Path 
      cache:
        paths:
       - node_module
        - .venv
   
   2. key 
     -> control cache key uniqueness
     
     cache:
      key : my_cache:
       
       paths:
        - pip install
        
        
        key - same , cache resued
        differnt key - new cache created
   
   3. smart technique
         
         cache:
          key: ${CI_COMMIT_REF_SLUG}
          paths:
           -   node_modules/          
        
        differnt branch different cache 
   
   4. use lock 
           
           
           cache:
             key:
              files:
                 - package-lock.json
                paths:
                - node_modules/          
                
                Cache updates only when dependencies change
                


-----------------------------------------------------------------------------------------------------

stages:
  - build

cache:
  key:
    files:
      - package-lock.json
  paths:
    - node_modules/

build:
  stage: build
  script:
    - npm install
    - npm run build                
                            
 
"""