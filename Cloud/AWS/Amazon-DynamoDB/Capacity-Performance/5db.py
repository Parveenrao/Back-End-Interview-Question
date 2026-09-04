""" 
=> Why are Eventually Consistent Reach cheaper 

    -> Eventuall consistent reads are cheaper becuase DynamoDb can return from any 
       availabe replica without waiting for all replica to be synchronized. This reduced 
       coordination , lower latency and allowsAWS to serve more read request with same
       infrastructure 


       1 strong conisistent read = 1RCU(4kb)

       2 eventual consistent read = 1RCU(upto 4kbb each)

       in other words an eventually consistency read cost half as much as a strongly consistent
       read

=> Why it is cheaper 

   -> With eventually consistent reads 

       1. Any up-to-date enough replica can serve the request 

       2. There is less coordination between replicas

       3. read traffic is spread across more replica

       4. AWS can serve more reads using the same hardware 


     Thats why AWS charge half the RCU for eventual consistent reads


=> Suppose application perform 10,000 reads/sec 

    Strongs reads -> 10,000 RCUs needed 

    Eventually reads -> 5,000 RCUs needed 


"""