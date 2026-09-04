""" 
=> NUll VS IS NULL

  1. NULL 
  
     -> In mysql null is unknown value , does not behave like normal value 
     
     -> Null means no value , unknown , missing data 
     
     -> Null cannot be compared with = and !=
     
     -> Any comparison with unknown value , result will be unkown

     -> null is value marker for column
   
   
   2. Check for null or not null
   
       select * from users where name is Null 
       
       select * from users whrer name is not null  

       IS null is operator to check


"""