""" 

=> WHy do we override __new__ instead of __init__

  
    __new___ = create object , allocate memory 


    __init__ = initializes the object 


"""


class Database:
    _instance = None       # class variable , belong only to class , not to any object , no db object has been created yet 
    _initialize = False    # another class variable , initialization is not happen yet


    def __new__(cls):               # is called before an object exist
        if cls._instance is None:
            print("Creating instance")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not self._initialize:
            print("Connecting to database")
            self.connection = "Connected"
            self._initialize  = True         