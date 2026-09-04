""" 


=> CORS (Cross origin Resources Sharing) In API Security

    -> CORS is a browser security mechanism that controls which website are allowed to access
       your API


    -> CORS tells browser that whether Javascript from another origin is allowed to make request
       your API

=> What is Origin

    Protocol + Domain + Port 

    https://example.com:443


=> Why do we CORS

    -> Imagine this 

     Frontend
     https://amazon.com

     Backend
     https://api.amazon.com


     Javascript on the frontend wants to call

     GET https://api.amazon.com/products 


     Since 
       1. amazon.com
       2. api.amazon.com 

       are different origin 

       the browser ask

          Is this API allowing this website 

          This permission is CORS


=> Same Origin Policy

   -> Browser only allow javascript to access resource from the same origin


=> Important CORS headers 

    1. Origin Request Header

        sent by browser 

        Origin: https://myapp.com

    2. Access control-allow origin

        Server response 

        Access-Control-Allow-origin: https://myapp.com

    3. Access control allow method

        GET  , POST , PUT , DELETE , PATCH

    4. Access-Control-Allow Headers

       -> Allowed Request Header 

           Authorization

           Content-type

           X_API_KEY


   5. Access-Control-Allow-Credentials

      -> Allows cookies or HTTP authentication

            Access-Control-Allow-Credentials : true


=> CORS In FastAPI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://myapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


-> 1. Origins = [https://myaap.com ]  

     -> only this website can acces my api 

-> allow_method = [*]

   -> allow all http method 

-> allow_headers = [*]

   -> allow all request headers 

-> allow_credentails = True   


"""