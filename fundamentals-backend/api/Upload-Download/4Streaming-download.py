""" 

=> Streaming Download 

   Streming dowload means the server sends a file piece by piece (chunks) instead of loading
   the entir file into memory before sending it

   this is important for large files such as videos , PDFs backups or machine learning models


=> Why do wee need it

    1. Suppose we have 5GB files

    2. without streaming

       data = open("movie.mp4" , "rb").read()   # reads all 5GB into RAM

       returns Response(RAM)

    3. Problems

        1. High memory usuage
        2. SLow response 
        3. can cause out of memory (errors)


=> Client
   |
   |------ GET /download/movie.mp4 ------>
   |
Server
   |
Read first chunk
   |
Send first chunk
   |
Read second chunk
   |
Send second chunk
   |
Read third chunk
   |
Send third chunk
   |
Until file ends


=> FastAPI Streaming 

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

def file_generator():

    with open("movie.mp4", "rb") as file:

        while chunk := file.read(1024 * 1024):  # 1 MB
            yield chunk

@app.get("/download")
def download():

    return StreamingResponse(
        file_generator(),
        media_type="video/mp4"
    )

-> why use yield

   -> python reads entire file into memory

   -> only one chunk is kept memory at time


=> Download with filename 

from fastapi.responses import StreamingResponse

@app.get("/download")
def download():

    headers = {
        "Content-Disposition": 'attachment; filename="movie.mp4"'
    }

    return StreamingResponse(
        file_generator(),
        media_type="video/mp4",
        headers=headers
    )

=> What is the difference between StreamingResponse and FileResponse?


StreamingResponse	                   FileResponse
Streams any iterable/generator	         Serves an existing file
Good for dynamic content	             Best for static files
Custom streaming logic	                 Simpler and optimized for files    



"""