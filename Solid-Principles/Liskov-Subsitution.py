""" Child class should behave like the parent class"""

# -------------------- Bad Design -----------------------------------

class Vehicle:
    
    def start_engine(self):
        print("Engine started")
        

class Car(Vehicle):
    pass



class Bicycle(Vehicle):
    
    def start_engine(self):
        raise Exception("Bicycle has no engine")
    


def start_vehicle(vehicle : Vehicle):
    vehicle.start_engine()
    
    
start_vehicle(Car())

start_vehicle(Bicycle())    

# Bicycle crash the program   
# Beacuse system expect every vehicle has engine 


# -------------------- Good Design ----------------------------


class Vehicle:
    pass


class EngineVehicle:
    def start_engine(self):
        print("Engine started")


class Car(EngineVehicle):
    pass

class Bicycle(Vehicle):
    pass
