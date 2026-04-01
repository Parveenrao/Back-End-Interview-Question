""" => Race Condition 
    
       -> When multilple thread try to  access the shared data simultaneously is calle race condition 
       
       -> Incorrect behavior caused by  multiple thread accessing shared data  without proper synchronization 
       
       -> Example   Initial balace = 100
       
           1. Thread A -> Read balance 
           2. Thread B -> Read balance  
           
           3. Thread A write 150 
           4. Thread b write 120
           
           -> Thread b overwrite b update  -- called race condition
    
   """
   
import threading , time

balance = 100 

def balance1():
    global balance
  
    balance = balance + 50

def balance2():
    global balance
  
    balance = balance  + 20 


t1 = threading.Thread(target=balance1)
t2 = threading.Thread(target=balance2)

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)         



"""   => Why Race condition happens 
         
          1. Shared data
          2. No synchronization 
          3. Multiple threads 
          
       if we remove any one , race condition disppaers   
      
      
      => Critical section  
      
         -> code that access shared resource is called critical section  
       
       
       
       
       """