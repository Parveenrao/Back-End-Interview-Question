"""   => DNS (DOMAIN NAME SERVER)

           -> DNS is a system that convert human -readable domain into IP addresses.
               
               google.com → 142.250.183.206
            
            -> Computer communicate using IP addresses  , but human remember domain name
               
               So DNS act as phonebook of internet 
               
       
       -> Why DNS Exist          
       
           

              Imagine if DNS didn't exist.

              To visit a website, you'd have to type:

              http://142.250.183.206

              Instead of:
 
              http://google.com

              DNS solves this by mapping:

              domain name → IP address
              
        
        -> DNS LOOKUP Process 
           
            when you type -> www.google.com   
              
            System perform DNS lookup 
            
                      Browser
                         ↓
                      OS Cache
                         ↓
                    DNS Resolver
                         ↓
                      Root Server
                         ↓
                      TLD Server
                         ↓
                    Authoritative DNS
                         ↓
                   IP Address returned     
                   
             1. Browser Cache 
                 -> Browser first check if it already known IP address   ex ->  www.google.com → 142.250.183.206     
                    
                    If found  , DNS lookup stops here
              
             2. OS Cache 
                
                 -> IF the browser does not kwown , os check its cache 
                      ipconfig /displaydns
                  
                  If found , return ip 
             
             3. DNS Resolver 
                
                 -> if not cache , request will goes to DNS resolver 
                    Usually provided by ISP and Public DNS 
                    
                    Examples:

                   Google DNS → 8.8.8.8

                   Cloudflare DNS → 1.1.1.1

                   The resolver will now search the internet.                     
                   
             4. Root DNS Server 
             
                   The resolver asks a root DNS server.

                    There are 13 root server clusters worldwide.

                    Example question:

                    Where is google.com located?

                    Root server responds:

                    I don't know the IP, but ask the .com server      

             5. TLD Server (Top Level Domain)
                                 Examples:

                                    .com
                                    .org
                                     .net
                                     .io

                                 Resolver asks:

                                 Where is google.com?

                                  TLD server responds:

             
                                  Ask the authoritative server for google.com

             6.  Authoritative DNS Server
             
                  This server contains the actual DNS records.

                   Example:

                   google.com → 142.250.183.206

                   It sends the IP address back.
                   
             7. Response Returned 
             
                  The IP travels back:

                  Authoritative Server
                         ↓
                    DNS Resolver
                         ↓
                        Browser      


                      Now the browser knows the IP.

                      It can connect to the server.





"""