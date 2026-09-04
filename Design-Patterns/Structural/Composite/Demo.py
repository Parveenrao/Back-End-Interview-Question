""" 

=> Composite Design Pattern 

    -> Structural Design Pattern that lets you treat individual object and groups of objects 
       in the same way

    -> It is useful when you have tree-like hierarchy (file-system , UI components , organization structure)   

    
    -> Problem it solves 

       Suppose you are building a file system

       A file has a size 

       A folder contain file and other folders


       without composite pattern we need separate logic for files and folders 

       with composite both implements the same interface so you can call the same operation on either one


=> Participants 

   1. Component

      -> Common interface for all object 

  2. Leaf 

      -> Represent individual object 
      -> Cannot contain children 

  3. Composite

      -> Represent container 
      -> Can hold components 

=>  Composite Pattern: "Treat a single object and a collection of objects through the 
    same interface."          
"""