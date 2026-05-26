""" 
=> Need
   
    -> tells gitlab , this job only depends on these jobs - do not wait for  whole stage
    
    stage:
      build 
      test
    
    build_a:
      stage : build
      scripts : sleep 10 
    
    build_b:
      stage : build
      script : sleep 20 
    
    test:
       stage : test
       script: echo  "Testing.."
       
    -> test wait for build_a AND build_b
         even if it only need build_a

-----------------------------------------------------------------------------------------

=> Need 
    
    test:
     stage : test 
      needs : ["build_a"]
      script: echo "Testing..."
      
      test start right after build_a 
      doest not wait for build_b

------------------------------------------------------------------------------------------------------

=> Artifact + need
 
     
     stage:
        build
        test
    
     build:
       stage : build
       script:
         - echo "data" > file.txt
       
       artifacts:
          paths:
            - file.txt  
     
     test: 
       stage : test 
       
       needs : ["build"]
       scripts:
         -cat file.txt                

--------------------------------------------------------------------------------------------------

=> Advance parallel execution
      
      
test1:
  stage: test
  needs: ["build"]
  script: echo "Test 1"

test2:
  stage: test
  needs: ["build"]
  script: echo "Test 2"                               

"""