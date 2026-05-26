"""" 

=> AWS Region 
   
   A geographic area whera aws as data centres 
   
   -> Each region is independent 
         
         1. separate infra.
         2. separate data  
         3. seprate pricing



-----------------------------------------------------------------------------------------------------

=> Example of Region
    
    Mumbai -> ap-south1
    Singapore
    
    Naming patter      = <continent>-<direction>-<number>


----------------------------------------------------------------------------------

=> Why Region exist 
     
     1. Latency
        CLose Region = Faster response        
        
        user in india -> use mumabi region
        
        if you use us region = slower app
     
     2. Data laws
     
       some country want - data must stay inside country
     
     3. Fault isolation 
        
        if one region  fall 
        
         other still work
         
         deploy in multi region      

"""