""" 
=> Arrrays


    1. Create array 
        
        arr = ("apple" "banana" "mango")
    
    2. Access element
        
        echo $(arr[0]) 
    
    3. Access all element 
       
       echo $(arr[@])
    
    4. Array length 
         
         echo $(#arrr[@]) 
    
    5. Add element
        
        arr+= ("Orange)
    
    6. Update element 
         
         arr[1]="grapes"
    
    
    7. Loop through Array
        
        for item in $(arr[@])
        do
           echo $item
        
        done
    
    8. Access index
         
         echo $(!arr[@]) 
    
    9. Remove element 
       
       unset arr[1]
    
    10. Rebuild
    
        arr=("${arr[@]}")     
        
    11. Read Array from user
         
         read -a arr
    
    12. SLicing 
          
          echo $(arr[@]:1:2)                                         






"""