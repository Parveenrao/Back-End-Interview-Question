"""  
=> Marking 
    
    -> Pytest.mark is used to add metadata (labels) to test so you can control their behaviour 

"""

import pytest 

@pytest.mark.slow
def test_big_task():
    assert True

# multiple mark 
@pytest.mark.slow  
@pytest.mark.api 
def test_api_call():
    assert True    
    

# built in marker 

# 1. skip don't run this test 

@pytest.mark.skip
def test_skip():
    assert False
    
# 2. skipif based on condition 

import sys

@pytest.mark.skipif(sys.platform == "win32" , reason= "NOt for windows") 
def test_linux():
    assert True

# 3. expected to fail 

@pytest.mark.xfail
def test_known_bug():
    assert 1 == 2
               