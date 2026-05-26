""" 
=> Script 
    
    script = actual command your job run
    
---------------------------------------------------------------------------------

buil_job:
   stage : build
   script:
     - echo "Installing dependencies"
     - echo "Building Project"
 
 
 each - is a comand
 runs top to bottom


---------------------------------------------------------------------------------------

=> before_scripts
     
     -> command that runs before every job


before_script:
  - echo "Setup environment"

build_job:
  stage: build
  script:
    - echo "Build step"

test_job:
  stage: test
  script:
    - echo "Test step"
    

Run before_script
Then run script

---------------------------------------------------------------------------------------------------

=> after_script
     
     -> commands that run after the job finish  (no matter success or failure)

build_job:
  stage: build
  script:
    - echo "Building..."
  after_script:
    - echo "Cleaning up..."     
    
                  

"""