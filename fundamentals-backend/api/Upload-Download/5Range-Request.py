""" 

=> Range Request 
   
     -> A Range Request is an HTTP Feature that lets a client request only a specific byte of
        range of a resources instead of downloading the entire file


        defined by HTTP Range header


     -> why do we need that 

         Imagine a 10GB movie 

         without Range Request

         Client -> GET/movie.mp4 -> server -> sends entire 10gb 


         problems 

           -> user watches only the first 5 minutes

           -> entire file is downloaded unnecessarily 

           -> cannot earily resume downloads

=> Fastapi did automatically 


from fastapi.responses import FileResponse

@app.get("/video")
def video():
    return FileResponse("movie.mp4")



"""