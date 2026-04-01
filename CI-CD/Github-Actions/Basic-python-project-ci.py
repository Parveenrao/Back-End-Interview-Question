"""  
=> Goal 
  1. When u push code
  2. Install dependencies
  3. Run test
  4. Fail if something breaks
"""

"""   
=> Python CI YAML FIle 
  
  
name : Python-CI

on:
  push:
    branches:[main]
  
  pull_request:

jobs:
    test:
        
        runs-on : unbuntu-latest
        
        steps:
          -name : Checkout Code
           uses : action/cheackout@v4
           
           -name : Setup Python
            uses : actions/setup-python@v5
            with:
                    python-version: '3.10'
            
           -name : Install dependencies
            uses : pip install -r requirements.txt 
            
           -name : Run  tests
            uses : pytest


->    uses: actions/setup-python@v5

        -> Action from GitHub

            Installs Python in runner

            Sets PATH            

"""