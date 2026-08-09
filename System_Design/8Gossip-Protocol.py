""" 

=> Gossip Protocols

   -> A gossip protocols is a communication mechanism used in distributed system where
      each node exchange information with a few randomly selected node.

   -> Over the time , information spreads to the entire cluster , just like rumor
      spread amoing people

    -> Real life example 

        1. Imagine there are 100 students in college 

        2. Principle announce Tommorrow is holiday

        3. Instead of calling  100 students individually 

           -> Principle tells 2 students 
           -> Those 2 students each tell 2 more students 
           -> Those students tell 2 more 

           -> The process continue 


=> In Distributed System 

   1. Suppose we have database cluster 


        +---------+     +---------+     +---------+
        | Node A  |     | Node B  |     | Node C  |
        +---------+     +---------+     +---------+

        +---------+     +---------+     +---------+
        | Node D  |     | Node E  |     | Node F  |
        +---------+     +---------+     +---------+

   2. Each node store data 

   3. Now suppose  Node A discover the Node E has crashed 

   4. How should everyone know


   -> Solution 1 , Broadcasting 

       Node A send message to every Node 

       with 10000 nodes , (N-1) message

       A sends 9,999 messages

       if many nodes do this frequently , the network become overload 


   -> Solution 2, Gossip Solution 

      1. Node A randomly chooses only a few nodes 

         A -> C , F 

         C -> B , D

         F -> E 

         B -> G 

         D -> H

         The information is spread like a rumor , 

         Eventually , every node knows that Node E is down


=> A gossip protocol is a decentralized communication protocol where 
   each node periodically shares its known information with a small
   number of randomly chosen peers, allowing information to spread 
   throughout the cluster efficiently.  

=> What Information Is Shared 

    1. Usually metadata , not the actual user data 

    2. Node is alive ,

    3. Node has failed 

    4. New node joined 

    5. Heartbeat value 

    6. Software version 

    7. Cluster topology

    9. Schema version


=> Main Characteristics 

   1. Decentralized 

      -> No master server 

      -> every node participate equally 

   2. Random communication

      -> Each node randomly selects a few peers

   3. Periodic 

      -> Every few millisecond or seconds 

      -> Pick peers => Exchange information => Sleep => Repeat 

   4. Eventually Consistent 

       -> Immediately after an event 

         Node A knows.

       -> After a few gossip rounds 

         All nodes know 



=> Why Gossip is Efficient 

   1. Suppose there are 10,000 nodes 

   2. If every node talk to 3 random nodes every gossip round

      10,000 * 3 => 30,000 message 

   3. Instead of 

      10,000 * 9,999 => 100 million message 


=> Where is Gossip is used 

   -> Many distributed system use gossip for cluster membership  and failure detection 

      1. Apache Cassandra 
      2. Amazon DynamodDb
      3. Scylla Db 
      4. HasiCorp Consul 
      5. HasiCorp Serf

"""