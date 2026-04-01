"""  
name: My First Workflow

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Print message
        run: echo "Hello GitHub Actions"
        
        

1. Name 
   -> basic name , helps indentify workflow

2. On 
    -> Trigger pipeline 
    -> define when workflow runs
    
    like trigger on push , only if pushed on main     
    
    
    -> variations  on: [push, pull_request]

3. Jobs 
    
   -> main execution unit
   -> A workflow can have multiple jobs   
   
   -> job is independent task
   
   -> can run parallel or sequential 
 
4. build 
    
    -> Name given to jobs , you can name any , like , test , deploy

5. runs-on 
    
    -> where it runs 
    
    -> github provide a machine 

6. steps 
    
    -> Sequention of steps
    
    1. checkout code
       
       pull you repo into runner
    
    2. actions/checoutv4
         
         -> “Use a pre-built action to download my repository code into the runner”
    
    
    
    When your workflow starts:

    GitHub gives you a fresh empty machine

    Your code is NOT there
    Your files are NOT accessible                           
"""