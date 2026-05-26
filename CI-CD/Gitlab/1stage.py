"""" 
=> Stage 
    
    -> in gitlab stage define the order of execution  in your pipline
    
    stage:
       build
       test
       deploy
       
       
    -> This create pipeline 
        
        first  -> build code
        second -> test code
        third  -> deploy code   
    
    
    -> What stage do 
        
        1. They control executions(order)
        2. groub job logically
        
        3. they do not execute code 
        4. the do not run code
        5. they do not do actual work , jobs do
    
    
    -> 1. Order matter 
        
        stages:
           test
           build
           
          run test before build  
    
    -> 2. Same stage run together
            
            if multiple job are in build:
                 they run in parallel
    
    -> 3. Failur stop pipeline 
          
          if any job in stage fail 
              
              next stage will not run 
    
    -> Stage  = when should this happen
    -> job =  what   should happen                                    


"""