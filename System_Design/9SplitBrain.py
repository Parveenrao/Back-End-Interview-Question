""" 

=> Split Brain Problem IN Distributed Sytem 

    -> Split brain is a failure condition in a distributed system where a network partition 
       or communication failure cause two or more groups of nodes to believe they are the 
       the active cluster , allowing multiple leaders or primary node to operate 
       simulataneously and leading to inconsistent or coflicting data 


    -> Split brain occur when communication between node fails , causing multiple  
       leaders to exist simultaneously in a distributed system


=> Example 

   1. In Distributed System

      -> Suppose we have 
       
          Server 1 
          Server 2 
          Server 3

      -> Suddenly network fails

          Server 1 fails 

          Now communication breaks

          Server 1 cannot reach Server 2 and Server 3

          Server 2 and Server 3 cannot reach Server 1


          Ideally

             Only one group should continue

             But if both continue

             Group A 

             Leader  = Server 1

             Group B

             Leader = Server 2


             Now we have two leaders

             This is split brain


=> Why is this dangerous

   -> Becuase both leader start accepting writes

       Db balance = 1000

       CLient 1 -> Connect to Leader A
        
          withdraw = 300

          balance = 700

       Client 2 -> Connect to leader B

          withdraw = 500

          balance = 500

       Now two different db exist 

          Leader A = 700

          Leader B = 500

          which one is correct 

          Nobody knows

          This is called , Data divergence

=> why does split brain happen

   -> Usually becausee of network partition

      Switch failure 
      Router issue 
      Firewall
      Cable cut 
      Cloud AZ failure 
      High latency 
      Packet loss

=> How Distribute  System Prevent Split brain

   1. Quorum 

      -> A leader must recieve vote from more than half of the nodes

         for 5 nodes

         majority = 3

      -> if only 2 node remain connected

          2 < 3

          cannot become leader 

          This prevent two active leader

    2. Leader Election 

       -> Algorithms like

           Raft 
           Paxos
           Zab

        ensure that at most one leader can be elected for a given time, assuming quorum
        rules are followed


   3. Fencing tokens

      -> When granting leadership , the system issues a monotonic incresing token

         Leader A 
         Token = 41

         New leader

         Token = 42

         if the old leader later send a write with token 41 , storage reject it becuase a neweer
         leader already exist 

    4. STONITH (SHoot The Other Node In THe Head) 

        -> If a node appears , isloated another node or a cluster manager forcibly power it 
           off or fences it from shared storage before allowing a new leader to take over 

    5. Read only monitor

        -> Some system allow the minority partition to serve read only but reject write                             



"""