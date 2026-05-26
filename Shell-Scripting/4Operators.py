""" 
=> Operators In Scripting

   1. Numeric Integer Operator 
      
      -> Used inside [] for numbers  like -ge , gt , -le , -ne
   
   
   2. String Operator 
       
       =  => equal 
       
       != => not equal
       
       -z => string is empty
       
       -n => string is not empty
         
     -> Example 
          
          read -p 'Enter your name" name 
          
          if [ "$name" = "Parveen"]
          then echo "Match"
          fi
   
   3. File operator 
       
       if => file exist
       
       -d => directory exist
       
       -e => exist(file / dir)
       
       -r => readable 
       
       -w => Writable
       
       -x => executable
                           
                           if [ -f "test.txt" ]; then
                           echo "File exists"
                           fi              

    
   4. Logical Operator 
       
       AND(&&)
       
                        if [ $x -gt 5 ] && [ $x -lt 20 ]; then
                        echo "Between 5 and 20"
                        fi 
       
       OR (||)           
              
              if [ $x -lt 5 ] || [ $x -gt 20 ]; then
              echo "Out of range"
              fi    
   
   5. Aithmetic Operator 
        
        x = 5 
        y = 3
        
        sum = $(x + y)
        
        echo $sum              

"""