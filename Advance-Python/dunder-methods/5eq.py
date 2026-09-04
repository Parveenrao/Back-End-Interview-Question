""" 

=> __eq__ in python 

    -> be default two separate objects are not considered equal becuase their data matches



"""

class Equal:
    def __init__(self , name):
        self.name = name 

    def __eq__(self, other):
        return self.name == other.name

u1 = Equal("Parveen")

u2 = Equal("Parveen")

print(u1 == u2)
            