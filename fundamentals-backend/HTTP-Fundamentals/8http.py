""" 

=> MIME Type 

   -> Multi-Purpose Mail Extension is a standard that tells the receiver what type of data
      is being sent 



    -> why do we need MIME Type

        1. Imagine browser receives this reponse


            HTTP/1.1 200 OK

            <some data here>

           How does the browser know whether the data is 

              HTML
              JSON
              Image
              PDF
              MP4 video

            thats why HTTP include a Content-Type header



=> WHere are MIME Types USED


    1. Content Type

       -> Tells what is acutally inside the body

          content-type : application/json

    2. Accept 

       Sent by the client 

       It tells the server 

          I can accept these MIME types      


"""