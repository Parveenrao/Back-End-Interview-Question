""" 

=> AWS Scaling Engine

    -> The scaling engine is the component of the Lambda Data plane responsible for automatically

       increasing or decreasing the number of execution env based on incoming traffic

    -> The Scaling engine automatically creates or removes lambda execution env to match 
       demand

=> Why Does Lambda Need Scaling Engine

   -> Imagine function receives

       1 request now 
       100 request one second later 

       10,000 request during flash sale

       AWS must handle all of them automatically 

=> Without scaling engine

  1000 request -> 1 server -> long queue -> slow response


=> with scaling engine

   1000 request -> scaling engine -> 1000 execution env (sub to concurrency limits) -> process

=>  Where Does the Scaling Engine fit 



            Event

              │

              ▼

      Lambda Front-End

              │

              ▼

      Invocation Router

              │

              ▼

        Scaling Engine

              │

   ┌──────────┼──────────┐
   ▼          ▼          ▼

Environment  Environment  Environment
     A            B            C

              │

              ▼

        Execute Handler

        
=> One Env = One concurrent invocation


=> Automatic Scale-out

   -> Traffic increase 

      1 request -> 1 Environment

   -> Later

      100 request -> 100 env 

=> Automatic scale in

   100 env -> 500 -> 100 -> 10


   -> idle execution env are eventually removed by aws


=> Warm Evn Use

   -> before creating new execution environment , the scaling engine checks for reuse warm env


=> What does scaling engine consider

   1. Number of incoming request 
   2. Available warm execution env 
   3. Account and function concurrency limits 
   4. function configuration
   5. Regional service capacity

=> Scaling Vs. Concurrency 

   -> Scaling is the process of creating or removing executio env 

       10 request -> 10 env



   -> concurrency is the number of lambda invocation running at the same time

   -> Scaling engine creates enough execution envionments to support the required concurrency limit

      within configured limit

=> Does one execution environment handle multiple concurrent requests?
  
    -> No. One execution environment processes one concurrent invocation at a time.      

=> Does the Scaling Engine always create a new environment?

   -> No. It first checks for an available warm execution environment. 
      If one is available, it reuses it; otherwise, it creates a new one, 
      resulting in a cold start.
"""