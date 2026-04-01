# Unit test 

import pytest

def add(a , b):
    return a + b


def test_add():
    assert add(2, 3) == 5

# conditions 

def test_condition():
    assert "hello".upper() == "HELLO"    
    
def multiply(a, b):
    return a *b

def test_multiply():
    assert multiply(2, 3) == 6

"""   
=> Python detect test if
   
   file - test_*.py / *_test.py
   function start with  test_
"""