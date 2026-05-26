# Args in process -> Passing positional arguments 

from multiprocessing import Process
import os

def square(n):
    print(n * n) 


if __name__ =="__main__":
    
    p = Process(target=square , args=(5, ))
    p.start()
    
    p.join()
    
# Multiple arguments 

def add(a , b):
    print(a + b)  

p = Process(target=add , args=(10 ,5))        


# kwargs 

def intro(name , age):
    print(name , age)
    
p = Process(kwargs={"name" : "Parveeen" , "age" : 21})    


# custom name process 

p = Process(target= intro , name = "Woker-1")

print(p.name)