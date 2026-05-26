"""  
=> Linting
    
    -> Static code analyzer 
    
    -> Analyze code without executing it 
    
    -> Check formatting 
    -> Bad practice
    -> Potential bugs

--------------------------------------------------------------------------------

=> Without Linting 
    1. Messy code merged 
    2. Bugs slip in 

=> With Linting 
    1. Clean code enforced
    2. PRs failed if code is bad

----------------------------------------------------------------------------------

=> Popular Python Linters 
    
    1. flake8 == Style + basic erros 
    2. black  == Autoformatter
    3. isort  == Sort imports 
    4. pylint == Deep Analysis  
    
-------------------------------------------------------------------------------------

=> Workflow 

Developer → Write code
          → Run black locally
          → Push
          → CI runs flake8
          → Pass → merge
          → Fail → fix              

"""



""" 
name : Python-Lint_CI

on : [push]

jobs:
  lint:
    runs-on: ubuntu-latest
  
    steps:
      -uses : actions/checkout@v4
      
      -uses : setup-python@v5
       with:
         python-version : '3.10'
      
      -name : Install tools
       run : pip install flake8 black
       
      -name : Run flake8
       run : falke8 .  
       
      -name : Check formatting 
       run : black --check..      

"""