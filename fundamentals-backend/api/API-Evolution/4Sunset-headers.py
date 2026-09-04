"""
=> Sunset Headers 


      -> A sunset headers tells API client 

           "This API(or feature) will stop being available after a specific date and time"


      -> It gives developers advance notice so they can migrate before the endpoint is removed

=> Why is it needed

     1. Suppose you have   

         GET/api/v1/users

     2. You create a better api 

          GET/api/v2/users

     3. Instead you

         1. keep v1/uers working 

         2. tell clients it will be removed 

         3. give them to migrate 

         4. Remove it after the announced date

      This is exactly what the sunset header for 


=>  

from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/v1/users/{user_id}")
def get_user(user_id: int, response: Response):
    response.headers["Deprecation"] = "true"
    response.headers["Sunset"] = "Wed, 31 Dec 2026 23:59:59 GMT"

    return {
        "id": user_id,
        "name": "Parveen"
    }


=>  

Deprecation	                                       Sunset

Means the API is no longer recommended.	            Means when the API is expected to be unavailable.
"Don't build new integrations on this."	            "This endpoint will stop working after this date."
Can last for months or years.	                     Contains a specific removal date/time.

  
""" 