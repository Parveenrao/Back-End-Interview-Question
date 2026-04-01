"""   TCP  => Transmission Control Protocol 
       
    
=> TCP is reliable communication protocol used on the internet 
    -> It ensures 
        1. Data arrive correctly 
        2. Data arrive in order 
        3. Data is not duplicated 
        4. Lost packets are transmitted 
        
    TCP operate at Transport layer of OSI model 
    
    -> Example:

       When you open:

       https://google.com

       Your browser communicates using:

       HTTP → TCP → IP

       TCP guarantees that the HTTP data arrives safely.    
--------------------------------------------------------------------------------------
1. Why TCP is exit 
   -> Internet is unreliable 
       
       Packets can be lost , out of order , be duplicated and delayed
       
    Example :   
    
            You send: HELLO

               TCP sends packets:

                 Packet 1: H
                 Packet 2: E
                 Packet 3: L
                 Packet 4: L
                 Packet 5: O

                 If packet 3 is lost:

                 TCP detects it and resends packet 3.   

    Websites use TCP (Reliable over Speed)
    Netflix use UDP  (Speed > Reliability)
    
2. TCP Connection 

   -> Before sending data , TCP creates a connection , called 3-way-handshake
   
         3-Way Handshake

         Client → Server : SYN     (Clinet ask to connect  SYN - synchronize)
         Server → Client : SYN-ACK (server acknowledgment - ACK)
         Client → Server : ACK     (Client confirms )     
                                  
                                   Now connection is eastblishment 

3. TCP Packet Structure 

              -> Every TCP packet contains a header.


                    ----------------------------|
                        Source Port             |
                        Destination Port        |
                        Sequence Number         |
                        Acknowledgement Number  |
                        Flags (SYN, ACK, FIN)   |
                        Window Size             |
                        Checksum                |
                        Data                    |              
                    ----------------------------|

              -> Sequence Numbers

                TCP tracks every byte.

                  Example:

                  Packet 1 → seq = 1
                  Packet 2 → seq = 1001
                  Packet 3 → seq = 2001

                ACK = 2001

                Meaning: -> "I received everything until 2000"

                If packet missing: -> TCP requests retransmission.

4. Congestion Control

     -> If the internet is crowded, TCP slows down.

                 Algorithms used:

                 • Slow Start
                 • Congestion Avoidance
                 • Fast Retransmit
                 • Fast Recovery


                Example:

                Sending rate increases like:

               1 packet ---- 2 packets ----- 4 packets ---- 8 packets   --- 16 packets

               If packet loss happens:

               Reduce speed

              This prevents internet congestion collapse.


















"""