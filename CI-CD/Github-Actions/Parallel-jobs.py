"""  
=> Parallel Jobs 
   
   -> Run multiple things at the same time
   
   -> Each job runs independently unless you control

---------------------------------------------------------------------------------------------

jobs:
  tests:
    runs-on: ubuntu-latest
    
    steps:
       uses : action/checkout@v4
       run :  echo "Running tests ...."
    
    lint:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - run: echo "Linting code..."

    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - run: echo "Building app..."      
 
-> All 3 runs at the same time 

-----------------------------------------------------------------------------------

=> Control with need
   
   -> You don't want to deploy is test fails 


jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Tests"

  build:
    runs-on: ubuntu-latest
    needs: test   # runs AFTER test
    steps:
      - run: echo "Build"

  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - run: echo "Deploy"

---------------------------------------------------------------------------------

jobs:
  test:
    runs-on: ubuntu-latest

  lint:
    runs-on: ubuntu-latest

  security:
    runs-on: ubuntu-latest

  build:
    needs: [test, lint, security]
    runs-on: ubuntu-latest

  deploy:
    needs: build
    runs-on: ubuntu-latest      
                 
"""