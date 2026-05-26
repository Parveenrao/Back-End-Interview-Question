"""" 
=> Git-Rebase
   
    -> Take my work and put onto top of main branch 
    
         A---B---C  main
             \
               D---E  feature  
               
        You made branch feature from commit B.

        But meanwhile, main got a new commit C.

        Now your branch is behind.       
        
        
    -> git rebase main 
      
       1. Temporarily remove your commit D and E 
       
       2. Moves your branch to latest main (c)
       
       3. Re-apply D and E
       
             A---B---C  main
                      \
                       D'---E' feature    
                       
             D and E become new commits (D', E')
             History becomes clean and straight       
       
       4. if conflict happen 
       
          git add . 
          
          git rebase --contiue
          
          
          if you want to cancel 
          
          git --rebase abort         


"""