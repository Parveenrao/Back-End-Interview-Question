"""
=> Artifacts
    -> File Generated in one job ,that you want to use later 
    
    -> Each jobs run on fresh runner 
    
    -> So file are not shared between jobs
  
  
  JOB A -> File createed
  
  JOB B -> Cannot seee file 
  
------------------------------------------------------------------------------

=> Artifacts Can be 
   
   1. Build files 
   2. Test reports 
   3. Logs 
   4. Ml models 
   5. Coverage reports 

----------------------------------------------------------------------------------

Job 1 → create files → upload artifact → GitHub storage
Job 2 → download artifact → use files       

"""


"""  
name : Artifact Pipeline 

on : [push]

jobs:
  build:
    runs-on : ubuntu-latest
    
    steps:
      - uses : actions/checkout@v4
      
      -name : Create File 
       run : |
             
             mkdir output 
             echo  "hello world" > output/file.txt  
     
     -name : Upload artifact 
      uses : actions/upload-artifact@v4
      with : 
        name : my-files 
        path : output /
  
  
  
  test:
    runs-on: ubuntu-latest
    needs: build   # 👈 important

    steps:
      - uses: actions/checkout@v4

      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: my-files

      - name: Show file
        run: cat output/file.txt


-> Need :  build          
    
    Run test  job after build 


What happens step-by-step
    build job runs
    Creates file
    Uploads artifact
    GitHub stores it

   test job starts
   Downloads artifact
   Uses file      


=>   Storage & Limits

        On GitHub:

        Stored in GitHub cloud
        Default retention: ~90 days
        Size limits apply               


"""