""" 

=> Cross-Site Request Forgery

    -> CSRF is an attack where a malicious website  tricks a user browser into sending an 
       authenticated reques to another webiste where the user is already logged in


=> Why this happen 


  -> Browser automatically attack cookies to request for the cookie's domain



  User
 │
 │ Login
 ▼
Bank
 │
 │ Cookie Stored
 ▼
Browser
 │
 │ Visit evil.com
 ▼
Evil Website
 │
 │ Hidden POST Request
 ▼
Browser
 │
 │ Cookie Added Automatically
 ▼
Bank
 │
 │ Executes Request
 ▼
Money Lost
       





"""