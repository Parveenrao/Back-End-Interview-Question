""" 

=> Cache-Types 

   1. Client Side Cache 

      -> This is the cache stored inside  the user's browsers

      -> Example , https://shop.com/logo.png

         first time

         browser -> Internet -> Server -> logo.png

         browser save it locally 

     -> next time 

        Browser -> Local cache -> Display image 

        No request goes to the server 


      -> what is actually cached

         1. Images 
         2. CSS
         3. javascript
         4. Fonts 
         5. Static HTML (when allowed)


  2. CDN Cache (Content Delivery Network)

     -> A CDN stores copies of files on servers around the world

     -> Suppose your server is in mumbai

     -> A user from london request 

     -> without CDN

       London -> Mumbai server -> London , Higher latency 


     -> With CDN

        London CDN Server -> Image 


  3. Reverse Proxy cache 

      -> A reverse proxy cache sits in front of your backend

         client -> Nginx -> backend

         if the response is cache , fastapi is not even call


      -> Example 

         Thousand of users request same page


  4. Application Cache 

     -> This caching is done application 

     -> usually done by redis

     -> cached data

         1. User profile 
         2. Product detail 
         3. Settings 
         4. API response
         5. Session data 

   5. Database Cache 

      -> Many database cache recently accessed pages internally 


   6. Distributed Cache 

      -> WHen you have multiple backend server 

         Client -> Load balancer -> Serve A / Server B / Server C

         Each server needs access to the same data 

         Server A -> local cache 

         Server B -> Local cache 

         Server C -> Local cache 


=> Why do we have multple cache instead of just Redis

   -> because each cache solve a different problem 

      1. Browser cache -> reduce repeated downloads  for the same user 
      2. CDN cache     -> server content quickly to user around the world 
      3. Reverse proxy cache -> prevents indetical request from reaching your application 
      4. Application cache (Redis) -> avoid expensive db queries and computations 
      5. Database cache -> speed up database access internally 




"""