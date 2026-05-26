""" 
=> Dependencies
    
    -> Control which job artifact should be download
    
    -> Without dependencies 
        
        a job downloads all artifact from previous stage


---------------------------------------------------------------------------------------------

stage:
  - build 
  - test

build_a:
   stage : build
   script:
     - echo "A" > a.txt 
     artifacts
      paths :["a.txt"]
      
build_b
   stage: build
    script:
      - echo "B" > b.txt 
      artifacts
        paths :["b.txt"]

test:
  stage : test 
  script:
    - ls
    
    
    -> test will get
        a.txt 
        b.txt   
        
    even if it only needs one
    
  
  
  -> Use dependencies 
      
      test:
        stage : test 
        dependencies:
          - build_a
        
        script:
         -- ls
         
         only a.txt is downloaded 
   
  -> Combine with need 
       
       test:
         stage : test 
         needs : ['build']
         dependecies:
            - build_a
            
          script:
            -cat a.txt              
                      
                
  -> Important 
     
     if u want no artifact at all 
       
       dependencies = []
       
       avoid unnecessary  downloads completely

"""