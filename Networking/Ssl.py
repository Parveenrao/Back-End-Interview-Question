"""  
=> SSL
    -> Secure Socket layer 
     
     -> It is technology that encrypt communication between client(browser) and server(webiste) so that no one read or 
         tamper data between them
         
     -> Replace by TLS(Transport Layer Security)

-----------------------------------------------------------------------------------------------------------------------------

=> Without SSL 
    -> Data is sent as plain text
    -> any one can read or tamper

=> With SSL
   -> Data is sent as encrypted 
----------------------------------------------------------------------------------------------------------------------------

=> Working OF SSL
     
     1. Client(browser) connect to server (say google.com)
     2. Server sends its SSL certificate
     3. Client verify the certificate 
     4. Both agree on encryption
     5. Secure communication starts
----------------------------------------------------------------------------------------------------------------------------

-> Public key Vs Private key 
   
   1. Public key --> shared with everyone
   2. Private key -> Keep secret on server 

-> SSL Certificate 
    
    1. A digital certificate the proves , this sever is legit 

-> HTTPS
   
   HTTP + SSL = HTTPS        
                        
"""