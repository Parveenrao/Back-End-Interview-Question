""" Authenication ---> Verifying who are you 

    you enter email + password  -> Succeed -> authenicated 
 
---------------------------------------------------------------------------------

1. Password based Authenication 

    -> You enterd email and password
       
       server check in db (hased password)
       
       
       Password never stored in plain text
       
       
       -> Simple to implment
       -> Widely used 
       -> Weak password ,, brute force attacks
       
-----------------------------------------------------------------------------------------

2. JWT Based 

--------------------------------------------------------------------------------------------

3. Session Based Authenication 
   
   Instead of sending identity every time  , server says  send me session id 
   
   -> Flow 
      
      server create a session 
      store it in DB/Redis/memeory 
      Give client a session ID 
      CLient send its in every request

---------------------------------------------------------------------------------

4. Login with Third - Party Application 

   -> We trust third party application to authenicate the user , instead of handling password manually
   
       Login with google
       Login with github
       Login with facebook
       
    1. User → /login
    2. Backend → Redirect to Google
    3. User logs in
    4. Google → /auth?code=123
    5. Backend → Exchange code
    6. Google → Tokens
    7. Backend → Verify ID token
    8. Backend → DB (create/find user)
    9. Backend → Generate JWT
    10. Backend → Send JWT
    11. User → API with JWT
    12. Backend → Verify JWT         
             
             
-------------------------------------------------------------------------------------------

5. Multi Factor Authenication 

   You login with email and password , if correct then  we move to next stage , like SMS , Email             
       
       
       
       
       """