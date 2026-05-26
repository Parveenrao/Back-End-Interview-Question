"""     
=> INT VS BIGINT 
  
  
========================================================================================================

1. INT 
    
    -> Smaller range
    
    
    Type	Storage	              Signed Range	                                 Unsigned Range
     
     INT	  4 bytes	          -   2B to +2B	                                   0 to ~4B
    BIGINT	  8 bytes	          very large (~±9 quintillion)	                 0 to ~18 quintillion  
    

   
   -> WHen to use int 
       
       1. Small to medium dataset
       2. ID's won't exceed to billions
       3. Memory efficieny matter
   
   
   -> When to BIGINT 
        
       1. Large-scale system 
       2. High traffic (millions of insert/day)
       3. Distributed  system(ID generation)    
       
    CREATE TABLE users (
    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
     );   


------------------------------------------------------------------------------------------------------------

=> FLoat vs Double 
    
    1. Float 
       
       -> Lower precision
       
       float === 4 bytes = 7 digits 
       double = 8 bytes  = 15-16 digits
   
   
   -> Use float when 
       1. We dont want exact precision
       2. small memory
       3. sesor values 
    
    -> Use double when 
    
        1. Need more precision than
        
        2. Geo location position


---------------------------------------------------------------------------------------------------

=> Decimal 
    
    -> Decimal store exact numeric value (no rounding errors)
       
       DECIMAL(M , D)
       
       m = total digit
       d= digit after decimal               

"""