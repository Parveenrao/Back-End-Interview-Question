""" 


=> CPU Profiling

    -> Cpu profiling is the process of measuring where your program spends its CPU execution time


    -> Which function take the most time 

    -> How many times each function call

    -> Which function is the bottleneck 

    -> Which function call other function

    -> how much time is spent inside a function versus its child fuction



=> CPU Profile Working 


    1. Instrument Profiling 

        -> This is what Python's cprofile use

        -> The profiler records every function call

    Function enter -> Start timer -> Execute fuction -> stop timer -> Recrod statistics


       -> Advantage 
          
           1. Very accurate 
           2. Exact all counts 
           3. Exact execution time

       -> Disadvantage 

          1. Adds runtime overhead 
          2. Slightly slows the program


    2. Statistical(Sampling) Profiling

       -> It perioidically checks which function is currently executing

       -> imgine program runs for 10 second

       -> The profilier check every millisecond

          Time 0ms   -> train()

          TIme 1ms   -> train()

          Time 2ms   -> train()

          Time 3ms   -> preprocess()

          Time 4ms   -> train()


        After 10000 samples 

           train -> 7200 samples 

           preprocess  -> 1800 samples 

           load()      -> 1000 samples

        Approximate CPU usuage

          train     72%

          preprocess()  18%

          load()          10%

      -> Disadvantage 

         -> Very short function calls may be missed


=> Wall Time

    -> wall time is the actual elapsed time measured by clock

        import time 

        time.sleep(5)

        wall time -> 5 second

        cpu time -> almost 0

        becuase during sleep , cpu is idle

=> CPU Time 

   -> Actual time processor actually spends executing your code 

    for _ in range(10000)

       total += 

   CPU is busy the entire time


=> Profile Metrics 

    1. Call count

       -> how many times a function executed

          
           for _ in range(100):
               square()

         square() -> 100 calls

    2. Total time (tottime)

       -> Time spend inside the fucntion itself 

       -> It exclude time spend in child function


           def B():
                heavy_work()

           def A():
               B()


             heavy work = 10 second

             B itself = 0.2 second 

             total time = 0.2 second


   3. Cumulative time (cumtime)

       -> time spend in fuctiona and plus all functions it calls

       A -> B -> heavy_work()

       heavy_work = 10 second

       B = 0.2 second 

       cumtime = 10.2 second

   4. Per-call time 

        Average execution time per function call

        Average time = Total time / number of calls


        function time = 12 second 

        calls  = 6 second

        Average = 2 second


=> Hotspot

    -> A hotspot is the section of code consuming the most CPU time


"""