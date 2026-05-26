""" 

=> Race Condition 
    -> When multiple process access and change the data at the same time
    
    -> Each process run independently , so timing become unpredicatable



"""


from multiprocessing import Process , Value

lock = 

def increment(counter):
    
    for _ in range(10000):
        counter.value += 1

if __name__ == "__main__":
    
    counter = Value("i" , 0)
    
    p1 = Process(target=increment , args=(counter,))
    p2 = Process(target=increment , args=(counter,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(counter.value)
            