"""   
=> TLS (Transport Layer Security)
    
    -> It is transport protocol that run on top of TCP and provides 
         1. Encryption
         2. Integrity
         3. Authenication

--------------------------------------------------------------------------------------------------------

=> Working 
  
  1. Client Hello 
     
     => Client sends
        
        1. Supported TLS version
        2. Cipher suits (Encryption)
   
   2. Server Respond
        => Server repsond with 
          
          1. Selected TLS version
          2. KEy share (public key for key exchange)
   
   3. SSL Certificate 
       => Server sends 
        
        1. SSL / TLs certificate
        2. Proof it owns the private key
        
        
        => Client verifies 
           
           1. Certificate 
           2. Domain match
           3. Certificate not expired 
    
    4. Key exchage 
            
            1. Both side compute a shared secret using 
                -> client Private key
                -> Server public key
   
   5. Session key generated 
   
   6. Secure communication start 
       
       -> Http become HTTPS

-------------------------------------------------------------------------------------------------------

=> TLS 1.3
    
    -> Faster handshake   
    -> One round trip 
    -> TLS old 2 round trip                                  
         
"""