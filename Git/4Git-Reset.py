""" 

=> What git Reset does
   
     -> It moves things backward 
     
     
     -> affect 
     
       1. commit history 
       2. Staging area
       3. Working files
    
    -> Git Area 
        
        Working Directory -> your actual files 
        Staging area      -> git add 
        Repository        ->  commits
        
        
        
        git add app.py  
        
        git commit -m "added app'
        
        file is committed
        
        commit exist in repo 
    
    -> git reset syntax 
       
         git reset <option> <target>
   
    
    -> Three types of reset 
    
    1. --soft
       
       -> moves history back 
       
       -> keep staging
       
       git reset --soft Head~1
    
    2. mixed 
    
       
       -> git reset Head~1
       
       -> git reset --mixed HEAD~1
       
       Remove commit 
       Remove staging 
       Keep file chaging
    
    3. hard 
       
       git reset --hard HEAD~1
       
       commit 
       staging 
       local changes                   

"""