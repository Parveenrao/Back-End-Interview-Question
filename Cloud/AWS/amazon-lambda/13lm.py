""" 
-> AWS Lambda Worker Pool

    -> Worker pool is an internal concept in aws lambda that refers to the collection of execution
       environments (workers) that are available to execute lambda invocations


=> What is worker 

   -> A worker is an execution environments capable of running one lambda invocation at at time


   -> Internally worker consist of

        1. firecracker microvm
        2. Runtime 
        3. function code 
        4. memory 
        5. /tmp storage 
        6. execution env

    -> think of worker a single employee

    -> one employee can handle one customer at a time

=> Worker Pool

   -> A worker pool is simply many workers available for processing request

      
       worker pool 
          |-> worker 1
          |-> worker 2
          |-> worker 3
          |-> worker 4 
          |-> worker 5
          |-> worker 6

      when request arrive , lambda assigns them to availabe workers


=> How Request are processed 

Request 1
Request 2
Request 3

        │
        ▼

Worker Pool

├── Worker A  ◄── Request 1
├── Worker B  ◄── Request 2
└── Worker C  ◄── Request 3

each worker executes indepedently



=> Busy work scenario

   -> Suppose worker A is already executing


       Worker A 

       Running Request 1

   -> A second request arrives

       Request 2 -> worker A (busy) -> Scaling engine -> create worker B


   -> lmabda does not send two concurrent invocation to the same worker


=> Warm workers

   -> After a request finish

   worker A -> Invocation complete -> freeze -> Available for Reuse


   -> if another request arrives

      Request -> worker pool -> reuse worker A


=> cold work creation 

   -> if no idle worker exist 


     new request -> worker pool -> no available worker -> create new firecracker microvm -> new worker 

     -> execute 


    -> this is called cold start


=> Worker Pool vs Thread Pool


  Thread Pool	                                   Lambda Worker Pool
     Threads inside one process	                      Independent execution environments
     Shared memory	                                  Isolated memory
     Managed by application                           Managed by AWS
     Runs on one server	                              Runs across AWS infrastructure
     Thread executes tasks	                          Worker executes Lambda invocations

      A Lambda worker is much heavier than a thread because it includes a 
      runtime and runs inside a Firecracker MicroVM.    

      
=> Worke Pool and Concurrency

   -> Suppose function has a concurrency of 500

   500 concurrent request -> worker pool -> 500 worker -> 500 function running


=> Is Worker pool always running

   -> Lambda does not keep a fixed number of worker waiting forever

   -> instead 

      1. It reuse warm worker when possible 
      2. it creates new worker when demand increase 
      3. it removes idle worker

   -> worker pool is dynamic , constantly growing and shrinking based on traffic


=> What is a worker in AWS Lambda?

   -> A worker is an execution environment (implemented using a Firecracker MicroVM) 
      that runs a single Lambda invocation at a time.      

=> What is the worker pool?

    -> The worker pool is the collection of available execution environments 
       that Lambda uses to process incoming invocations.      

=> Can one worker process multiple concurrent invocations?

    -> No. A worker handles only one concurrent invocation. After it finishes, 
      AWS may reuse that worker for another invocation.    

=> Who manages the worker pool?

    -> AWS Lambda's internal Scaling Engine automatically creates, reuses, and removes workers based on demand.         
"""