"""  
=> Dependecy Caching
   
   -> Save installed dependecy  -> reuse them in next run
   
   -> Instead of install every time
   
   -> Install once -> reuse -> faster builds
   
   
   -> Solution 
      
      -> we use actions/cache from github
"""


"""   
name : Python-Ci-With-Cache

on : [push]

jobs:
    test:
       runs-on : ubuntu-latest
       
       steps:
           -name : actions/checout@v4
            
           -name : Setup Python
            uses : actions/setup-python@v5
            with :
               
               python-version : '3.10'
           
           -name : cache dependencies
            uses : actions/cache@v4
             with:
                path: ~/.cache/pip
                key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
                restore-keys: |
                ${{ runner.os }}-pip-

           - name: Install dependencies
             run: pip install -r requirements.txt

           - name: Run tests
             run: pytest
                

1.  uses: actions/cache@v4
     
     -> Enable cache system

2. path: ~/.cache/pip
    
    wher store downloaded packages

3. key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}    

     -> cache indentity 

4. restore-keys: | ${{ runner.os }}-pip-
    
    -> Fallback if cache not found


---------------------------------------------------------------------------------------------------

=> If you:

     Add 1 new dependency

      Partial cache restore (from restore keys)
      Only new package downloaded
      Cache updated    
             
                  


"""