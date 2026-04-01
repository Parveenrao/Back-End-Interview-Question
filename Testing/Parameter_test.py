"""  
=> Write one test , run multiple input
"""

import pytest

@pytest.mark.parametrize("a , b ,expected" , [
    (2 , 3 ,5),
    (1, 1, 2),
    (0, 5,  5)
])

def test_add(a , b , expected):
    assert a +  b == expected

#-----------------------------------------------------------------------------------------------

def login_user(user , password):
    
    if not user["is_active"]:
        raise ValueError("User is inactive")
    
    if user["password"] != password:
        raise ValueError("Wrong password") 
    
    return "login successfull"


@pytest.fixture
def active_user():
    return {"is_active" : True , "password" : "1234"}

@pytest.fixture
def inactive_user():
    return {"is_active" : False , "password" : "1234"}

@pytest.mark.parametrize("password " , ["1234"])
def test_login_success(active_user , password):
    result = login_user(active_user , password)
    assert result ==  "login successfull"
    
    
@pytest.mark.parametrize("password" , [
    "wrong" ,
    "123",
    "abcd"
])    

def test_wrong_password(active_user , password):
    with pytest.raises(ValueError):
        login_user(active_user  ,password)