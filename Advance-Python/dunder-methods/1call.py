""" 

=> Call dunder method in python 

    -> __call___ is an special dunder method that lets an object behave like a function




"""

class Counter:
    def __init__(self):
        self.counter = 0 

    def __call__(self):
        self.counter += 1
        return self.counter


count = Counter()

print(count()) #1
print(count()) #2
print(count()) #3


class Greet:
    def __init__(self , name):
        self.name = name 

    def __call__(self):
        print(f"Hello {self.name}")


h = Greet('Parveen')

h()  # here h is not a function , but it behaves like a function