""" => JWT (Json Web Token) is a self - authentication token 
    
        -> Instead of storing  session data on server , the token itself contain information 
     
     
    -> JWT FLOOW 
    
           User --> Login 
                |
           Server Verify Credentials 
                |
           Server generate JWT
                |
           Client store JWT 
                |
           Clinet Send token in Request 
                |
           Server Verify token 
        
        No sesson lookup 
        
     
    -> JWT Structure 
       
        JWT has three main part ---- Header  , Payload , Signature 
        
        1. Header  
           -> Contains metadata 
             
              {
               "alg": "HS256",
               "typ": "JWT"
              }                       
        
        2. Payload 
           
            -> Contains data 
                 {
                  "user_id": 10,
                   "email": "user@gmail.com",
                   "role": "admin",
                   "exp": 1700000000
                 }
     
        3.  Signature  
       
              ->  Signature is generated using:

                       hash(header + payload + secret_key)
     
             -> Where should JWT be stored?

                        Possible places:

                         localStorage
                         sessionStorage
                         HttpOnly cookies
                         memory
                         secure mobile storage

                         Most secure for browsers:

                         HttpOnly cookies
     
              -> Full verification FLow 
              
              
                       Client sends request
                               ↓
                      Server extracts token
                               ↓
                     Split token into 3 parts
                               ↓
                      Recalculate signature
                               ↓
                        Compare signatures
                               ↓
                        Check expiration
                               ↓
                         Extract user info
                               ↓
                         Allow request
     
     
 """