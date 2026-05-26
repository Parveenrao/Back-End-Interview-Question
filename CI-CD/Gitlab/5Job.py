""" 
=> Rules 
    
    rules = decide when a job run or not run

-----------------------------------------------------------------------

=> Without rules 
     
     1. Every job runs on every push
     2. You waste time + CI Time
     3. Accidently deploy from feature branch
     
     
     deploy_job:
        script:
        - echo "Deploying..."
        rules:
          - if: '$CI_COMMIT_BRANCH == "main"'    
          
          Runs ONLY on main branch

-------------------------------------------------------------------------------------

=> Multiple Rules
          
          job:
            script: echo "Hello"
             rules:
             - if: '$CI_COMMIT_BRANCH == "main"'
                  when: always
                   - if: '$CI_COMMIT_BRANCH == "dev"'
                    when: manual
                   - when: never          
          

           It check top to bottom 
           
           if main -> run automatically
           if dev -> manual trigger 
           
           Else never run 
  
  
  -> When keyword 
          
          
          on_success(default)  -> Run if previous stage passed
          always  -> Run even if previous failed 
          manual  ->   Run only if clicked 
          never   ->  Don't run 

-----------------------------------------------------------------------------------

=> Using Predefined Variables 
   
   rules:
      - if  : '$CI_PIPELINE_SOURCE == "push"'


=> File based Rules 
    
    -> if certain files change 
             
             job:
             script: echo "Run if code changed"
              rules:
               - changes:
                - src/**      


=> Combine condition
         
         
         rules:
  - if: '$CI_COMMIT_BRANCH == "main" && $CI_PIPELINE_SOURCE == "push"'
 
=> Skip jobs 
         
         
         rules:
         - if: '$CI_COMMIT_MESSAGE =~ /skip-ci/'
           when: never

----------------------------------------------------------------------------------------

stages:
  - build
  - deploy

build_job:
  stage: build
  script:
    - echo "Building..."
  rules:
    - if: '$CI_PIPELINE_SOURCE == "push"'

deploy_job:
  stage: deploy
  script:
    - echo "Deploying..."
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'                             
                 
"""
