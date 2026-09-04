""" 

=> Race condition in Singleton

    Thread-1                Thread-2
---------                    ---------

Starts __new__()

                              Starts __new__()

Checks:
_instance == None ✓

                              Checks:
                              _instance == None ✓

Creates Object A

                              Creates Object B

Stores:
_instance = Object A

                              Stores:
                              _instance = Object B


       -> Now two objects are created ,                        




"""


from threading import Thread , Lock , current_thread

import time 


class Database:
    _instance = None
    _intilization = False 
    _lock = Lock()

    def __new__(cls):

        # only one thread can enter this block at a time 

        with cls._lock:
            if cls._instance is None:
                print(f"Creating instance by {current_thread().name}")

                cls._instance = super().__new__(cls)

    def __init__(self):

        # prevenet multiple initialization 

        if not self._intilization:
            print("Connection to database")
            time.slee(2)                       # stimulate expensive intialization

            self.connection = "Connected"
            self._intilization = True

    def query(self):
        print(f"{current_thread().name} using {id(self)}")            


db1 = Database()

db2 = Database()

print(db1 is db2)