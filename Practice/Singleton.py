# Thread safe singleton pattern we can implement 


from threading import Lock , current_thread , Thread
import time

class Database:
    _instance = None
    _initialization = False
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                print(f"Creating instance by {current_thread().name}")

                cls._instance = super().__new__(cls)

        return cls._instance


    def __init__(self):
        if not self._initialization:
            print("Connecting databse")
            time.sleep(2)   

            self.connection = "Connected"
            self._intilization = True
            
    def query(self):
        print(f"{current_thread().name} using {id(self)}")            



# hit multiple request 

def handle():
    db = Database()
    db.query()


threads = [] 

for i in range(5):
    t = Thread(target = handle , name = f"Request - {i + 1}")

    threads.append(t)


for t in threads:
    t.start()


for t in threads:
    t.join()





