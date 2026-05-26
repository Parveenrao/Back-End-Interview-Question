""""
=> Daemon Thread
    
    -> A Daemon Thread is a background thread that automatically stop when the main program finish
    
    -> It does keep the program alive

"""

import threading
import time

def worker():
    while True:
        print("Running...")
        time.sleep(1)

t = threading.Thread(target=worker, daemon=True)          # if dameon false , program stuck infeintly
t.start()

time.sleep(3)
print("Main finished")

"""  
👉 Program exits right after "Main finished"
👉 Worker thread is killed instantly

"""