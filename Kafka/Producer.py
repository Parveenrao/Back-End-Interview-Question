""" 
=> Producer  == A Producer is a client that send message to kafka topic 

                    Order service → sends order event
                    Payment service → consumes it
                
                Producer = data generator
                
-------------------------------------------------------------------------------------

=> How kafak sends data 

    -> producer.send('orders' , value)
    
      -> Internally 
         
         1. Serialize data
         2. Decide partition
         3. Batch message 
         4. Send to broker

=> Partition Selection Logic 
   
   1. NO key 
      
      producer.send('orders' , b'data')
      
      -> kafka will use round robin algo 
   
   2. With key 
         producer.send('orders', key=b'user1', value=b'order1')
         
         kafka use hash key 
         
         same key -> same partition -> ordering gurantees

------------------------------------------------------------------------------------------------

=> Batching 
   
   1. Kafka does not send immedaitely 
   2. It batches message 
   3. Improve throughput
   4. Improve Performance 
   
   KafkaProducer(
    bootstrap_servers='localhost:9092',
    batch_size=16384,
    linger_ms=5
)

-----------------------------------------------------------------------------------------------------------------

=> Retry 
  
  KafkaProducer(retries =5)
  
  if fails , retry 5 times 
  
----------------------------------------------------------------------------------------------------------------

=> Idempotent Producer 
   
   KafkaProducer(enable_idempotence = True) 
   
   Prevent duplicate message

-------------------------------------------------------------------------------------------------------------

=> What is Idempotent Producer 
   
   -> An idempotent producer ensure that duplicate processing are not written  even if retry occur , by assigning a unique sequence 
      number to each message.
      
=> Batching in Kafka Producer 
    
    -> kafka producer batches multiple message together before sending to improve throughput and reduce network overhead
 
=> What is batch.size?
 
    -> It controls the maximum size of a batch. Larger batches improve throughput but use more memory.
    
=> How to achieve high throughput in producer?

    -> By increasing batch size, using compression, enabling asynchronous sends, and tuning linger time.
    
=> What is linger.ms?

    -> It defines how long the producer waits to accumulate messages before sending a batch. Higher values increase batching but 
        add latency.

=> What is compression in Kafka producer?
   
   -> Compression reduces message size to improve throughput and reduce network usage. Kafka supports gzip, snappy, and lz4.

=> What happens if broker is down?

  -> The producer retries sending messages based on retry configuration. If retries are exhausted, the send fails.
  
=>  What is sticky partitioning?

    -> Sticky partitioning keeps sending messages to the same partition for a short time to improve batching efficiency.

       This is high-level knowledge  
   
  
             
    

      
                                  

"""