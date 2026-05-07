""" 
=> Decision-Making
    
    if this condition true -> do this
    
    else - do something
    
                                  if [ condition ]
                             then
                                 command
                            fi
    
    -> example 
         
         read -p "Enter your age" age
         
         if [ $age -ge 18]
         
         then 
             
             echo " You can vote
         else
             
             echo " You cannot vote
         
         fi 
    
    -> comparison operator 
        
        -eq => equal 
        -ne => not equal 
        -gt => greater than 
        -lt => less than
        -ge => greater than or equal 
        -le => less than or equal
    
    -> Multiple conditions
         
         if[ $age -ge 18 ] && [ $age -le 60]
         
         then 
            
            echo "Working Age"
         
         fi                    


"""