""" 
=> Duck Typing  
     
     -> Means type of object is less important that the behaviour it provide.  
     -> If an object has required method or attribute, it can be used regardless of its class
   
   
   
   -> If it looks like duck , behave like duck , python treat it as duck  

"""


class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

def make_sound(animal):
    return animal.speak()


print(make_sound(Cat()))
print(make_sound(Dog()))


# if required object has not method , then it crash , so we can handle it multiple way


# 1. EAFP , Try first  handle error if fails
  
  
def make_sound(obj):
    try:
        return obj.speak()
      
    except AttributeError:
          return "Object cannot speak"


# 2. LBYL , Check before using

def make_sound(obj):
    
    if hasattr(obj, "speak"):
        return obj.speak()
    
    return "Object cannot speak"

# 3. Protocol says , i dont care about classess , if you must have these methods

from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str : ...  
    


class Dog:
    def speak(self):
        return "Bark"

class Car:
    pass 

def make_sound(obj: Speaker):
    return obj.speak()

print(make_sound(Dog()))   # ✅ works
print(make_sound(Car()))   # ❌ type checker will warn             
        