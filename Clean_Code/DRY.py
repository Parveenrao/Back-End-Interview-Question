""" 
=> DRY Principle (Do Not Repeat Yourself)
   
   -> DRY is a principle that states that every piece of logic and knowledge shoud have single, unambiguous representation in system
      
    -> Clean codebase 
    -> Fewer base
    -> Scalable 
    -> Faster development
    
-> Apply DRY where duplication is meaningfull 

    1. Duplicate once = Ok
    2. Duplicate twice = Think
    3. Duplicate thrice = refactor 
        
"""


# Example , validate username and password

if len(username) < 3: 
    raise Exception("Invalid username")

if len(password) < 8:
    raise Exception("Invalid password")


# clearn code 

def validate_length(username , min_len):
    
    if len(username) < min_len:
        raise Exception("Invalid input")



validate_length(username, 3)
validate_length(password, 8)