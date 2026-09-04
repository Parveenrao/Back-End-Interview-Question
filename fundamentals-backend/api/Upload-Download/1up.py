""" 

=> File Upload and Downloads

    -> File upload and download are common API operations used in social media apps , cloud-storage
      e-commerce , healthcare


    -> Example 

         Upload profile picture 
         Upload PDf invoice
         Upload product image 
         Download reports 
         Download videos


=> FastAPI Upload 

   from  fastapi import FastAPI , UploadFile , File

   app = FastAPI()

   @app.post("/upload")
   async def upload(file :UploadFile = File(...)):
        return {
             
            "filename" : file.filename,
            "content-type" : file.content_type


        }

=> validate file

ALLOWED = {
    "image/png",
    "image/jpeg",
    "application/pdf"
}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED:
        return {"error": "Invalid file"}

    return {"success": True}


=> validate file size 


MAX_SIZE = 5 * 1024 * 1024  # 5 MB

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    size = 0

    while chunk := await file.read(1024 * 1024):
        size += len(chunk)

        if size > MAX_SIZE:
            return {"error": "Too large"}

    return {"message": "OK"}


=> Upload multiple files 


from typing import List
from fastapi import UploadFile, File

@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    return {
        "count": len(files)
    }


=> downlaod file in Fastapi 


from fastapi.responses import FileResponse

@app.get("/download")
def download():
    return FileResponse(
        "resume.pdf",
        filename="resume.pdf",
        media_type="application/pdf"
    )

=> stream large files 

from fastapi.responses import StreamingResponse

def file_iterator():
    with open("movie.mp4", "rb") as f:
        while chunk := f.read(1024 * 1024):
            yield chunk

@app.get("/video")
def video():
    return StreamingResponse(
        file_iterator(),
        media_type="video/mp4"
    )



"""