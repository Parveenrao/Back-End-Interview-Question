""" 
=> Stash Command 

    -> It temporarily saved unfinished work somewhere else

   
   -> Why we need it 
       
       1. let say we are working on branch feature/payment 
       
       2. suddenly someone say , fix the bug in main branch    , so we need to switch the branch
       
       3. git stash 
           
            -> git take modified files and hide them somewher else
       
       4. after working , we come back 
           
             git stash pop  , file come back
             
             
             git stash list -> show all stash
             
            -> restore but keep stash 
                
                  git stash apply 
            
            -> Names stash 
               
                git stash push -m "Payment half api done"
            
            -> to include mew files 
               
                git stash -u                 



"""