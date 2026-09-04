""" 

=> HTTP Caching 

   -> Http caching is a mechanism where the server tells the client (browser) how long a response
      can be stored and when it should check for update

   -> Instead of downloading the same resources every time

      browser -> GET/logo.png -> server -> logo.png


      Browser can store it locally 

      Browser -> local cache -> logo.png

      next request may never reach the server 


=> Why do we need HTTP cache 

   -> Imagine our website has 

      1. Logo
      2. CSS
      3. Javascript
      4. Icons


   -> every page refersh download everything again 

      1. waste bandwidth 
      2. server resourcess 
      3. user time



=> WIth HTTP caching

    first visit -> download files -> stored in browser


    next visit 

    browser -> used cached files -> instant page load 


=> Where is HTTP cached stored

   -> chrome -> cache storage -> logo.png/style.css/main.js


=> How does browser decide 

   -> Server send http headers

      http/1.1 200 ok

      cache-control max-age = 3600

      browsers read 

      cache for 3600 seconds


   -> browser -> need style.css -> still valid -> yes -> load locally 


   -> if the cache expired

      browser -> cache expired -> ask server -> has this file changed 

      server can either 

        -> Return a fresh file 

        -> say it is unchanged (304 not modified )


=> Advantage of HTTP caching 

   1. Faster loading

       instead of downloading -> rendering

       browser simply reads from disk or memory

   2. Less bandwidth

      -> instead of downloading 5mb css every refersh

      it downloads it only once until the cache expire 

   3. Reduced Server load

       -> if 1 million users all request the same logo 


       -> with http cache 

             reaminig users (or repeat visit by the same user ) use their cached copy        


"""