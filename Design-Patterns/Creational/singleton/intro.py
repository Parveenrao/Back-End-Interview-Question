"""

=> Singleton Design Pattern
   
    -> Creational design pattern that ensure 

        1. Only one instance of class exists through throughout the application
        2. There is a global point of access of that instance




=> Why we need Singleton Design Pattern 

    1. Imagine we are building a backend system 

        -> Authentication service 
        -> Payment service 
        -> Notification service 
        -> Order service 

    All of them need access to the database


              
"""

# without singleton 

class Database:
    def __init__(self):
        print("Connecting to database")

# now every service 

db1 = Database()

db2 = Database()

db3 = Database()

db4 = Database()

"""

=> Problems 

    1. Four db connection 
    2. Wasted memory 
    3. Expensive intialization 
    4. Harder to coordinate shared state 
    5. Different object may have incosistent state



"""

""" 

=> WHat problem does sigleton solve

    1. Instead of creating 

       -> database 
       -> database 
       -> database

    2. Create

        One database

        and everyone use it


        every one share the same object

    3. Singleton guranteee

                db1
     
               db2 ---> Object A

                db3       


"""

""" 

=> WHen we use Singleton 

    1. Logger

       -> Imagine 

          Order servie 
          Payment service 
          Inventory service

        all write logs

    2. Configuration manager

        -> Application starts 

        -> Configuration is loaded once

        -> with singleton , configuration is loaded once

    3. Thread pool

       -> Creating thread is expensive

       -> Better 


           Threadpool

             1. Task1
             2. Task2
             3. Task3

    4. Database connection manager 

       -> most application do not create a new dataabse manager object everywhere . Instead 

          they use one shared manager , which may internally maintain a pool of db connection                     

"""
