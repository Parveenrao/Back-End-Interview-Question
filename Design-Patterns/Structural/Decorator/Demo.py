"""" 

=> Decorator Design Pattern 

   -> Structural Design Pattern that allows you to add new functionallity to an object 
      dynamically without modifying its existing code 

   -> Wrap the original object inside another object (decorator) that add extra behaviour


=> Why do we need Decorator

    1. Suppose we have a coffee class , later we want to add 

       1. Milk
       2. Sugar 
       3. Wipped cream

    2. Instead of creating many subclass

       Milkcoffee
       Sugarcoffee
       Milksugarcoffee
       Milksugarwhippedcreamcoffee

      we can use decorator to add features at runtime    


"""