""" 
=> API-Versioning 
     
     -> How we manage changes to an API  over time withoiut breaking existing clients. 
     
     -> In real system , APi will evolve - mew features  structures changes , Versioning ensure older apps keep working 
         while newer clients can use improvements 


--------------------------------------------------------------------------------------------------------------------------------

=> WhY Exist 
    
    -> Let say we launch api 
      
      
      GET / users /1
      
      {
          name : "parveen",
          age : 21
      }         
         
         
    later we change it to 
    
       {
        "full_name": "Parveen Kumar",
        "dob": "2004-01-01"
    }     

       Versoning = Control evovlution without breaking users 
   
   
   -> We maintain multiple version of same api 
   
      
      old clients use -> v1
      new clients use -> v2 

============================================================================================================

=> URL Versoning
   
     api/v1/users
     api/v2/users
     
     
     -> Best for public apis


=> Version life cycle 
      
      -> Relese v1
      
      -> Release v2 with improvements
      
      -> mark v1 as deprecated 
      
      -> Give migration time 
      
      -> Eventually remove v1              


"""