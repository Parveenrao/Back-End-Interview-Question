"""

=> Git Reflog 
  
    git reflog is a recovery command in Git that keeps track of all movements of HEAD and branch references locally. 
    It helps recover lost commits after operations like reset, rebase, or accidental branch deletion.
    
    
    For example, if I accidentally run git reset --hard and lose a commit, 
    I can use git reflog to find the old commit hash and restore it.
    
    git reset --hard d4e5f6 , it will recover lost commit 


"""