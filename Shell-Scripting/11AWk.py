""" 
=> AWk 
    
    -> Tiny programming language for processing text line by line and column-by-column
    
    -> Example 
        
        John  21 india 
        alice 25 usa
        bob   19 uk
    
    -> Syntax 
        
        awk pattern {action}  file
    
    
    1. Print entire line 
        
        awk '{print}' data.txt 
        
        or 
        
        awl '{print $0}' data.txt
    
    2. Print first column 
       
       awk '{print $1}' data.txt 
    
    3. Print Multiple column 
        
        awk '{print $1 $2}' data.txt
    
    4. Print last column
         
         awk '{print $NF}' data.txt
    
    5. Print line number 
         
         awk '{print NR, $0}' data.txt
         
         1. john 21 number
         2. parveen
         3. bob 19 uk
    
    6. Conditional filtering 
        
        awk '$2 > 20 {print $1}' data.txt
    
    7. BEGIN BLOCK 
        
        Runs before processing 
        
        awk BEGIN {print "Start"} {print $1}
    
    8. Sum number 
        
        File:
         10
         20
         30
         
         awk '{sum+= $1} END {print sum}' nums.txt
    
    9. Average 
        
        awk '{sum+= $1} END {print sum/NR}' nums.txt
    
    10. Customer separator
        
        john , 21 , india
        
        use comma separator
        
        awk -F "," '{print $1}'
    
    12. Pattern Matching 
        
        awk '/india/ {print $1}'
          
          lines containing india
    
    13. conditions 
        
        awk '{
            if ($2 > 20)
               
               print$1
        }             
    
    14. Print specific line 
        
        awk 'NR == 2'                                    
                 


"""