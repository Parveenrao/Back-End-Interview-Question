""" 
=> Depends-On
    
    -> Tells docker which service start first 
    
    app:
      depends_on:
        - postgress:
        - redis:
     
    
    Start postgres → start redis → then start app
  
  -> Depdens only control order , it does not check , db ready , redis ready

----------------------------------------------------------------------------------------------

=> Advance Depends 
    
    app:
      depends_on:
         postgress:
             condition : service_healthy      
"""