""" 
=> Case Statment 
    
    -> Cleaner alternative way to if-else
     
     -> Syntax
               
               case $variable in
                pattern1)
                 commands
                  ;;
                pattern2)
                 commands
                  ;;
                     *)
                default command
                ;;
               esac
     
     -> Example 
        
        read -p "Enter Option" opt
        
        case $opt in 
            start)
              echo "Starting device"
            
            ;;
            
            stop)
              echo "Stopping Device"
              
              ;;
            
            Resume)
               
               echo "Restarting Device"
               
               ;;
            *)
             
             echo "Invalid Option"
               ;;
        esac              


"""