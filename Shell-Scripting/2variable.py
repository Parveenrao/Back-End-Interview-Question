""" 
=> Variable
    
    -> Is just a container to store value
       
       name = Parveen
       
    -> to use it add $
    
      echo $name -> Parveen   
    
    
    -> Example 
        
        in .sh file
        
        name="Parveen"
        age=21
        
        echo "My name is $name"
        echo "I am $age years old"
        
        
        echo "You are in $current_dir"
        echo "Today is $today"

    
    -> a file 
              
              
              #!/bin/bash

               read -p "Enter your name: " name
               read -p "Enter your age: " age

               echo "Your name is $name"
               echo "You are $age years old"

               current_dir=$(pwd)
               echo "You are in $current_dir"


"""