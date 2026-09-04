""" 

=> Observer Design Pattern
 
     -> An Observer Pattern is a behavioral design pattern that define one to many dependency between
        objects 


     -> When one object change its state , all objects that depend on it are automatically notified 
        and updated 

     -> Instead of every object contantly checking whether something has changed (pooling) , the object 
        itself sends notification to everyone who is interested 


     -> Example 

         1. Imagine you subscribe to a Youtube channel 

         2. Youtube channel uploads a new video 

         3. Every subscriber recieve a notification 


     -> Core Terminology 


        1. Subject (Publisher)

           -> This is the object thats own the data 

              a. Store state 
              b. Register observer 
              c. Remove observer 
              d. Notify observer 

        2. Observer 

            -> Objects interested in updates 

              a. Register with subject 
              b. Recieve notifications 
              c. React to changes 


     -> Advantage 

        1. Loose coupling -> The subject doesn't need to know implementation detail of observer 
        2. Easy to extend -> Add new observer without changing the subject 
        3. Automatic updates -> Subscriber stay in sync with latest data 
        4. Reusable design  -> work for many event driven architecture 


      -> Drawback 

         1. If there are many observer , notifications become expensive 
         2. Notifications order may matter but is not always guranteed 

         3. If observer are not removed when no longer needed , they can cause memory leaks 

            (in long-running applications)                                 



"""