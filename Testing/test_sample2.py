# Little complext unit test 

import pytest

def apply_coupon(price : float , discount_price : float) -> float:
    
    if price < 0:
        raise ValueError("Price cannot be negative ")
    
    if not (0<= discount_price <=100):
        raise ValueError("Invalid discount percent")
    
    discount  = price *(discount_price/100)
    
    return price - discount


def test_valid_discount():
    assert apply_coupon(100 , 10) == 90
    
def test_zero_discount():
    assert apply_coupon(100 , 0) == 100

def test_full_discount():
    assert apply_coupon(100 , 100) == 0        


# Test edges cases 

def test_negative_price():
    with pytest.raises(ValueError):
        assert apply_coupon(-100 , 10)

def test_invalid_discout():
    with pytest.raises(ValueError):
        assert apply_coupon(100 , 150)        
        