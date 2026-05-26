""" 
=> Gitlab Runners 
    
    A gitlab runner is the machine (or process) that actually executes your pipeline job
    
    -> gitlab itself does not run code , runner do
    
    GitLab (brain)
         ↓
    Runner (worker)
         ↓
    Runs your job (build/test/deploy)

-------------------------------------------------------------------------------------------------------

=> What a runner actually do 
    
    when u push code
    
    1. Gitlab CI/CD reads .gitlab-ci.ymal
    
    2. find a job
    3. send it to runner
    
    4. runner execute
        
        build
        docker commands 
        kebectl deploy
        tests

-------------------------------------------------------------------------------------------------------------

=> Types of runner
    
    
    1. Shared runners 
       
       -> provided by gitlab (default)
       
       -> Easy to use
       
       -> Limited control
    
    2. Specific runners
          
          -> Attach to specific runner 
          -> you mange them
    
    3. Group runners
        
        -> shared across multiple projects                      

"""