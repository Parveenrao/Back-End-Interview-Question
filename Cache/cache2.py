"""       =>  Where Cache is Stored       


          1.  Application Cache  
             
              -> simples is inside application Process Memory (RAM)
              
              -> Each server has its own cache
              -> No shared between server
          
          2. Distributed Cache 
             
             -> In large system , cache is stored into external cache server(Redis , Memcached)   
             
               Client
                 ↓
           Application Server
                 ↓
          Redis / Memcached
                 ↓
             Database 
             
             
             
             
             1 Request
               → Redis
               → Cache miss
               → DB
               → store in Redis
               → return

              Next request
              → Redis hit
              
          3. Browser Cache 
             
             cache stored in user browser
             
               -> cache-control  : max-age = 3600
               
          4. CDN Cache 
          
              -> Cache stored in global edge  server close to user
              
              Example --> user in india request image 
                          
                          India cached in India CDN cache
          
          5. Database Cache 
          
              -> Many database internally cache data in memory 
                 
                  1. Mysql buffer pool
                  2. PostgresSQl  shared buffer
                  
                  
                  Application
                     ↓
                Database Cache
                       ↓
                     Disk       
                     
     => Multiple Cache  
     
              User
               ↓
          Browser Cache
               ↓
           CDN Cache
               ↓
           API Server
               ↓
           Redis Cache
               ↓
          Database Cache
               ↓
            Database                               

"""