"""" 
=> SED (Stream Editor)
     
     -> Read text line by line , modify it and print the result
     
     -> Sed is used mainly for 
         
         1. search & replace 
         
         2. deleting files 
         
         3. inserting text
         
         4. extracting patterns
         
         5. editing files automatically
    
    
    -> Find text that flowing through a pipe/file -> transform it
 
---------------------------------------------------------------------------------------------------------------

=> Syntax 
    
    sed 'command' text
  
  
  -> Example   
      
      sed 's/apple/mango' file.txt
      
      s -> subsitute
      
      replace first apple
      
      with mango           

----------------------------------------------------------------------------------------------------------

-> 1. Create simple file 

       cat > file.txt
       
       write in file 
        
        apple 
        banana
        apple pie
        orange 
        apple juice
   
  2. subsitute 
      
      s 'apple/mango/' file.txt
      
      only first occurrence per line change 
         
         mango
         banana
         mango pie 
         orange 
         mango juice 
   
   3. Replace all match (-g flag) 
          echo "apple apple apple" | sed 's/apple/mango/g'
          
          
          output => mango mango mango
   
   4. Sed does not modify original file 
        
        -> It print only modified input
        
        -> Original file stays same
   
   5. Modify file peramanet 
       
       sed -i 's/apple/mango/g' fruits.txt
   
   
   6. Print line number   
      
      sed -n '2p' fruits.txt
      
      output -> banana
   
   7. Print range of lines 
       
       sed -n '2 , 4p' fruits.txt
   
   8. Delete one line 
       
       sed '2d' fruits.txt
       
       delete line 2 from output 
       
   
   9. Delete range 
   
         sed '2,4d' fruits.txt
    
   10. Delete match lines 
      
      sed '/apple/d' fruits.txt
      
      deletes line containig apple
   
   11. Insert text 
           
           sed '/banana/i yellow fruit' fruits.txt
           
           Add line before
           
         output 
         
         apple 
         yellow fruit
         banana
   
   12. Add line after 
   
      sed '/banana/a sweet fruit' fruits.txt     
      
   13. Change entire line 
   
          sed '/banana/c grapes' fruits.txt                                                  
     



"""