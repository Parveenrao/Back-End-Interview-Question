""" 

=> Long Running Operations 

   -> A long running operation is an API request that takes too long to complete immediately 


   -> Instead the client wait , the server 

      1. accept the request 
      2. starts the work in background 
      3. immediately returns a response 
      4. lets the client check the progress later 


=> Why not keep connection Open 

    POST/generate-report 

    Generating report takes -> 8 minutes 

    if the server waits 8 minutes before responding

    Client -------------------> Server 

    POST/generate-report 

    (wait.....)

    (wait.....)

    (wait.....)

    (wait.....)

    -> Problems 

       1. HTTP timeout 
       2. Browser timeout 
       3. Load balancer timeout
       4. User think application froze 
       5. Waster server threads / workers 

-> Real life example 

   1. Video upload 

       POST/video

       Video is uploaded 

       -> Server now needs 
          
          1. encode
          2. compress
          3. create thumbnails 
          4. detect copyrights 
          5. generate copyrights

   2. Ml-Training Model 

      -> may take  2 hours 

  3.  Data import 

     -> Processing 

        1. Validation 
        2. duplicates 
        3. insert 
        4. indexing 


   4. Email campaigns

       POST/campaign/send                 



"""