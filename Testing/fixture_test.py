""" 
=> A fixture is a reusable setup that provide data or enviornment to test
     
     -> Prepae something once , resuse , it across test
"""

from pytest import fixture
import pytest

def login_user(user , password):
    if not user["is_active"]:
        raise ValueError("user is inactive")
    
    if user["password"] != password:
        raise ValueError("Wrong password")
    
    return "login successfull"

# creat fixture

@pytest.fixture
def active_user():
    return {"is_active" : True , "password" : "1234" }


def test_login(active_user):
    result = login_user(active_user , "1234")
    
    assert result == "login successfull"
