""" 

=> What is System Design 

    -> System Design is the process of designing a software system that solve a real-world 
       problem while meeting requirement like scalability , reliability , performance 
       security and maintainability.


     -> In simple worlds , is the blueprint  of how software components work together to solve a real 
        problem


     -> A real example 

        Imagine we are building whatsapp platform

        we do not immediately start coding

        first we ask 

             1. How will user send message 
             2. Where will message be stored
             3. What if 1 billion users use it simultaneously 
             4. what happen if server crash
             5. how to keep data secure


=> What problem system design solve 

    1. Scalability 

       -> Can the system handle growth

           today 100 users , tomorrow 100 millions users

    2. Relability 

       -> If one server crash 

           can user continue using the application

           Server A crash , server B working , application still works

    3. Availability

       -> Is the application always online

    4. How fast is the response

       user click login -> Reponse in 40ms , instead of 8 second

    5. Fault tolerance 

       -> Suppose a database crash

            does the application stops

            or does another db takes over 

    6. Security 

       -> how do we protect

          passwords , credit cards , message , personal message

    7. Maintainability 

       -> can we addd 

          1. New features 
          2. fix bugs 
          3. replace component

          without breaking the entire application                                  



"""