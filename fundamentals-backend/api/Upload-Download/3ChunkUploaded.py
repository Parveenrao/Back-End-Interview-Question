""" 


=> Chunked Uploaded 

    -> Chunked uploaded means breaking a large file into smaller pieces and uploading each chunk
        separately 

    -> why use chunked uploads 

        1. Resume interrupted uploads 
        2. Retry only failed chunks 
        3. Upload very large files 
        4. Reduce memory usuage
        5. Support parallel uploads


=> What is chunked upload?

    -> Chunked upload is a technique where a large file is divided into smaller chunks, 
       and each chunk is uploaded separately. The server reconstructs the original 
       file after receiving all chunks.  

=> Who splits the file into chunks?

    -> Usually the frontend or client application (JavaScript in a browser, a mobile app, 
       or another backend service). The server simply receives each chunk.                 


"""