""" 

=> Composition 

    -> Composition has a strong has-A relationship where , one object own another object 

    -> child object is created and manged by parent object



"""


class Engine:
    def __init__(self):
        print("Engine Created")

    def start(self):
        print("Engine started") 

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()               


car = Car()

car.start()