""" 

=> RFC-7807 
    
      -> Is an HTTP standard that defines a consistent JSON format for API error response

      -> Instead of every API returing errors in different formats , RFC 7807 gives everyone the
         structure 



=> Structure 


   {
    "type": "https://example.com/errors/user-not-found",
    "title": "User Not Found",
    "status": 404,
    "detail": "User with id 15 does not exist.",
    "instance": "/users/15"
}


-> type 

   A URI identiyfing the error type 

   "https://example.com/errors/user-not-found",

   This URL can describe 

      -> Why the error happened

      -> how to fix it 

      -> Documentation

-> title 

    -> A short human-readable summary

       "title" : user not found

-> status 

  HTTP status code
    "status" 404

-> details 

   Detailed explanation 

   "detail" : "user with id 5 does not exist"

-> instance

   the request caused the prpblem

   "instanc" /user/5


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int, request: Request):
    if user_id != 1:
        return JSONResponse(
            status_code=404,
            media_type="application/problem+json",
            content={
                "type": "https://example.com/errors/user-not-found",
                "title": "User Not Found",
                "status": 404,
                "detail": f"User {user_id} does not exist.",
                "instance": str(request.url.path)
            }
        )

        
    return {"id": 1, "name": "Alice"}

    
-> we can add custom field 


{
    "type": "https://example.com/errors/validation",
    "title": "Validation Failed",
    "status": 422,
    "detail": "Email is invalid.",
    "instance": "/register",
    "timestamp": "2026-07-19T10:30:00Z",
    "request_id": "req_abc123",
    "field": "email"
}
   



"""