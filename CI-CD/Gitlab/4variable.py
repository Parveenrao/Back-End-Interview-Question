""" 
=> Variable 
   -> Reusable values
   
   -> instead of writing same thing again and again  , store it once 
   
variables:
  APP_name  : "my-app"

build_job:
   stage:build
   script:
      - echo "$APP_NAME"


-----------------------------------------------------------------------------------------------------

=> Types of Variables 
     
   1. Global variable
           
           -> Defined at the top level
           -> availabe in all job 
     
     
     variables:
        APP_NAME: "my-app"
        VERSION: "1.0"

     build_job:
      stage: build
      script:
         - echo $APP_NAME $VERSION     
   
   2. Job level variables 
        
        -> Defined inside a specific job 
        -> Availabe only for that job 
                   
                   build_job:
                       stage: build
                    variables:
                       ENV: "production"
                       script:
                        - echo $ENV       
                        
                     Other jobs cannot access this
    
    3. Important 
         
         job level variables override the global variables
         
         variables:
            ENV: "dev"

              build_job:
                 stage: build
                  variables:
                   ENV: "prod"
                    script:
                    - echo $ENV   # prints prod                               

"""