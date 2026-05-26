"""  
=> Job 
    
    -> A job is a set of commands that gitlab run
    
    -> job = unit of work inside stage
    
    
    build_job:
       stage : build 
        script:
           - echo  "Building project"
    
    build_job -> name of job(anything)
    stage : build (which stage it belongs to)
    scripts (run command)


----------------------------------------------------------------------------------------

stages:
   build 
   test

build_job:
    stage: build
      script:
        -echo "Building projects"

test_job:
  stage : test 
    script:
      -echo "Testing Project"

---------------------------------------------------------------------------------------------

=> Multiple job in same stage

stages:
   - build

job1:
   stage: build
   script:
    - echo "job 1"

job2:
  stage : build
  scripts:
   - echo "job 2"

-> both job run in parallel

-------------------------------------------------------------------------------------------------

=> Every job have
    1. script
    2. stage

-> job name must be unique 
    

=> jobs are independent
    
    -> one job does not share data with another job  (unless u use artifact)        
                                   


"""