""" 

=> XSS (Cross-Site Scripting)

   -> XSS is a vulnerability where an attacker inject malicous javascript into a trsuted 
      website . That script then runs in other users browser 


   -> XSS is an attack that allows attackers to execute malicious javascript in victim 
      browser 



=> WHy XSS is Dangerous 

   1. Suppose u visit 

       https://facebook.com

   2. An attacker has injected this script malicious

   3. WHen browser loads the page 

       -> Scripts executes 
       -> Read your cookies

       -> send them to attacker 


Attacker
   │
   │ Posts malicious script
   ▼
Website
   │
   │ Stores it
   ▼
Database
   │
   │ Sends it to users
   ▼
Victim Browser
   │
   │ Executes script
   ▼
Attacker gains data/actions           



"""