""" 

=> WHy are strings are immutable in python 

  
     1. Immutable meaning in python

         -> An immutable object cannot be modified after it is created 

         s = "hello"
         
         s = s.replace("h" , "H")

         Original "hello" never changed 

         A new string "Hello" was created 

         Variable s now points to new object 


    2. Memory Efficiency

        suppose 

        a = "python"
        b = "python"


        python often store only once copy of "python" in memory

                        +-----------+
            a -------->| "python"  |
                        +-----------+
            b -------->|     

    3. Hashibility (Dicitionary keys)

       -> Dict keys must never change

       -> immutable strings gurantees

             hash never change 
             dictionay remai correct 

    4. Faster hashing 

       -> Since string never change

       -> Python compute hash only once 


    5. Thread safety

       -> Suppose two thread 

          Thread A reads -> "hello"

          THred B changge  hello -> world

          Thread A gets incosistent data 

          Immutable string remove this issue


          Multiple thread can safely read the same string simultaneously 

    6. Resuse Across Entire program

        Suppose program contains 

          "Error"

          500 times 

          Instead of storing

          Error
          Error
          Error
          Error
          Error


         Python may keep only one object 

         Huge memory saving                    

"""