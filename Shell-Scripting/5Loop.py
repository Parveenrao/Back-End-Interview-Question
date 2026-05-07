"""  
=> Loop In scripitng
   
  
  1. for loop  
   
   -> Synxtax 
      
      for i in 1 2 3 4 5
      do 
         
         echo $i
      
      done
    
    -> Range 
       
       for i in {1..5}
       do 
         echo &i
       done
    
    -> Example 
          
          for file in *.txt
           do
              echo "Processing $file"
          done  


------------------------------------------------------------------------------------------------------------

2. While loop
    
    -> used when condition control execution 
       
       x = 1
       
       while [ $ x -le 5]
          
       do  
         
          echo $x
          
          x = $((x+1))
        done
  
  => Infinite loop 
      
      monitoring scriptss
      
      servers
      
      background jobs
       
       
       while true
       
       do 
          
          echo "Running"
             
             sleep
       done

---------------------------------------------------------------------------------------------------------

=> break And Continue 
   
   1. Break stop loop 
      
      for i in {1...5}
      
      do 
          
          if [ $i -eq 3]
            
            break
           fi
        echo $i
      
      done
    
   
   2. Continue (Skip iteration)
   
      
      for i in {1..5}
      
      do 
         
         if [ $i -eq 3]
           
           continue
         
         fi
         
         echo $i
      done                                     
                            

"""