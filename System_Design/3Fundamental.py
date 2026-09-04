""" 

=> Performance Metrics



    1. Latency 

        -> Latency is the time it take for a request to travel through system

        latency = Delay


        Client -> Request -> server -> Request -> db -> Result -> server -> Respones -> client 

        network to server = 20ms
        server processing = 50ms
        db query = 30ms
        response back = 20ms


        total latency = 120ms

    2. Througput 

       -> Amount of work a system can complete in a given time

       -> usually measure  in

           1. Request per second 
           2. Txn per second 
           4. Message per second 
           5. MB per second


        -> Example 

            suppose an api , processs 1000 request per second 

            thorughput = 1000 request/sec

    3. Response Time 

       ->   Response time is the total time from when a user send a request until they receieve 

            the complete response

           Response time = Network Delay + Queue waiting time + Processing time + Db time + Response transfer time


    4. Bandwidth 

       -> Bandwidth is the maximum amount of data that can be transmitted per unit time

       -> measured in

           GBps
           MBps


       -> Example 

          Internet connection = 100mbps

          maximum capacity = 100 Mbps


          
=> Bandwidth Vs. Throughput 


   -> Bandwidth is the theortical maximum 

   -> Throughput is the acutal amount acheieved



   5. Concurrency 

      -> Is the ability to manage multiple task at the same time , even if they are not literally 
         executing simultaneously 

   6. Parallelism 

      -> Means multiple task actually execute at the same time , typically on different CPU
        core and machine

   7. Resource Utilization 

      -> Performance also depend on efficient resource usuage

         1. CPU utilization 
         2. Memory usuage 
         3. Disk I/O

         4. network I/O

   8. Queue time

      -> Some request wait before processing

          Request -> waiting in queue -> Server processes                 


"""