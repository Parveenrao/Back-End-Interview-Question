""" 
=> Arguments
    
    
    $0 -> Script name 
    $1 -> First Arguments
    $3 -> Third Arguments
    
    
   -> #!/bin/bash

    echo "Script: $0"
    echo "First: $1"
    echo "Second: $2" 
           
           
           Script: ./script.sh
           First: apple
           Second: mango
   
    
    -> Print all arguements
        
        echo "$@"
    
    -> Number of Arguments 
        
        echo #@
    
    -> Loop through arguments
               
               for arg in "$@"
               do
                  echo $arg
               done                


"""