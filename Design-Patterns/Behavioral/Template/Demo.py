""" 

=> Template Design Pattern 

    -> The Template method define overall algorithm (workflow) in base class while
       allowing subclass to customize specific step without chaging the algorithm's
       structure

     -> Parent decide the process , child decide some of the steps


     -> Advantage 

        1. Eliminate duplicate code 
        2. Ensure a consistent workflow 
        3. Making adding new variant easy 
        4. Centralize common logic 
        5. Improve maintainability

     -> Disadvantage 

        1. Inheritance is required 
        2. Changes to template method can affect all subclass
        3. Not suitable if every step varies significantly     



"""