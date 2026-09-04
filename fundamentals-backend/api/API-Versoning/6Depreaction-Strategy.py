""" 

=> Depreaction Strategy

   -> Is a plan for retrining an old API version without suddenly breaking existing clients 

   -> Instead of deleting v1, immediately after releasing v2 m you give users time to migrate 


        Depreaction = This version still works , but it will be removed in future


from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/api/v1/users")
def users_v1(response: Response):
    response.headers["Deprecation"] = "true"
    response.headers["Sunset"] = "Wed, 31 Dec 2026 23:59:59 GMT"
    response.headers["Link"] = '</api/v2/users>; rel="successor-version"'

    return {
        "message": "Old API version"
    }   



"""