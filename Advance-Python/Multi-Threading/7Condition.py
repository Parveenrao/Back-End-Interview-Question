""" 
=> Condition
    
    -> A condition let thread wait until a specific state become true , another thread notifies them 
       
       when it changes
       
    -> Sleep until something happens   


"""

import threading

con = threading.Condition()

buffer = []


def consumer():
    with con:
        
        while not buffer:
            print("waiting")
            con.wait()
    
        print("waking up" , buffer.pop())

def producer():
    with con:
        buffer.append(42)
        print("Produced 42")
        con.notify()

threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()                        


# Condition lets threads pause safely and resume when something changes