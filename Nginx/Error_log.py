"""  
=> Error logs 
       -> Record of problems , warning and internal failures 


---------------------------------------------------------------------------------

=> Default location 
           
           /var/log/nginx/error.log

=> Configure logs 
         
         error_log /var/log/nginx/error.log warn;

=> Debugging -> debug 
          error_log /var/log/nginx/error.log debug:

------------------------------------------------------------------------------------

debug --> Everything(internals)
info --> general info 
notice ---> normal events 
warn   ---> something might be wrong 
error ---> Serious issue 
crit ---> critical failure
alert --> immediate action needed 
emerg ---> System unusable                                      

"""