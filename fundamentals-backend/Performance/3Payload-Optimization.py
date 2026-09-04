""" 

=> Payload Optimization 

    -> Means reducing the size of data sent between client and server without losing important 
       information . So API become faster , use less bandwidth and reduce server cost 

    -> Goal 

       1. Faster response time 
       2. Lower network usuage 
       3. Lower latency 
       4. Better mobile performance 
       5. Reduce cloud cost 


=> Example An E-commerce Returns without Optimization 
  

{
    "id": 101,
    "name": "iPhone 17",
    "description": "Latest Apple smartphone with A20 chip, OLED display, 256GB storage...",
    "manufacturer": {
        "id": 12,
        "name": "Apple Inc.",
        "address": "California, USA",
        "employees": 160000,
        "ceo": "Tim Cook"
    },
    "reviews": [...500 reviews...],
    "images": [...50 images...],
    "related_products": [...100 products...]
}

    -> Response size 5MB


------------------------------------------------------------------------------------------

=> 1 Field Selection 

    -> Instead of returning every field  , return only requested field 

        GET/user?filed = id , name ,email


=> Pagination 

  -> never send thousand of records 


=> Compression 

   -> Server compress response


=> Sparse Response

   -> Allow client to choose exactly what they need


=> Projection 

   -> Means selecting only specific database columns before fetching data 

      select  id , name , email from user 


   -> instead of selecting every field from database and then discarding them , projection 
       reduce I/o and memory usuage 

=> Remove Null values

     {"name"  :  "john",
      "phone" :   null,
      "age"   :   null,
      "address" : null}


     -> FastAPI pydantic

from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: str | None = None
    age: int | None = None

@app.get("/user", response_model=User, response_model_exclude_none=True)
def get_user():
    return User(name="John") 

=> Binary Formats

   -> JSON is text 

   -> use binary format mainly for service to service communication 

=> Lazy Loading

   -> Load heavy data only when needed

=> Efficient Serilization

     -> Some serializers are faster and produce smaller payloads 

=> Minification Of JSON     

"""