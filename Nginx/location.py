"""   
=> Location 
   
   -> It decide how a request is handled based on its url 
   
   incoming request -> match a location - apply config
   
------------------------------------------------------------------------
=> Types of Location 

   1. Exact Match (=)
       
    -> Example  
    
       location = /login {
           
           # exact match only
                
       }   
       
    -> match only , /login
    
    -> Not , /login/ , /login/users
  
  2. Prefix match (default)
       
       location /static/ {
           
       }  
       
       
       -> matches    /static/a.png  , /static/css/style.css
  
  3. Regext match (~ and ~*)
  
  4. Priority prefix (^~)
  
    -> if this prefix match  , stop seaching regex
    
-----------------------------------------------------------------------------------

=> Matching Priority 

    1. Eaxact match 
    2. Priority Prefix
    3. Regex
    4. Normal prefix
    
---------------------------------------------------------------------------------------

=> Example 
             
location /api/ {
    proxy_pass http://backend;
}

location /static/ {
    alias /var/www/assets/;
}
    
   
           
"""