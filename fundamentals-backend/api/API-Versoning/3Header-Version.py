""" 

=> Header Version 

    -> Header Version means the API version is sent in an HTTP header instead of URL

    -> THE URL stays the same

        GET/user/1

        CLient specifies the version in a header


    -> Example 

        GET/user/1

        API-version 1

        for newer version 

        GET/users/1

        API-version 2

=> from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/users/{id}")
def get_user(
    id: int,
    api_version: str = Header(...)
):
    if api_version == "1":
        return {
            "id": id,
            "name": "Alice"
        }

    elif api_version == "2":
        return {
            "id": id,
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": "alice@example.com"
        }

    raise HTTPException(
        status_code=400,
        detail="Unsupported API version"
    )            



"""