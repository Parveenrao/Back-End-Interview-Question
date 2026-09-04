""" 


=> Amdahl' Law 

   
      -> Most Important principle in computer science 

      -> It explain why some optimizations produce huge speedups while others barely matters


=> What is Amdahl's Law

   -> The maximum speed of program is limited by the portion of the program that cannot be improved

   -> if only part of your program is optimized , the unoptimized part become the bottleneck



=> example 

    1. Imagine we are driving a car 100Km

    2. The journey consist of 

        80 KM highway 
        20 KM in city traffic

    
    3. Current speed 

       Highway = 80 km/hr 

       city = 20km/hr


    4. Now imagine buying a sports car

        highway speed doubles

        highway = 160 km/hr

        time = 80/160 => 0.5 hour


        city traffic remians the same


        0.5 + 1 => 1.5 hours


    5. Although the highway becomes 2X faster  , the whole journey improved by only 25%

        but the city traffic could not be optimized


=> Why was Amdahl's created


   -> In 1960s , people believed


      Lets keep adding CPU

   -> Amdahl asked 

        what if only part of the program can run in parallel

    -> He proved mathematically that adding more processes eventually give dimishing returns 

       because some work remain sequential


=> Mathematical Formulae


       Speedup  = 1 / (1-P) + p/s

       
       p -> fraction of the program that can be improved

       1-p -> fraction of the program that cannot be improved

       s -> speedup applied to the improved part 



=> Amdahls law is a performance opitmization principle that tells us the overall speedup of 
   system is limited by the portion of the program that cannot be optimized.

   it helps us decide where opitmization efforts will have biggest impact




"""