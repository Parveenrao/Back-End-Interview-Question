""" 
=> Freeze / Thaw 

    -> Freeze / Thaw is an optimization used by aws lambda to improve performance by resuing
       execution environments


       freeze = pause the execution env after the function finishes

       thaw = resume the paused execution env for a new invocation


    request -> INIT (cold start) -> invoke -> freeze -> next request -> thaw / shutdown

=> Why does lambda freeze

   -> creating a new execution env takes time

      1. creating firecracker microvm
      2. load runtime 
      3. download code 
      4. import library
      5. Run intialization

   this cause cold start

   instead of destorying the env immediately , aws pause it

   request -> execute -> freeze -> wait

   if another request arrive soon , lambda can reuse it

=> following are typically preserved while the env remains frozen 

    1. runtime 
    2. imported libraries
    3. global variable 
    4. sdk client 
    5. db connection
    6. /tmp files
    7. memory

   nthng is executing while frozen


=> What is thaw

   -> if another request arrive

      new request -> existing frozen env -> thaw -> execute handler

      aws resume the same execution env 

      no runtime loading 

      no imports 

      no init



"""