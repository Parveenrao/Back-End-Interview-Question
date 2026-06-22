"""

=> Polymorphsim 

     -> One interface , many forms

     -> Same method or operation behave differently depending on the object it is used 

"""

class Dog:
    def speak(self):
        return "Bark"
    
class Cat:
    def speak(self):
        return "Meow"


animals = [Dog() , Cat()]

for animal in animals:
    print(animal.speak())


    