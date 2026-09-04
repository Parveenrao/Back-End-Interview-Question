""" 

=> Backward Compatibility 

    -> A new version of the API should continue to work with old client without requiring 
       them to change their code 


=> Real world example 

    -> Suppose mobile apps version 1.0 calls this API

        GET/users/1

    -> Server resposne 

         {
         "id" : 1,
         "name" : "Parveen"
         
         
         
         }    
    
    -> frontend code 

         console.log(user.name)

         everything works

    -> Later the backend team want to add an email 

        New response 

        {
        
        "id" : 1,
        "name" : "Parveen",
        "email" :'parveen@example.com"

        
        }          

    -> old frontend

        console.log(user.name)

        still works

    -> because nothing the old client depended on was removed or changed.
       The client simply ignores the new email field

    -> this backward compatibility

=> Safe changes

    1. Add optinal fields

    2. Add new endpoint

    3. Add optional query parameter 


    4. Add new response headers 


=> Unsafe changes 

    1. Rename a field

    2. Remove a field

    3. Change data type 

    4. Change endpoint

=> Safe 



from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None

@app.get("/users/{id}", response_model=User)
def get_user(id: int):
    return {
        "id": id,
        "name": "Parveen",
        "email": "parveen@example.com"
    }    
"""