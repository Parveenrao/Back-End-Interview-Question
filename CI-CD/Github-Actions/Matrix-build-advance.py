"""  
=> Advance matrix build 

 1. fail-fast 
      
      -> it does , stop all running matirx job if one fails 
      
      strategy:
        matrix:
          python-version: [3.9, 3.10, 3.11]
          
          3.9 fails , 3.10 , 3.11 stops immedaitely 
    
    -> We can control it 
        
        strategy:
          fail-fast : false
            matrix:
              python-version: [3.10 , 3.11 , 3.12]
                 
                 if 3.10 fails ,  3.11 and 3.12 still running


2. include
    -> Add extra combination to matrix 
    
            strategy:
              matrix:
                 python-version: [3.9, 3.10]

                include:
                  - python-version: 3.11
                    os: ubuntu-latest                 
                    
3. exclude 
    
    -> Remove unwanted combinations 
                   
                   strategy:
                     matrix:
                      os: [ubuntu-latest, windows-latest]
                        python-version: [3.9, 3.10]

                     exclude:
                     - os: windows-latest
                         python-version: 3.9  
                    
                    
                    ubuntu + 3.9 ✅
                    ubuntu + 3.10 ✅
                    windows + 3.10 ✅
                    windows + 3.9 ❌ (removed)     

-------------------------------------------------------------------------------


=> Full example 
 
 
 name: Advanced Matrix CI

on: [push]

jobs:
  test:
    runs-on: ${{ matrix.os }}

    strategy:
      fail-fast: false

      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: [3.9, 3.10]

        include:
          - os: ubuntu-latest
            python-version: 3.11

        exclude:
          - os: windows-latest
            python-version: 3.9

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - run: python --version                                      








"""