# Advance mocking 


import requests
import unittest
from unittest.mock import Mock
import pytest
def fetch_data():
    
    for _ in range(3):
        try:
            res = requests.get("https://api.com")
            
            if res.status_code == 200:
                return res.json()
        
        except Exception:
            continue
    
    raise Exception("API failed after 3 retry")
        

def test_retry_success(mocker):
    
    # create mock response 
    
    fail_response  = Mock()
    fail_response.status_code = 500
    
    success_response = Mock()
    success_response.status_code = 200
    success_response.json.return_value = {"data" : "ok"}    
    
    
     # Side effect = multiple returns
    mocker.patch(
         __name__ + ".requests.get",
        side_effect=[fail_response, fail_response, success_response]
    )    
    
    # call functiom 
    
    result = fetch_data()
    
    assert result == {"data" : "ok"}

# all fail

import pytest

def test_retry_fail(mocker):
    
    mocker.patch(
        __name__ + ".requests.get",
        side_effect=Exception("API down")
    )

    with pytest.raises(Exception):
        fetch_data()    