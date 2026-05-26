"""
=> In Real 
    
    -> You don't write CI/CD logic 10 times 
    -> You create one standard pipeline and reuse it everywhere 

--------------------------------------------------------------------------

=> Without Reusable Workflow 
    
    1. Copy-Paste everywhere 
    2. Hard to maintain

---------------------------------------------------------------------------------
# .github/workflows/reusable-build.yml

name : Reusable Build 

on:
  workflow_call:
    inputs:
      node-version:
         required : True 
         type : string

jobs:
  build:
    runs-on : ubuntu-latest
    
    steps:
       -uses: action/checkout@v4
       
       -name : Setup-Node
        uses : actions/setup-Node@v4
        with:
          node-version: ${{ inputs.node-version }}  
        
        
        - name: Install & Build
          run: |
          npm install
          npm run build         
    

----------------------------------------------------------------------------
# caller workflow 

# .github/workflows/main.yml

name: Main CI

on: [push]

jobs:
  call-reusable:
    uses: ./.github/workflows/reusable-build.yml
    with:
      node-version: "18"    

"""