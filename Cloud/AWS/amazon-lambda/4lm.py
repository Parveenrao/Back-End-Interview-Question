""" 

=> AWS Lambda Function Lifecycle

    -> Lmabda function lifecycle describes what happens from the moment a lambda function
       invoked until the execution environment is destoryed

=> High Level Lifecycle



Function Created
       │
       ▼
Invocation Received
       │
       ▼
Is Execution Environment Available?
       │
 ┌─────┴─────────┐
 │               │
No              Yes
 │               │
 ▼               ▼
Cold Start    Warm Start
 │               │
 ▼               ▼
Initialize     Skip Initialization
Runtime
 │
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
Wait for Next Request
 │
 ▼
Reuse or Destroy



=> Phase 1 Function Deployment

   -> Before, execution you create a lambda function

   -> Include

      1. Upload code
      2. select runtime 
      3. Configure memory 
      4. configure timeout 
      5. Attach IAM role 
      6. Configure triggers


    -> Example

                Lambda Function

                   Code
                   Runtime
                   Memory
                   Timeout
                   IAM Role
                   Environment Variables  

    -> At this stage 

        No server is running


        AWS simply store our function


=> Phase 2 Invocation

    -> A request arrive 

      API Gateway -> lambda

      S3 upload -> Lambda 

      SQS message -> lambda 

      AWS now check

          Do I already have an execution environments

          Two possibilities exist 


    -> Case 1 Cold start 

      -> If no execution environments exist , Lambda creates one 

         Called cold start 


       -> cold start steps 


           Request -> Allocate compute -> Create firecracker MircroVM -> Start OS

           -> Load runtime(Python / java) -> download function code -> Load dependencies

           -> run intialization code 

       -> entire setup  happens before your handler runs

=> Phase 3 handler Execution

    After Intialization 

    AWS calls the handler 


            1. Receive the event 

            2. Process business logic 

            3. call database 

            4. Invoke APIs

            5. Reads S3

            6. Write DynamoDB

            7. Return Response

=> Phase 4 Response

    -> After execution

     lambda -> Serialize Response -> Return to caller 


=> Phase 5 Freeze

    -> lambda does not immediately destory the execution environemnt

    -> Instead 

        Memory 

        Variables 

        Runtime


        Freeze 


        -> think of laptop entering sleep mode instead of shutting down


=> Phase 6 Warm start


    -> Another request arrive shortly afterwards


    Request -> Existing environment found -> unfreeze -> execute handler 


    -> no runtime loading 

    -> no dependency loading 

    -> no code download 

    -> no intialization

   this is why warm start are much faster 


=> when is environment destroyed 

    1. AWS may destroy an execution environment when:

       -> It remains idle for some time 

       -> AWS need capacity 

       -> New code is deployed

       -> memory configuration changes 

       -> Runitime version change 

       -> infra maintenance occur

    after it is destroyed , next request experience another cold start 


=> complete lifecycle   


Deploy Function
        │
        ▼
Invocation
        │
        ▼
Execution Environment Exists?
        │
 ┌──────┴──────────┐
 │                 │
No               Yes
 │                 │
 ▼                 ▼
Create          Reuse
Environment     Environment
 │                 │
 ▼                 ▼
Load Runtime    Skip Init
 │
 ▼
Load Code
 │
 ▼
Initialize
 │
 ▼
Execute Handler
 │
 ▼
Return Response
 │
 ▼
Freeze
 │
 ▼
Wait
 │
 ▼
Reuse or Destroy



=> Production Best Practice

    1. Initialize expensive resources outside the handler 

         boto 2 clients , db connection so they can be reused across warm invocations 

    2. keep deployment package small to reduce start time 

    3. avoid heavy initialization logic unless it is necessary


=> 1. What is a cold start?
       -> A cold start occurs when Lambda must create a new execution 
          environment, initialize the runtime, load the function code, and run
         initialization code before invoking the handler.         

         
=> Does Lambda reuse execution environments?
     -> Yes. AWS may reuse an existing execution environment 
        for subsequent invocations, but reuse is not guaranteed.         

        
=> Can you rely on in-memory variables across invocations?
     -> No. They may persist in a reused environment, but Lambda can 
        create a new environment at any time, so your function must remain stateless.    


=> What is a warm start?
     -> A warm start reuses an existing execution environment, 
        skipping initialization and resulting in lower latency.            
"""