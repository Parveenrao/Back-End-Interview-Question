"""  
=> Websockets 
     
     -> Web-Socket is a protocol like (HTTP , TCP)
     
     -> It enables 
        1. Persistent connection
        2. Full duplex connection (both side talk anytime)
    
    
    -> Websocket is a communication protocol that provide a continous , bidirectional communication over a single TCP connection


---------------------------------------------------------------------------------------------------------------------------------

=> Where it sits in networking 
    1. Application Layer -> HTTP / Websockets
    
    2. Transport Layer -> TCP
    
    3. Network Layer -> IP
  
  -> So websockets runs on TCP
      -> IT is reliable , ordered , no packet loss

----------------------------------------------------------------------------------------------------------------------

=> Core Properties 
   
   1. Persistent 
       -> Connection stays open
       -> No repeatedly handshake 
   
   2. Full-Duplex 
       
       -> Client --- Server both send anytime 
   
   3. Stateful 
       
       -> Server keep track of connections 
   
   4. Low Latency 
       -> No HTTP overhead

-----------------------------------------------------------------------------------------------------------------------

=> Working Of Websocket 
    
    1. Client send HTTP Request with special headers 
       
       upgrade : wesocket
       Connection : upgrade
       sec--websocket-key
     
     -> This tell server , Switch protocol from HTTP -> WebSocket
    
    2. Server Upgrade Connection
       
       -> Server respond 
       
          101 Switching Protocol 
          Accept Upgrade 
       
       -> After this HTTP Gone 
          Connection become persistent TCP Channel 
    
    3. Connection Stays Open 
       
       -> No more request / response
       -> Both side can send data anytime 
           Called full duplex communication 
           
    4. Data is sent as frames , not message 
        
        -> One message -> multiple frame possible 
    
    5. Connection Health 
       
       Server -> Ping 
       Client -> Pong 
       
       if no response - connection is dead 
    
    6. Closure Connection 
        -> Either side can close conection 
        
        -> TCP connection terminated 


----------------------------------------------------------------------------------------------

=> Limitation 

    1. Scaling is Hard 
       
       -> Each connection is tied to one server 
          
          Horizontal scaling is complex
          
          Solution -> Pub/sub model 
    
    
    2. High Memroy and Resource Usage 
       
         -> Each user open TCP COnnection 
         
         -> Server store 
            
            socket , buffer , metadata 
            
         -> 100k users = heavy ram use 
    
    3. No Built-In-Reconnection 
        
        -> If connection drop  -> gone 
        
        
        -> We must implement 
            
            1. Auto reconnect
            2. Session recovery 
            
            
      -> Websocket give connection , not reliability                    
    
    4. No message guranteee 
        
        -> Even though TCP connection is reliable  
          1. No retry logic 
          2. No ack system 
          
   
   5. Security is manual 
      
      1. No built in authentication 
      
      2. No rate limiting 
      
      3. NO JWT validation
   
   6. Proxy / Firewall issues 
   
      -> Some network block websockets
   
   7. BackPressure Problem 
      
      -> CLient send to fast 
      
      -> Server can not keep up 
      
      -> Memory issue
   
   8. Stateful nature 
       
       server must track
        
        1. Connection
        2. users 
        3. sessions
    
    9. Idle connection cost 
    
      -> Even idle connection use resource 
      
      1M idle connection doing nothing  -> still expensive 



------------------------------------------------------------------------------------------

=> use Websocket when 

   
   1. Live chat
   2. live update       
                                                                    
                          
"""