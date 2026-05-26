""" 
=> Semantic Version  

     -> Semantic Version is structured way to version software so people instantly understand the impact 
    
    
    -> Core Format 
         
         1.4.2   
         
         MAJOR = 1 , MINOR = 4 , PATCH = 2
       
       
       -> MAJOR 
           
           Increase when you make changes that break users
           
           - "name" 
           + "full_name"
           
           1.4.2 = 2.0.0 
        
        
        
        -> Minor (New Feature , backward compatible)
            
            Add new functionality without breaking functionality 
            
               {
                   "name": "Parveen",
                   "age": 21,
                   "email": "abc@gmail.com"   // new field
               }           
              
              1.4.2 -> 1.5.0 
        
        -> PATCH 
            
            FIx issue without changing behaviour 
              
              1.4.2 -> 1.4.3

=================================================================================================

=> Let say your are building API 
      
      v1.0.0
      
      {
          name : "Parveen"
      } 
      
    
    1. Minor (Add new field)
    
         {
             "name" : "Parveen",
             "age" : 21
         }                     
          
          v1.1.0  == old app still workd
    
    2. PATCH 
         
         v1.1.1  (fix bug)
    
    3. MAJOR 
       
       V2.0.0 
        
        {
            
            "full_name" : "Parveen kumar"
        }           
        
        old app break 
"""