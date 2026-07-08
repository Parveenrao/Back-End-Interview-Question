""" 

=> AWS Lambda Execution Model

     -> Execution model describe how AWS lambda execut our function when event arrives, including

        how execution environments are created , reused and scaled


     -> Think of it as the runtime behaviour of lmabda from receiving an event to completing 

        execution


=> high level execution model

                 Event
                   │
                   ▼
         Lambda Front-End Service
                   │
                   ▼
          Invocation Router
                   │
                   ▼
      Find Execution Environment
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
 Existing Environment     Create New Environment
     (Warm Start)            (Cold Start)
        │                     │
        └──────────┬──────────┘
                   ▼
           Execute Handler
                   │
                   ▼
           Return Response
                   │
                   ▼
          Freeze Environment
                   │
                   ▼
         Wait for Next Invocation

         

=> Step 1 Event Arrival

   -> Any event can come from many aws service 

   -> example 

       HTTP Request 
       S3 upload 
       SQS message 
       sns notification
       dynamodb stream
       eventbridge schedule
       cloudwatch alarm

    -> every event is coverted into a standard invocation request 

                          {
                     "event": {
                          ...
                        },
                   "function": "OrderProcessor"
                 }   


=> Step 2 Lambda Front-End

    -> Lambda Frontend is responsible for 

        1. Receiving invocation request 
        2. Authenticating the request 
        3. Checking IAM permission
        4. Applying concurrency limits
        5. sending the request to correct region

     User -> Lambda API -> Authentication -> Authorization -> Request Routing


=> Step 3 Invocation Router

   -> Router decide 

        Can an existing environments handle this request 

    -> it checks 

        1. function version
        2. memory size 
        3. runtime 
        4. architecture (x86/ARM)
        5. Availability of warm environment

    -> if one exist 

        Request -> warm env

    -> Request 

        Create new env


=> Step 4 Execution Enviornment

   -> An execution environment contains everything needed to run your function

                          Execution Environment

                              ├── Firecracker MicroVM
                              ├── Runtime (Python, Java, Node.js...)
                              ├── Function Code
                              ├── Dependencies
                              ├── Environment Variables
                              ├── Temporary Storage (/tmp)
                              └── Memory

        each environment executes one invocation at a time

    -> important Rule 

        One execution evironment  = One concurrent invocation

        100 request = 100 execution env

        lambda does not run multiple concurrent invocations inside the same execution env.


=> Step 5 Intialization Phase (Cold start)

    -> IF aws create a new env

    Create firecracker vm -> load runtime -> load function code -> load lib -> run global intialization -> ready


=> Step 6 Handler Execution

     AWS calls 

        lambda_handler(event , context)

     During execution our function can

      1. Read from s3 
      2. write to dynamodb
      3. call apis
      4. access RDS
      5. send sns notification
      6. push to sqs

=> Step 7 Response 

    After the handler finishes

    handler -> serialize response -> return to caller 

=> Step 8 Freeze 

    -> Instead of destroying the env immediately 

    execution finished -> freeze memory -> freeze runtime -> wait 

    env remain avaiblabe for reuse

=> Step 9 Warm Execution

  -> if another request arrives


    New request -> Resue env -> execute handler 

=> Automatic Scaling

    -> 1 request = 1 env.

    -> later 

       1000 request = 1000 env.

    lambda automatically creates more execution env to process concurrent request , subject 
    to your accounts concurrency limits


    -> When traffic decrease

       1000 -> 500 -> 100 -> 10


       unused env are eventually removed    

"""