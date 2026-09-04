""" 

=> Multipart Upload

   -> Is a way to upload large file in multiple smaller part (chunks) instead of sending the entire 
      file in one HTTP request 


   -> why do we need it

       1. Imagine a user uploads 10Gb video

       2. without multipart upload 

           -> client send the whole 10GB file
           -> If the connection breaks at 9.8 Gb , the client must start again from 0GB

      3. With multipart Upload

          -> split file into chunks (10MB each)

          -> Upload each file chunk separately 

          -> if chunk 450 fails , only 450 is uploaded again

          -> server combine all chunks after every part is received 

=> Client
   |
   |---- Create Upload Session ---->
   |
Server
   |
   |<---- upload_id = abc123 -------
   |
Client

Split file

Part 1 (10 MB)
Part 2 (10 MB)
Part 3 (10 MB)
...

   |---- Upload Part 1 ---->
   |<---- OK ---------------
   |
   |---- Upload Part 2 ---->
   |<---- OK ---------------
   |
   |---- Upload Part 3 ---->
   |<---- OK ---------------
   |
   |---- Complete Upload --->
   |
Server joins all parts

final_file.mp4


=> Why use multipart upload instead of a single upload?
     -> It improves reliability for large files by allowing retries and resuming without 
        restarting the entire upload.

=> Can parts be uploaded in parallel?
    -> Yes. Parts are independent, so clients can upload several simultaneously to 
       reduce total upload time.


=> What happens if one part fails?
    -> Only that part is retried; previously uploaded parts remain intact.       

=> what is multipart upload 

    -> Is a technique where a large file is split into smaller chunk and each chunk is uploaded 
       separately.

       after all chunk are uploaded , the server combine them into the final state

=> How do you prevent duplicate chunks?

     -> Use the combination of upload_id and chunk_number as a unique identifier. 
        If the same chunk is uploaded again, either overwrite it or reject it based 
        on your design.       

=> What if the client never finishes the upload?

    -> Keep a timeout (for example, 24 hours). A background job periodically deletes 
       incomplete uploads and their temporary files.        
"""