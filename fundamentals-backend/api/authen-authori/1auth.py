""" 

=> 1 Session 

    -> A session is a way for the server to remember who you are across multiple HTTP request.

    -> HTTP is stateless , every request is completely independent

    -> server does not who you are , whether you logged in or not


=> Solution 

    -> After successfully login , server creates a session

    -> server memory -> Session ID -> A9XZ12345 -> {
                                                      user_id : 20,
                                                      username : "Parveen",
                                                      role : admin}

            server store this information

            then it send only the sessionID back to the browser 


=> Flow 

   1. Step 1 Login 

       -> Browser  POST/LOGIN

          username + password  

        -> server check db

   2. server create session 

        -> server creates 

            SessionID -> AXYDBJS

            store {
                      user_id : 20 ,
                      role    : admin}

   3. Send cookie

      Server respond

        HTTP/1.1 200 OK

        Set-Cookie:

        session_id = ADISHIJDSIK

     Browser automatically save it

     -> browser only save session id

    4. Next Request

       -> browser automatically send

          Cookie:

          Session_id = A6789GHJ


    5. Server lookup session

       -> server receives , SessionID

       -> Search session Store

       -> Request is authenticated


=> Where are session stored

    1. Memory

        -> fast , but not good because session disapper when the server restarts and are not
           shared across multiple servers

   2. Database


   3. Redis (Good)


=> Session Expiration 

   -> session shoud expire after some time

        user must log in again

   -> logout 

      -> when user click logout

         server deletes ID from redis and server store     






"""