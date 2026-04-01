"""              
    => HTTPS (HyperText Transfer Protocol Secure)
      
        -> HTTPS = HTTP + TLS
        -> HTTP = HypeText Transfer Protocol  
        - >TLs  = Encryption lyaer that secure the connection 
        
    =>    Application Layer     → HTTP
          Security Layer        → TLS
          Transport Layer       → TCP
          Network Layer         → IP    
    
    => Without HTTPs
       
       1. Read data (attackers) , http send plain data anyone can see on the network 
       2. Modify data --> attackers could damage
    
    
    => Working of HTTPS 
    
      1. when u viist   https"//example.com   
      
      2. TCP Connection 
         -> first browser extablished tcp connection 
         
      3. TLS Handshake begins 
      
           -> plain text 
             client -> server
             Clinethello 
             
            -> client sends
               supported tls algorithms
               supported encryption algorithm
               random number
               
            -> Server respond
               Serverhello 
               certificate
               public key 
               selected encrpted algo
            
            -> Browser verify certificate 
                if verification fails 
                browser shows warning 
            
            -> Now both side generate a shared secret key 
            
                 secret key is generated independently , 
            
            -> now connection is secure
    
    
    =>       Browser
              |
           DNS lookup
              |
         TCP handshake
              |
         TLS handshake
              |
       Encrypted HTTP request
              |
       Server processes request
              |
       Encrypted HTTP response                           
    



















"""