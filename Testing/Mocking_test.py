"""  
=> Mocking 
   -> In pytest is replacing real dependencies  with controlled fake objects to isolate and test a unit of code
   
--------------------------------------------------------------------------------------------------------------------

=> What is actually means 
  
  When your function depends on thing like 
   
   1. Databse
   2. File system
   3. External API
   4. Network 
   
   -> You don't want to use real one in tests 
   
   -> So we replacing with fake ones   , control their behaviour and test our only logic



"""
import unittest
from unittest.mock import Mock
import pytest

def call_api():
    
    # imagine this call real external api 
    
    return {"name" : "real_user"}


def save_to_db(user):
    # imagine saving to db 
    
    print("Saved to db")

def process_user():
    data = call_api()
    save_to_db(data)
    return data["name"]

# Now we mock 

def test_user_process(mocker):
    
    # mock api
    
    mocker.patch(__name__  + ".call_api" , return_value = {"name" : "Parveen"})
    
    # mock db
    
    mock_db = mocker.patch(__name__ + ".save_to_db")
    
    # call function 
    
    result = process_user()
    
    # assert 
    
    assert result == "Parveen"
    mock_db.assert_called_once_with({"name": "Parveen"})
    
def test_process_user_api_failure(mocker):
    
    # Simulate API failure
    mocker.patch(__name__ + ".call_api", side_effect=Exception("API failed"))

    # Check exception
    with pytest.raises(Exception):
        process_user()    


    