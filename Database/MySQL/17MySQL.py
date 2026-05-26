"""" 
=> Coalesce
      
      -> Return the first non null values from left to right
      
      ->  COALESCE(a, b, c, d)
           
           if   a is not null , return a 
           else b is not null , return b 
           else c is not null , return c 
           else return d
       
       -> SELECT COALESCE(NULL, NULL, 10, 20);
             
             null , null -> Skip 
                
                10 -> first valid , return
       
       
       -> Null vs empty 
            
            SELECT COALESCE(NULL, '', 5);
            
            return "" , because it is not null
       
       -> Replace null with default 
            
            SELECT COALESCE(age, 0) FROM users;
              
              if age is null , return 0
       
       -> Multiple Values  
               
               SELECT COALESCE(phone, email, 'No Contact') FROM users;
               
               Priority => phone , email , default text                          


"""