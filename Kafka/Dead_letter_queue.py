""" 
=> Dead letter queue

    -> A dead letter queue is just an another topic wher u can send message that your consumer failed to process
    
    
    -> Without DLQ
        
        Consumer read message -> fails -> retries -> fails -> retries -> fails
        
        you get a posion pill loop
        
        
    -> With topic 
       
       System keep moving
       
       -> bad message isolated for later inspection

-------------------------------------------------------------------------------------------------------------------

=> Working 
    
    1. Consumer read message 
    2. Processing fail
    3. catch the error
    4. Send message to dlq topic
    5. commit offset           

"""

from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    group_id="order-service",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    enable_auto_commit=False
)

dlq_producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def process(msg):
    if msg.value["amount"] < 0:
        raise Exception("Invalid amount")

for msg in consumer:
    try:
        process(msg)
        consumer.commit()

    except Exception as e:
        print("Error:", e)

        # 👉 send to DLQ
        dlq_producer.send("orders-dlq", value=msg.value)

        # 👉 skip this message
        consumer.commit()