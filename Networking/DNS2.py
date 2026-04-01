"""  => DNS Caching 

         To reduce DNS queries, results are cached.

         Each DNS record has TTL (Time To Live).

       
       
    ->  DNS and Load Balancing

           DNS can also distribute traffic.

            Example:

            google.com → multiple IP addresses

             Example response:

               142.250.183.206
               142.250.183.207
               142.250.183.208

             Clients connect to different servers.

              This is called DNS load balancing.




                                 User
                                  ↓
                                  DNS
                                  ↓
                                  CDN
                                   ↓
                            Load Balancer
                                   ↓
                              Web Servers
                                   ↓
                                Database
"""
  