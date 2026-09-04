""" 

=> Validation Errors

     -> validation errors occured when the client send that does not satisfy API rules

     -> API expects 

         {
         
         
         
         "name" : "Parveen"
         
         }

     -> Client sends 

         {
         
         "name" : "parveen"
         "age"  : "twenty two" 
         }    

         request reach the server , but data is invalid so the server returns a validation error


=> What is Validation

    -> Validation means checking whether the incoming data matches the expected format and rule 
       before processing it 



-> Examples of rules:

Required fields
Correct data types
Minimum/maximum length
Valid email format
Positive numbers
Date format
Custom business rules



=> Custom validation 

from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        return value


=> Real life example 

 class RegisterRequest(BaseModel):
    username: str = Field(min_length=4)
    password: str = Field(min_length=8)
    email: EmailStr


=> Field validator in pydantic

    -> Use it when we want to validate a single field

    -> age must be at least 18

from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        return value


=> Model validator

   -> use when validator depends on multiple field
from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


from pydantic import BaseModel, EmailStr, field_validator, model_validator

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError(
                "Password must be at least 8 characters"
            )
        return value

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match"
            )
        return self


        before mode in model validator
"""