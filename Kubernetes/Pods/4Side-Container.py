""" 


=> Sidecar Container 

    -> Is a helper container that runs alongside the main application container in the same 
       Pod.

    -> It provide additional functionality without changing the application code 


=> WHy do we need sidecar container 

     1. Imagine we have application

         App -> Receives Request -> Writes logs 


     2. Now company wants

         1. Send logs to elasticsearch 
         2. send metrics to prometheus 
         3. encrypt network traffic 
         4. rotate certificate 


=> Side car run in parallel 


     Application Container + Sidecar pattern = Both keep running


=> Example 

   1. Log Collection 

      Application 
         
         Writes -> /logs/app.log


       Sidecar

       Read -> /logs/app.log -> Sends -> Elasticsearch     



"""