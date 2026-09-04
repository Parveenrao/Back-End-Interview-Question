""" 

=> Cookies 

   -> An HTTP cookie is a small piece of data that a server store in a user's browsers.

   -> Browsers automatically send that back to the server with future request to the same website 


=> Why do we need cookies 

   -> HTTP is stateless

   -> means every request is stateless

   -> example 

       GET/login , server -> 200 OK

       later GET/profile , server does not automatically know , who are you , did you log in

   -> without cookies , server treats every request as coming from a new user 


=> How Cookies work

   1. User log in

      POST/Login -> user send username and password

   2. Server verify credentials

      if correct 

         HTTP/1.1 200 Ok

         SET-cookies : session_id = abc123 


   3. Browser store it


   4. Future request

     -> when the browser request another page 

         GET/profile

         browser automatically includes

         Cookie:abc124


=> What can cookie store 


   1. Cookies typically store

      -> SessionID 

      -> Login tokens 

      

=> Cookies Types 


   1. Session Cookie

      -> Live only until the browser close


   2. Persistent cookies 


      -> Has an expiration date

   3. Secure cookies 

       Only sent over HTTPS


   4. HTTPonly cookie         

      -> javascript cannot read it , helping protecting against XSS attacks

   5. Same site cookies 

      -> Controls whether cookies are sent with cross-site request 

         Set-Cookie:
         session=abc;
         SameSite=Strict   
         




"""