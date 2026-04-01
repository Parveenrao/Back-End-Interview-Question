#  A Topic is  a named stream of data (message / events) where producer and consumer read them 

# Example in an E-commerce application , i have topic called orders where every new order event is pushed

# Real life example  

"""  Suppose you build a food delivery app 
     
      -> User places order 
      
      -> Order service send data somewhere
      ->  Payment service need it
      -> Delivery service need it 
       
       -> So we create a topic called order ,, producer and consumer read from it
       
     """

# One topic multiple consumer , No direct communication between services

from kafka import KafkaProducer

import time 

producer = KafkaProducer(bootstrap_servers = "localhost:9092")

for i in range(10):
    msg = f"orders_{i}"
    producer.send('orders' , msg.encode())
    print(f"Sent {msg}")
    time.sleep(1)
    
producer.flush         
