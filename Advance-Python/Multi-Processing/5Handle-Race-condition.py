# Using lock 

from multiprocessing import Value , Lock , Process

def increment(counter , lock):
    with lock:
        for _ in range(100000):
            counter.value += 1


if __name__ == "__main__":
    
    counter = Value("i" , 0)
    
    lock = Lock()
    
    p1 = Process(target=increment  , args=(counter , lock))
    
    p2 = Process(target=increment , args = (counter , lock))
    
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(counter.value)
    print("Main Process finished")
    
    
    
            