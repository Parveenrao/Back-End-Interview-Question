# Clients shoud not forced to depend on interface they don't use 

# ---------------- Bad Design ------------------------------------

# Delivery Agent system 

class DeliveryAgent:
    
    def pick_order(self):
        pass
    
    def deliver_order(self):
        pass
    
    def charge_battery(self):
        pass
    

class BikerRider(DeliveryAgent):
    
    def pick_order(self):
        print("Rider picking order")
        
    def delilver_order(self):
        print("Rider Delivering order")
    
    def charge_battery(self):
        raise Exception("Bike dont need battery to charge")



# BikeRider forced to implement charge_battery()



#-------------------------- Good Desing---------------------------------

class DeliveryAgent:
    
    def pick_order(self):
        pass
    
    def deliver_order(self):
        pass
    
class BattteryPowered:
    
    def charge_battery(self):
        pass
    
    
class BikeRider(DeliveryAgent):
    
    def pick_order(self):
        pass
    
    def deliver_order(self):
        pass


class DroneDeliver(DeliveryAgent , BattteryPowered):
    
    def pick_order(self):
        pass
    
    def deliver_order(self):
        pass
    
    def charge_battery(self):
        print("Drone need batteryh to charge")
                

           