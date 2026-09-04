""" 

=> Polling 

   -> Polling means the client repeatedly ask the server 

        "Is my job finished"

      unitl the server says it is completed 

      Instead of waiting on one HTTP request , client send multiple request at interval


=> WHy Polling

   -> Suppose generating report take 5 minutes

   -> Bad approach

       POST/report 

       (wait....)

       (wait....)

       (wait....)

       http timeout 
       user refersh page browser timeout


    -> Better approach 

       POST/report 


       202 Accepted 


       CLient poll every 5 second

       Eventually received completed      



"""