"""  
=> Matrix Builds
    -> Return the same job multiple times with different configurations
    
---------------------------------------------------------------------------------------

=> Why do we Need it 
   
   -> Python Project runs different python version
   -> Different os 
   -> Different environments
   
 -> instead of writing many jobs manually , use matrix builds      


"""

"""   
name : Python-MatrixCI

on :[push]

jobs:
  test:
    runs-on: ubuntu-latest
      
    strategy:
      matrix:
        python-version : [3.9 , 3.10 , 3.11]
    
    steps:
      -uses : actions/checlout@v4
      
      -uses : actions/setup-python@v5
       with:
         python-version: ${{matrix.python-version}}
       
       -run : pip install -r requirements.txt 
       -run : pytest 
          

1.  ${{matrix.python-version}} 
      
      -> dynamically change per job 

2. if one fail , whole workflow fails 
    
    3.9 right 
    3.10 fails 
    3.11 right 
    
    final result = fail 

-------------------------------------------------------------------------------------------------

=> Advance matrix 
   
   strategy:
     matrix:
       os : [ubuntu-latest , windows-latest]
       
       python-version : [3.9 , 3.10]
       
   -> This creates 
             ubuntu + 3.9
             ubuntu + 3.10
             windows + 3.9
             windows + 3.10     
        
        -> more combination ==== more cost                        
          



"""