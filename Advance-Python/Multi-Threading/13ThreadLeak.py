""" 

=>Thread Leak
    
    -> Thread leak happen when thread are created but never properly cleaned up or terminated
    
    -> Forgetting to join thread , cause thread leak , 

"""

import threading 
import time

def worker():
    time.sleep(10000)
    
while True:
    threading.Thread(target=worker).start()          # infinite thread created , never cleaned or teriminatd    
    
    
# Creating thread per request 

@app.get("/")
def api():
    threading.Thread(target = task).start()     # huge traffic , thousand of threads     
    
    
# always use Threadpool executor , only no of thread used

# daemon thread , automatically kill thread when program runs    