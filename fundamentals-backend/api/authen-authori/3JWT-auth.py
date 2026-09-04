""" 

=> JWT Token 

   -> JSON WEB TOKEN

   -> IT is just a string that contain information about user


   -> it has three part 

      1. Header

           -> Contains metadata

             {algo : "HS256",
             "typ" : "JWT"}

      2. Payload 

         -> container claims (information)

           {
           
           "user_id"  : 10,
           "username" : "parveen",
           "role"     : "admin"
           
           }       
       
        -> The payload is base64url-encoded , not encrypted. Anyone with the token can decode it 
           never put password or other secrets in it

      3. Signature

         -> Signature prove that the token has not been modified


=> Is JWT Encrypted 

    -> No JWT Is signed , not encrypted

    -> anyone decode the header and payload

=> Why do we need signature 

   -> To ensure the token has not been modified


=> How does server verifies the signature

   -> Server recompute the signature using its secret key and compares it with signature receive
      in the token

=> Does server store jwt 

   -> It only store 

       1. Secret key 


=> What happen if the payload changes 

    -> The signature become invalid


=> What if a JWT is stolen

  1. if a valid jwt token is stolen , an attacker can use it to impersonate the user until 
     the token expires or is revoked


     JWT is Bearer token

       -> Whoever posses the token can use it 

     -> so server does not know whether the request is come from you or attacker 

        server only check 

           signature is valid 
           token has not expired
           claims are valid  

   2. Solution 

      1. short lived token 

          -> Never make access token valid for hours or days

                banking = 5 minutes 
                enterprises aaps = 10-15 minutes 

                social apps = 15-30 minutes

      2. Use referesh token 

          -> do not make make user log in every 15 minutes

          login -> access token (5 minutes) -> refersh token (30 days)

          -> when access token expire

            client -> Post/referesh / New access token

      3. Store token securely 

         -> never store jwt like this 

             local storage


         -> better httpscookie only 


       4. Always use HTTPs


       5. Referesh token rotation 

          -> every referesh should issue

             old referesh token -> new referesh token


      6. Keep referesh token in database


           refresh token

             id 
             user_id 
             token_hash
             expire_at
             revoked 
             device
             ip
             created_at

      7. allow logout

         -> JWT itself cannot be destroyed

            logout -> revoke refersh token -> delete cookie -> access token expire in 15 min

      8. Blacklist token

         store revoked jwtids in redis



=> JWT is stateless , how do you implement logout

   1. first the problem is JWT is stateless , server does not store access token,
      once token is issued , it remains valid until it expire.
      because of that server cannot simply delete an access token during logout


   Step 1. Revoke The Refersh Token

       -> Suppose the db contain

           referesh token 

           id | user_id | token_hash| revoked   
            1    10          abc        false 


           POST/Logout

           -> server 

           token.revoked = True 
           db.commit()

    Step 2. Delete token from the client

          -> Client remove 

              Access token 
              Refersh token

              or clear HTTPS cookie by sending 

              response.delete_cookie("referesh_token)


=> Can you invalidate the access token immediately 


   1. Short-lived Access Token


       The access token naturally expire soon , no new access token can be issued


   2. Blacklist the jwt token

      -> include a unqie JTi ID in JWT 


      on logout 

        -> for every request 


           if redis.exist("jti"):
               raise HTTTPexeception(401)    




"""