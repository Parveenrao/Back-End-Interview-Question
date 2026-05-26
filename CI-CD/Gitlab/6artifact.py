""" 
=> Artifact
    
    -> File created in one job used in another job 
    
    -> Without artifacts 
         
         1. every job run in fresh environment
         2. Files from previous jobs are lost
   
   
   
   build_job:
      stage : build
       script:
         - echo "hello" > file.txt 
       
       artifacts:
          paths:
            - file.txt 
   
   test_job: 
     stage : job
      script:
        - cat file.txt
 
 
 -> Work internally 
   
   Step 1 . (Build)
        
        create file 
        upload to gitlab storage 
   
   Step 2 
   
    Download artifact 
    Use it


----------------------------------------------------------------------------------

=> Important Fields
   
   1. Paths (what to save)
       
       artifacts:
          paths: 
           
           - file.txt 
           - folder /
   
   
   2. expire in     
   
      
      artifacts:
        paths:
          - file.txt  
          
         expire_in : 1 hour
   
   3. when 
        
        artifacts:
           paths: 
             - file.txt
            
            when : always       
            
        options [ on_success(default) , always (success or failure) , on_failure]                                           


"""