""" UDP (User Datagram Protocol)

=> UDP is a transport layer protocol used to send data quickly without gurantees delivery. It sits at the same layer as tcp 
=> UDP send data without establishing a connection and checking if it arrived

1. Characteristics of UDP 

   -> No connection setup
   -> No reliability guranteee
   -> NO packet ordering 
   -> NO congestion control 
   
 -> UPD is often called 'Send and Forgot protocol"
 
Use TCP when accuracy matters.
Use UDP when speed matters.

---------------------------------------------------------------------------------------------------------------------------------- 
 
2. UDP Headers 

     Source Port
     Destination Port
     Length
     Checksum
     Data

----------------------------------------------------------------------------------------------------------------------------------

3. Example  

    Video Streaming

   Streaming platforms use UDP because waiting for lost packets would cause buffering.

  Examples:  YouTube  Netflix
  
  
-> Video Streaming

YouTube
Netflix

When you watch a video, data is continuously sent.

Example:

Frame1
Frame2
Frame3
Frame4

If Frame2 is lost, the player does not wait for it.

It just continues with:

Frame1
Frame3
Frame4

Otherwise video would constantly buffer.

This is why streaming prefers UDP-like behavior.



-> Video Calls

Apps like: WhatsApp , Zoom

Voice and video data are streamed continuously.

If a packet is lost:

small glitch in audio

But the call continues.

Waiting for retransmission would cause delays and echo.

----------------------------------------------------------------------------------------------------------------------------------

4.  How UDP know where to send 

UDP uses IP address + port number.

This information is inside the UDP packet header.


Structure:
Source IP
Destination IP
Source Port
Destination Port
Data

Example packet:

Src IP: 192.168.1.5
Src Port: 50000
Dst IP: 8.8.8.8
Dst Port: 53

That is enough for the network to deliver the packet.

Routers only look at: -> Destination IP

The destination machine then uses:

Destination Port -> to decide which application should receive the data.

So UDP doesn't need a handshake to know where to send.

Example: DNS Request (UDP)

When your computer asks for an IP:

Example DNS server: -> 8.8.8.8:53

Your computer sends a UDP packet:

Src: 192.168.1.10:53000
Dst: 8.8.8.8:53

DNS server replies to:

192.168.1.10:53000

No handshake needed.

Just request → response.




















"""