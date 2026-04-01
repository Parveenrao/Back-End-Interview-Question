""" COOKIES AND SESSION

    1. Why Cookies and Server Exist 
       
       -> HTTP is Stateless 
         
          Request1 --> Login 
          Request2 --> Open profile
          
          Server does not  remember  the user between request
          SO we need a way to identify  the same user across between multiple request 
          
    
    2. COOKIE 
     
       -> Cookie is a small piece of metadata stored in user browser
       
          The server send a cookie --> browsers store it --> browsers send it back with future request
          
          Example 
          
          1. Response from server 
             
             Set-cookie : session_id = abc123
          
          2. Browser stores it 
             session_id : abc123 
             
          3. Next Request automatically includes 
             
             Cookie : sesson_id  = abc123
       
       -> COOKIE FLOW 
          
          1. Client log-in
          2. Server verify credentials
          3. Server create cookies 
          4. Browser store  cookies
          5. Browser send cookies with every request 
          
        
       -> Types Of Cookies 
       
          1. Session cookies 
          
             -> Temporary cookies 
             -> They disapper when browser close 
                
                 Set-Cookie: session_id=abc123
          
          2. Persistent cookie 
          
              -> Stored until expiry 
                  
                  Set-Cookie: user_id=10; Expires=Wed, 10 Jun 2026
           
           3. Secure cookie 
           
              -> Only sent over HTTPs
           
           4. HTTPs only cookie                         
          
              Cannot be accessed by JavaScript (prevents XSS attacks).

              Set-Cookie: session_id=abc123; HttpOnly
          
          
    
    3. Session       
    
        -> A session store user data on server 
        
        -> Instead of store everthing in browser , we store in the server
        
        -> Browser store only the session ID 
        
       
      ->  Session FLow 
       
        1 User logs in
        2 Server creates session
        3 Server stores session in database / memory
        4 Server sends session_id cookie
        5 Browser sends session_id on every request
        6 Server retrieves session data  
       
       
       -> Where Session are Stored 
         
          1. Database 
          2. Memory 
          3. Redis 
          4. File System 
          
       
       -> 9. Example Login Flow (Session Based)
              
            Step 1: Login request
              
              POST /login

              Body:

              {
                "email": "user@gmail.com",
                 "password": "123456"
                      }

            Step 2: Server verifies user

                     Server creates session:

                     session_id = abc123

                       Stored in Redis:

                      abc123 → user_id=10

            Step 3: Server sends cookie
                   
                   Set-Cookie: session_id=abc123

            Step 4: Browser sends cookie later

                     GET /profile
                     Cookie: session_id=abc123


            Server checks session store → identifies user.      
          
          
          
          
          
          
          """