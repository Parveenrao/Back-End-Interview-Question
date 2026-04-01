"""  
=> Github Actions
    -> is CI/CD tool that build inside github
    
    -> It helps you 
        
        1. Automatically test your code
        2. Automatically build and deploy apps 
        3. Run scripts when event triggered (Push , pr)

------------------------------------------------------------------------------------------
=> Core Idea 
    
    1. When something happens in repi == run auotmateed worlflow 
    
    2. Example 
        
        I push code  -> test run automatically 
        PR Created = checks run
        Merge   = deply to sever
        
------------------------------------------------------------------------------------------

=> Basic Architecture 
    
    Github Actions has 4 main parts 
    
    1. Workflow 
        
        -> A yaml file (.github/workflows/main.yml)
        -> Define automation
    
    2. Event Trigger 
        
        -> When workflow run
        
             on :[push]       
    
    3. jobs 
        
        -> A set of steps running on a machine 
    
    4. Step 
       
       -> Individual Command/scripts                          
"""