""" 
=> Method Override 

    -> Means a child class provides its own implementation of a method  that already exist in parent class




"""


class Aniaml:
    def sound(self):
        print("Animal makes a sound")


class Dog(Aniaml):
    def sound(self):
        print("Dog barks")



d = Dog()
d.sound()

# Dog class override the  sound method of animal