"""" 
=> Function
    
    -> Block of code u can reuse
    
    -> Syntx 
         
         my_functiom() {
             
             echo "Hello"
         }

        my_function()   , call it 
    
    -> Passing arguments
        
        greet(){
            
            echo "Hello $1"         $1 , $1 arguments
            
        }  
        
        greet Parveen  

    -> Example add numbers
        
        add() {
            
            sum = $(($1 + $2))
            
            echo $sum
        }
        
        result = $(add 5 3)
        
        echo 'Result : $result"
    
    
    -> Local Variables 
         
         -> Prevent variable leaking
                 
                 my_func() {
                       local x=10
                      echo $x
                     }    
    
    
    -> Function + loop 
                    my_function() {
                        
                        for i in {1..5}
                        
                        do  
                          
                          echo $1
                        done  
                    }                 
                   
                   my_function

"""