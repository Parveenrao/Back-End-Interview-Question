""" 

=> Bridge Design Pattern

    Structural Design Pattern that separates an abstraction from its implementation so that 
    both can change independently 

    

=> Why do we Need Bridge Pattern 

   Imagine we are developing a notification system

   we have 

   1. Email Notification 
   2. SMS Notification 
   3. Push Notification 

   Now notifications can be 

   Urgent 
   Normal


   -> Email Notification
   -> SMS Notification
   -> Push Notification

   -> UrgentEmail Notification
   -> UrgentSMS Notification 
   -> UrgentPush Notification

   -> NormalEmail Notification 
   -> NormalSMS Notification 
   -> NormalPush Notification


   -> Already 9 classes 

   Now add slack notification , 3 more class 

   Now add Schedule notification , 3 more class

   This is called Class Explosion

=> Idea Behing Bridge Pattern

   -> Instead of inheritance 

   -> Split the problem into two independent hierarchies 


     Notification  ----> Notification Sender 


     One hierarchy decide , what notification is 

     Another hierarchy decide how notification is sent 


     Notification -> Urgent Notification , NormalNotification 

     Sender -> EmailSender , SMSSender , PushSender , SlackSender



=> Bridge


     Bridge Pattern is a structural design pattern that decouples an abstraction 
     from its implementation by connecting them through composition instead of inheritance. 
     This allows both the abstraction and the implementation to evolve independently, 
     avoids class explosion, and enables implementations to be swapped at runtime.
"""

"""" 



             Notification (Abstraction)
                       |
          -------------------------
          |                       |
     UrgentNotification      NormalNotification
                       |
                 uses (Bridge)
                       |
                    Sender
          -------------------------
          |          |            |
         Email      SMS        Slack



"""