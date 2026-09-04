""" 
=> Builder 

    -> Builder Design Pattern is a creational design pattern that helps us to construct 
       complex object step by step

     -> Instead of Passing many parameteres to constructor or writing many setter calls , we use 
        builder to build the object  



"""

# Without builder Pattern -> Imagine we are creating a computer object 

computer = Computer(
    
    "Intel-19",
    "32GB",
    "1TB SSD",
    "RTX 4090",
    "Windows 11",
    "True",                  # here we cannot tell which argument for keyboard or monitor
    "True",
    "Mechanical",
    "Wireless",
    "4K "
)


"""

=> Example 

    -> Think of ordering a burger 

    -> we do not tell chef 

      Burger(
           bun,
           cheese,
           onion,
           tomato,
           lettuce,
           mayo,
           ketchup,
           extra_chesse)

    -> Instead we say 

      I want a burger -> Add cheese -> Add onion -> Add lettuce -> Done       

"""