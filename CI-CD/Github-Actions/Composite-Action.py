""" 
=> Compoiste Action
    
    -> Is a way to bundle  multiple step into one reusable step 
    
    -> With composite actions 
        
        1. DRY (Do not repeat yourself)
        2. Clean pipelines
        3. Standardized logic
    
    -> Composite action lives in your repo 
    
           .github/actions/my-action/action.yml


--------------------------------------------------------------------------------------------------

1. Simpl Composite Action 


name : "Setup and Install"
description : "Install dependencies "     

inputs:
   required : True
   type : String
   
   runs:
     using : "composite"
     
     steps:
        -uses : actions/setup-python@v4
         with:
           python-version: ${{ inputs.python-version }}

    - run: pip install -r requirements.txt
      shell: bash      
      
      
=> Now use in workflow 


jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup project
        uses: ./.github/actions/my-action
        with:
          python-version: "3.11"
          

----------------------------------------------------------------------------------------------

=> Use composit action for 
  
  1. install dependencies
  2. setup environment 
  
  3. Liniting
  
  4. Test 
  
------------------------------------------------------------------------------------------------

=> composite action of docker 

runs:
  using: "composite"
  steps:
    - run: echo "Logging into Docker"
      shell: bash

    - run: docker build -t myapp .
      shell: bash

    - run: docker push myapp
      shell: bash
 
------------------------------------------------------------------------------------------------

=> Composite action of linting 
       
       .github/actions/lint/action.yml

name: "Python Lint"
description: "Run lint checks using flake8 and black"

inputs:
  python-version:
    required: true
    default: "3.11"

runs:
  using: "composite"
  steps:
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ inputs.python-version }}

    - name: Install dependencies
      run: |
        pip install flake8 black
      shell: bash

    - name: Run flake8
      run: flake8 .
      shell: bash

    - name: Check formatting (black)
      run: black --check .
      shell: bash               
  
            
                
          

"""